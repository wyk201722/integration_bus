#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "watchdog>=4.0",
#   "rich>=13.7",
# ]
# ///
"""integration-bus state watcher.

Tails ``state/{quant,kb,orchestrator}.jsonl``, pretty-prints new events,
fires macOS desktop notifications on high-signal events, and (optionally)
appends ``wakeup`` events to ``orchestrator.jsonl`` so the orchestrator
agent sees a clear "something happened" marker on its next cycle.

Phase 1.5 of the integration-bus: the orchestrator agent still has to be
invoked by the human, but the watcher removes the polling burden — the
human only intervenes when a notification fires.

Usage
-----
    ./watch.py                       # default: notify + console tail
    ./watch.py --no-notify           # silence macOS notifications
    ./watch.py --wakeup              # also write wakeup events for orchestrator
    ./watch.py --since 30m           # dump last 30 min and exit (status check)
    ./watch.py --since 2h --tail     # dump last 2 h, then keep tailing live

First run will be slow as uv resolves watchdog + rich; subsequent runs
are instant.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from collections.abc import Iterator
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from rich.console import Console
from rich.text import Text
from watchdog.events import FileModifiedEvent, FileSystemEventHandler
from watchdog.observers import Observer

# ============ Constants ============

BUS_ROOT = Path(__file__).resolve().parent
STATE_DIR = BUS_ROOT / "state"

PEER_FILES: dict[str, Path] = {
    "quant": STATE_DIR / "quant.jsonl",
    "kb": STATE_DIR / "kb.jsonl",
    "orchestrator": STATE_DIR / "orchestrator.jsonl",
}
ORCHESTRATOR_LOG = PEER_FILES["orchestrator"]

# Events that warrant orchestrator attention (notify + optional wakeup).
HIGH_SIGNAL_EVENTS: set[str] = {
    "blocker",
    "test_failed",
    "daemon_ready",
    "daemon_down",
    "milestone_reached",
    "request_help",
    "instruction_done",
}

# Color palette
AGENT_COLOR: dict[str, str] = {
    "quant": "cyan",
    "kb": "magenta",
    "orchestrator": "yellow",
    "watcher": "dim",
}

console = Console()


# ============ Helpers ============


def os_notify(title: str, body: str) -> None:
    """Fire a macOS desktop notification. No-op on non-darwin platforms.

    Notification failure must NEVER crash the watcher — wrapped in broad
    try/except by design.
    """
    if sys.platform != "darwin":
        return
    # Escape double quotes in the body to keep osascript happy.
    safe_body = body.replace('"', "'")
    safe_title = title.replace('"', "'")
    try:
        subprocess.run(
            [
                "osascript",
                "-e",
                f'display notification "{safe_body}" with title "{safe_title}"',
            ],
            check=False,
            timeout=5,
            capture_output=True,
        )
    except Exception:  # noqa: BLE001  watcher must survive notification failure
        pass


def append_wakeup(triggering: dict[str, Any]) -> None:
    """Append a synthetic ``wakeup`` event to orchestrator.jsonl.

    Lets the orchestrator's next-cycle tail see a clear marker that the
    watcher noticed a high-signal event from a peer.
    """
    wakeup = {
        "ts": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "agent": "watcher",
        "event": "wakeup",
        "summary": (
            f"high-signal event detected: "
            f"{triggering.get('agent', '?')}/{triggering.get('event', '?')}"
        ),
        "payload": {
            "triggered_by": triggering.get("agent"),
            "triggering_event": triggering.get("event"),
            "triggering_ts": triggering.get("ts"),
        },
        "blocks_on": None,
    }
    with ORCHESTRATOR_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(wakeup, ensure_ascii=False) + "\n")


def format_event(event: dict[str, Any]) -> Text:
    """Render one event as a colored, single-line Rich Text."""
    agent = str(event.get("agent", "?"))
    name = str(event.get("event", "?"))
    ts = str(event.get("ts", "?"))
    summary = str(event.get("summary", ""))
    blocks_on = event.get("blocks_on")

    agent_color = AGENT_COLOR.get(agent, "white")
    event_color = "bold red" if name in HIGH_SIGNAL_EVENTS else "green"

    text = Text()
    text.append(f"{ts}  ", style="dim")
    text.append(f"[{agent}]".ljust(15), style=agent_color)
    text.append(name.ljust(22), style=event_color)
    text.append(summary[:100])
    if blocks_on:
        text.append(f"  blocks_on={blocks_on}", style="bold red")
    return text


def iter_jsonl(path: Path, start_pos: int = 0) -> Iterator[dict[str, Any]]:
    """Yield JSON objects from each line of ``path``, starting at byte offset.

    Malformed lines are reported inline and skipped — never crash the loop.
    """
    if not path.exists():
        return
    try:
        with path.open("r", encoding="utf-8") as f:
            f.seek(start_pos)
            for raw in f:
                line = raw.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except json.JSONDecodeError as e:
                    console.print(f"[red][parse error] {path.name}: {e}[/red]")
    except OSError as e:
        console.print(f"[red][read error] {path.name}: {e}[/red]")


# ============ Watchdog handler ============


class StateChangeHandler(FileSystemEventHandler):
    """Watch state/*.jsonl files for appends; print + optionally notify/wakeup."""

    def __init__(self, *, notify: bool, wakeup: bool) -> None:
        # Remember the byte offset of each file at watcher start;
        # we'll only emit lines appended after that.
        self.positions: dict[Path, int] = {
            p: (p.stat().st_size if p.exists() else 0) for p in PEER_FILES.values()
        }
        self.notify = notify
        self.wakeup = wakeup

    def on_modified(self, event: FileModifiedEvent) -> None:  # type: ignore[override]
        path = Path(event.src_path)
        if path not in self.positions:
            return
        prev_pos = self.positions[path]
        try:
            new_pos = path.stat().st_size
        except OSError:
            return
        if new_pos <= prev_pos:
            # File shrunk or unchanged (truncate / atomic rewrite). Reset baseline.
            self.positions[path] = new_pos
            return

        for ev in iter_jsonl(path, prev_pos):
            console.print(format_event(ev))
            self._maybe_react(ev, source=path)
        self.positions[path] = new_pos

    def _maybe_react(self, ev: dict[str, Any], source: Path) -> None:
        name = ev.get("event")
        if name not in HIGH_SIGNAL_EVENTS:
            return
        if self.notify:
            os_notify(
                title=f"integration-bus: {ev.get('agent', '?')}",
                body=f"{name}: {str(ev.get('summary', ''))[:120]}",
            )
        if self.wakeup and source != ORCHESTRATOR_LOG:
            # Never wake on orchestrator-emitted events — would cause feedback loop.
            append_wakeup(ev)


# ============ Modes ============


def parse_since(s: str) -> timedelta:
    """Parse '30m', '2h', '1d' into a timedelta."""
    s = s.strip().lower()
    if s.endswith("m"):
        return timedelta(minutes=int(s[:-1]))
    if s.endswith("h"):
        return timedelta(hours=int(s[:-1]))
    if s.endswith("d"):
        return timedelta(days=int(s[:-1]))
    raise argparse.ArgumentTypeError(
        f"--since wants suffix m/h/d (e.g. '30m', '2h', '1d'), got {s!r}"
    )


def show_recent(window: timedelta) -> None:
    """Print all events from the last ``window`` across all peer files, sorted by ts."""
    cutoff = datetime.now(timezone.utc).astimezone() - window
    bag: list[dict[str, Any]] = []
    for path in PEER_FILES.values():
        for ev in iter_jsonl(path):
            ts_raw = str(ev.get("ts", ""))
            try:
                # Tolerate both 'Z' and explicit offsets
                ev_ts = datetime.fromisoformat(ts_raw.replace("Z", "+00:00"))
                if ev_ts.tzinfo is None:
                    ev_ts = ev_ts.replace(tzinfo=timezone.utc)
                if ev_ts >= cutoff:
                    bag.append(ev)
            except ValueError:
                continue
    bag.sort(key=lambda e: str(e.get("ts", "")))
    for ev in bag:
        console.print(format_event(ev))
    if not bag:
        console.print(f"[dim](no events in the last {window})[/dim]")


# ============ Main ============


def main() -> None:
    parser = argparse.ArgumentParser(
        description="integration-bus state watcher",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--no-notify",
        action="store_true",
        help="Disable macOS desktop notifications on high-signal events",
    )
    parser.add_argument(
        "--wakeup",
        action="store_true",
        help="Append 'wakeup' events to orchestrator.jsonl on high-signal "
        "peer events (gives the orchestrator a clear next-cycle marker)",
    )
    parser.add_argument(
        "--since",
        type=parse_since,
        default=None,
        help="Show events from the last N (m/h/d) and exit unless --tail",
    )
    parser.add_argument(
        "--tail",
        action="store_true",
        help="With --since, dump the window then continue tailing live",
    )
    args = parser.parse_args()

    if not STATE_DIR.exists():
        console.print(f"[red]state/ directory missing at {STATE_DIR}[/red]")
        console.print(
            "[dim]Did you run from inside integration-bus/? "
            "Or has the bus been initialized?[/dim]"
        )
        sys.exit(1)

    # --since mode (with optional --tail continuation)
    if args.since is not None:
        console.rule(f"Events in the last {args.since}")
        show_recent(args.since)
        if not args.tail:
            return
        console.rule("Live tail")

    # Banner
    console.rule("integration-bus watcher")
    console.print(f"Watching: [bold]{STATE_DIR}[/bold]")
    console.print(
        f"Notifications: [{'red' if args.no_notify else 'green'}]"
        f"{'OFF' if args.no_notify else 'ON'}[/]    "
        f"Wakeup events: [{'green' if args.wakeup else 'red'}]"
        f"{'ON' if args.wakeup else 'OFF'}[/]"
    )
    console.print(
        f"High-signal events: [bold]{', '.join(sorted(HIGH_SIGNAL_EVENTS))}[/bold]"
    )
    console.print("[dim]Press Ctrl+C to stop.[/dim]")
    console.print()

    # Default: show last 10 minutes for context, then live tail.
    if args.since is None:
        console.rule("Recent (last 10 min)")
        show_recent(timedelta(minutes=10))
        console.print()
        console.rule("Live tail")

    handler = StateChangeHandler(notify=not args.no_notify, wakeup=args.wakeup)
    observer = Observer()
    observer.schedule(handler, str(STATE_DIR), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n[dim]Stopping watcher...[/dim]")
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
