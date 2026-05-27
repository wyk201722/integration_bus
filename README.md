# integration-bus

Shared filesystem-based coordination workspace for cross-project work between
`stock-quant` and `reobsidian`.

## Why this exists

The two projects sit in adjacent directories under `~/Desktop/wyk/`:

```
~/Desktop/wyk/
├── stock/                # stock-quant (A-share quant multi-agent system)
├── reobsidian/           # reobsidian (KB / memory backend)
└── integration-bus/      # ← you are here
```

When work spans both repos (e.g., running L4/L5 KB contract harness tests, debugging KB
contract drift, planning a contract version bump), neither repo's AGENTS.md alone can drive
the loop. This workspace holds the **shared goal**, **peer status logs**, and **coordinator
instructions** so a third Claude session can orchestrate the two.

## Operating model

```
                      goal.md  (orchestrator writes)
                          ↓
              ┌───────────┴───────────┐
              ↓                       ↓
        instructions/             instructions/
        quant-next.md             kb-next.md
              ↓                       ↓
        ┌──────────┐            ┌──────────┐
        │  Quant   │            │   KB     │
        │  CLI     │            │   CLI    │
        │ Terminal │            │ Terminal │
        │    A     │            │    B     │
        └──────────┘            └──────────┘
              ↓                       ↓
        state/quant.jsonl       state/kb.jsonl
              ↓                       ↓
              └───────────┬───────────┘
                          ↓
                  orchestrator (Terminal C)
                  reads, decides, writes
                  new instructions
```

## How to start a coordination session

See [`runbooks/how-to-orchestrate.md`](runbooks/how-to-orchestrate.md).

Short version:

1. Open **four terminals**:
   - **A** — Claude Code CLI in `~/Desktop/wyk/stock/`
   - **B** — Claude Code CLI in `~/Desktop/wyk/reobsidian/`
   - **C** — Claude Code CLI in this directory (the orchestrator)
   - **D** — `make watch` from this directory (the watcher daemon)
2. Decide the goal in C, write it to `goal.md`, write initial instructions
3. Each project terminal reads its instructions, executes, appends events to its `state/*.jsonl`
4. Watcher (D) tails state, pretty-prints, fires macOS notifications on high-signal events
5. Orchestrator (C) loops: tail state, decide, write next instructions
6. When the goal is achieved, append a record to `milestones/`

## Quick commands (from this directory)

```bash
make watch       # tail state + macOS notifications on high-signal events
make watch-loud  # also write wakeup events to orchestrator.jsonl
make status      # dump last 30 min of events and exit
make goal        # show current goal.md
```

First `make watch` run is slow (~30 s) — uv resolves dependencies once.

## Phase status

- **Phase 1** (current): filesystem-based protocol. Each side cooperates via AGENTS.md instructions.
- **Phase 2** (future): wrap the protocol in an MCP server (`coordinator/report_status`, `coordinator/check_instructions`, `coordinator/await_peer_event`) so the conventions are enforced by the tooling rather than by prompt cooperation.

## Files

| Path | Owner | Purpose |
|---|---|---|
| `AGENTS.md` | orchestrator | Persistent context for the orchestrator agent |
| `goal.md` | orchestrator | Current cross-project goal |
| `state/quant.jsonl` | quant CLI (append) | Quant-side event log |
| `state/kb.jsonl` | KB CLI (append) | KB-side event log |
| `state/orchestrator.jsonl` | orchestrator (append) | Orchestrator's reasoning log |
| `instructions/quant-next.md` | orchestrator | Pending instruction for quant CLI |
| `instructions/kb-next.md` | orchestrator | Pending instruction for KB CLI |
| `milestones/<date>-*.md` | orchestrator | Append-only log of completed goals |
| `runbooks/how-to-orchestrate.md` | human + orchestrator | Operator manual |
