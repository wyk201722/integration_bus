# Runbook: How to run an orchestrated cross-project session

> Operator manual. Read this once before starting a session; refer back when steps drift.

## Roles in the room

- **You (human)** — start / supervise the session, escalate when the orchestrator says so, sign off on milestones
- **Terminal A** — Claude Code CLI running with cwd `~/Desktop/wyk/stock/`
- **Terminal B** — Claude Code CLI running with cwd `~/Desktop/wyk/reobsidian/`
- **Terminal C (orchestrator)** — Claude Code CLI running with cwd `~/Desktop/wyk/integration-bus/`

All three CLIs read their own `AGENTS.md` and follow the shared protocol.

## One-time prep

### Both project AGENTS.md files include an "Integration Mode" section

- `~/Desktop/wyk/stock/AGENTS.md` has an `Integration Mode` section pointing to `integration-bus/AGENTS.md` (already in place).
- `~/Desktop/wyk/reobsidian/AGENTS.md` needs a similar section. **Suggested text** (paste under a new `## Integration Mode` heading near the bottom):

  > When working on a task that spans the quant side (`~/Desktop/wyk/stock/`), follow the protocol in `~/Desktop/wyk/integration-bus/AGENTS.md`. Specifically:
  > 1. Before starting a cross-project task, read `~/Desktop/wyk/integration-bus/instructions/kb-next.md`.
  > 2. After each meaningful step (daemon up, test pass/fail, blocker), append a JSONL line to `~/Desktop/wyk/integration-bus/state/kb.jsonl` using the schema in `integration-bus/AGENTS.md`.
  > 3. Do **not** modify peer instruction files or `goal.md` — those are the orchestrator's.

  This is an addition the human owner of reobsidian needs to make once.

## Starting a session

1. **Decide the goal** (with the human, or have the orchestrator propose one).
2. In Terminal C, write the goal to `goal.md` (overwrite the previous goal; preserve the History table).
3. In Terminal C, write `instructions/quant-next.md` and `instructions/kb-next.md` for the first step of each side.
4. In Terminals A and B, prompt the project CLI:
   > "Read `~/Desktop/wyk/integration-bus/instructions/<your-project>-next.md` and follow it. Log events to `state/<your-project>.jsonl` per the protocol in `~/Desktop/wyk/integration-bus/AGENTS.md`."
5. Both peers work; they append events as they go.

## The orchestrator loop

In Terminal C, the orchestrator runs this loop (manually invoked or by a watcher script):

```
1. cat goal.md                                   # ground itself
2. tail -n 50 state/quant.jsonl
3. tail -n 50 state/kb.jsonl
4. tail -n 20 state/orchestrator.jsonl           # what did I decide last time
5. reason about progress (closer / further / blocked)
6. write/overwrite instructions/quant-next.md and/or kb-next.md
7. append a reasoning line to state/orchestrator.jsonl
8. tell the human "I just updated <files>; next checkpoint is event <X>"
```

The human's job: nudge each peer CLI to re-read its instruction file when the orchestrator updates it.

## The watcher (Phase 1.5)

A small Python daemon (`watch.py` at the bus root) removes the polling burden:
it tails all three state files, pretty-prints new events to its terminal, and
fires macOS desktop notifications when **high-signal events** appear. The human
only needs to look at Terminal C when a notification fires.

### Starting the watcher

Open a fourth terminal (Terminal D) at `~/Desktop/wyk/integration-bus/` and run:

```bash
make watch
# OR (variants)
make watch-quiet   # no desktop notifications, just colored tail
make watch-loud    # also write wakeup events to orchestrator.jsonl
make status        # dump last 30 min of events and exit
make recent        # dump last 2 h, then continue tailing
```

First run is slow (~30 s) — `uv` resolves `watchdog` + `rich` from PEP 723 inline
metadata. Subsequent runs start instantly. No separate venv setup needed.

### What the watcher does

- **Console tail**: each new line in `state/{quant,kb,orchestrator}.jsonl` is
  rendered with color-coded agent + event name + truncated summary
- **Recent context**: on startup, dumps the last 10 minutes of events for grounding
- **macOS notification** (`osascript` based, zero dependencies) for any event in
  the high-signal set:
  `blocker`, `test_failed`, `daemon_ready`, `daemon_down`, `milestone_reached`,
  `request_help`, `instruction_done`
- **Wakeup events** (with `--wakeup` / `make watch-loud`): when a peer emits a
  high-signal event, the watcher appends a synthetic `wakeup` event to
  `state/orchestrator.jsonl`. Next time the orchestrator agent is invoked, its
  tail naturally surfaces "watcher saw quant emit test_failed at 10:32" as a
  clear marker. Recommended for autonomous orchestration sessions.
- **Failure safe**: parse errors on individual JSONL lines are reported inline
  but never crash the watcher; notification failures are silently swallowed.

### What the watcher does NOT do

- It does **not** invoke the orchestrator agent (no `claude --print` injection).
  The human still types into Terminal C to prompt a new orchestrator cycle.
  Phase 2 (MCP server) will close this gap.
- It does **not** read peer terminal output directly — peers must cooperate by
  appending JSONL events to their state file per the schema in this workspace's
  `AGENTS.md`.

### Typical four-terminal layout

```
┌─────────────────────────┬─────────────────────────┐
│ Terminal A (stock-quant)│ Terminal B (reobsidian) │
│  claude code            │  claude code            │
└─────────────────────────┴─────────────────────────┘
┌─────────────────────────┬─────────────────────────┐
│ Terminal C (orchestrator│ Terminal D (watcher)    │
│ integration-bus)        │  make watch             │
│  claude code            │                         │
└─────────────────────────┴─────────────────────────┘
```

The watcher in D lights up your menu bar via macOS notification when something
interesting happens; you then bring Terminal C forward and prompt the
orchestrator agent to re-run its decision loop.

## Event log conventions

See the schema in `~/Desktop/wyk/integration-bus/AGENTS.md`. The 11 standard event names cover most cases. If you need a new event type, **first add it to AGENTS.md** (in the table), then use it.

Avoid:
- Long `summary` lines (over 200 chars) — put detail in `payload`
- Skipping the `blocks_on` field on `blocker` events
- Writing free-form events that other agents won't recognize

## Closing a session

When `goal.md`'s DoD checklist is fully met:

1. Orchestrator appends a `milestone_reached` event to `state/orchestrator.jsonl`
2. Orchestrator creates `milestones/<YYYY-MM-DD>-<short-name>.md` containing:
   - Final goal text
   - DoD check (all green)
   - Pointer to the underlying gate file in either project
   - Joint signoff path (e.g. `reobsidian/docs/design/memory-extension/sign-offs/quant-signoff-m0-live-<date>.md`)
   - Per-side commit hashes at completion
3. Orchestrator overwrites `goal.md` with the next goal (or `goal: idle` if none queued)
4. Both peers may emit `instruction_done` and idle

## Common situations

### A peer hits a blocker

- Peer appends `blocker` event with `blocks_on` set
- Orchestrator next cycle:
  - If `blocks_on: "human"`: write the escalation into `goal.md`'s `Escalation` section, stop
  - If `blocks_on: "kb"` or `"quant"`: write a new instruction to the **blocking** side that addresses the root cause
  - Never instruct the blocked side to "try again" without changing something — that's a busy loop

### Contract drift surfaced by L4

- Quant emits `test_failed` with payload describing the mismatch (e.g. response header casing)
- Orchestrator writes an instruction to KB describing the contract clause that's violated
- Orchestrator does **not** edit `reobsidian-kb-contracts/` — the contract is signed; either fix the implementation to match, or both sides agree to bump the contract via PR (which is its own ADR + signoff cycle)

### Peer goes silent

- Orchestrator notices `tail -n 5 state/<peer>.jsonl` is unchanged for >30 minutes
- Append `nudge_requested` to `state/orchestrator.jsonl` with `payload.peer = "..."` and tell the human

## Phase 2 preview (when Phase 1 friction warrants)

Replace the filesystem protocol with a Python MCP server that exposes:

- `coordinator/report_status(event, payload, blocks_on?)` — typed equivalent of appending to state.jsonl
- `coordinator/check_instructions()` — read the current instruction file as structured JSON
- `coordinator/await_peer_event(event_name, timeout_sec)` — block until peer emits a given event
- `coordinator/issue_instruction(target_project, command, rationale)` — orchestrator-only

Phase 2 also adds:
- Authentication (per-project tokens) so the wrong CLI can't impersonate the other
- Audit signing (each event signed by the writer) — useful when the human reviews a session later
- A `watcher` daemon that auto-prompts the orchestrator CLI when peer events arrive
