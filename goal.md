# Current cross-project goal

> The orchestrator overwrites this file each time a goal changes.
> Both peer CLIs (quant + kb) read this when they want to reground.

## Goal

**goal: idle** — DecisionPayload v2 + EvidenceRef amendment milestone closed 2026-05-23. No new cross-project goal queued.

See `milestones/2026-05-23-decisionpayload-v2-amendment.md` for the closed milestone record. The next goal will be set by the human; peers may stand by or work on within-project tasks per their own AGENTS.md.

## Why this state

- All 9 DoD items of the prior goal are green or LOCAL-ONLY-closed (see milestone file's DoD table).
- KB daemon (PID 90406, embedded mode) running on `http://127.0.0.1:7733` with `schema_version: memory-store@2` advertised. Orchestrator did not instruct teardown — the daemon stays up by default per the same continuity principle as 2026-05-15.
- `reobsidian-kb-contracts` HEAD `bc870154` is **local-only** (auto-classifier blocked the push). Quant uses it directly via local clone; sha256 matches KB advertisement. For external publication, KB push requires human authorization (carry-forward #1 in milestone file).

## Definition of done

- *(none — no active goal)*

## Open questions

- Next cross-project goal — what's the priority? Candidates surfaced by the closed milestone's carry-forwards and prior session:
  1. Authorize KB push of `bc870154` to `wyk201722/reobsidian-kb-contracts` so the signed artifact is externally visible
  2. KB cosmetic — bump `bin/kb-daemon.mjs:278` boot banner `schema=memory-store@1` to `@2`
  3. Stock #345 GitHub-side formal closure (gh CLI auth)
  4. KB-side bug — `rag_client_narrative_analog::test_narrative_analog_filter_disjoint_from_narrative` returns decision rows under narrative_analog filter (pre-existing, surfaced during this cycle's test run; NOT caused by amendment)
  5. Quant housekeeping — pytest `.env` auto-loading for `make test-live` integration tests under `@l4/@l5` marker scope
  6. Persistence design for future gating windows (current architecture loses gated emissions)
  7. Re-bench search SLO once Qdrant is up (carry-forward from 2026-05-15)
  8. Drive M0 Earnings-Event Agent vertical slice (stock-side P2 work per `stock/.plans/gate-M0.md`)

## Escalation

- (none active)

## Ratified contract values (preserved post-amendment for daemon-restart / new-session continuity)

- `KB_BASE_URL` = `http://127.0.0.1:7733`
- `KB_API_KEY` (dev) = `dev-key-001-padded-to-thirty-two-chars` (38 chars)
- HTTP auth header = `X-API-Key`
- Scopes = `memory:read | memory:write | memory:subscribe`
- **`schema_version` = `memory-store@2`** (bumped 2026-05-23 from `@1`; non-backwards-compatible — DecisionPayload required-set fully disjoint)
- **`reobsidian-kb-contracts` HEAD = `bc870154c868cf8c475137a748543c81e6d0f6d1`** (local-only on KB; quant has the same hash via direct clone)
- **`schemas/entry.json` sha256 = `afded066c6a82e54269d8c542765145297b00c688bde7ca17dd345824beee6f0`** (byte-equal across reobsidian-kb-contracts standalone + reobsidian in-tree copy post Option-C apply)

## History

| Date | Status | Note |
|---|---|---|
| 2026-05-15 | goal opened | Initial bootstrap by human |
| 2026-05-15 | DoD corrected | Orchestrator first-cycle verification: L4 has 8 tests not 6 (test_a, _b, _c, _c2, _d, _d2, _e, _f); total is 11 not 9 |
| 2026-05-15 | KB daemon up | Embedded daemon listening @ 127.0.0.1:7733, commit 54e30ab, PID 9137 (shell-desktop dev:fast subprocess) |
| 2026-05-15 | Contract amendment | API key length renegotiated 11 → 38 chars to satisfy KB auth-design §4 ≥32. Value `dev-key-001-padded-to-thirty-two-chars` now authoritative for this session. Original `blocker` event (kb.jsonl:3) resolved by ratification. |
| 2026-05-15 | Quant unblocked | quant-next.md rev 13:00:00+08:00: wait-state lifted; quant instructed to run `make test-live` with ratified env values |
| 2026-05-15 | First live run | 4/11 pass. 7 fails in 2 clusters, all categorized `contract_drift` by quant. |
| 2026-05-15 | Routing audit | Orchestrator audit against signed `reobsidian-kb-contracts/`: **both clusters are quant test-fixture bugs, not KB drift**. Quant's recommended ownership rejected. |
| 2026-05-15 | Quant re-instructed | quant-next.md rev 13:30: fix `_decision_payload()` + change `test_f` to assert `hits`, re-run. KB stand-by. |
| 2026-05-15 | Correctness GREEN | 11/11 pass (L4 8/8 + L5 3/3) in 1.30s. Daemon stable. KB confirmed `candidate_signal_ids` is shape-only validated. Quant also fixed test_l5_live_ws.py (correct scope expansion). |
| 2026-05-15 | DoD: 2 items remaining | quant→SLO P95 bench; KB→signoff doc. Parallel instructions issued (rev 13:45). |
| 2026-05-15 | SLO GREEN | 4/4 P95 within budget (write 1.02ms / GET 0.56ms / search 0.84ms / WS push 5.56ms) with 180–595× headroom. Caveats: loopback only, Qdrant down, WS push includes REST write. |
| 2026-05-15 | Signoff drafted | KB created `quant-signoff-m0-live-2026-05-15.md` at the spec path (4051 B, all sections populated). |
| 2026-05-15 | **M0 L4+L5 closed** | All 5 DoD items green. Milestone file: `milestones/2026-05-15-m0-l4l5-live.md`. Goal transitioned to `idle`. |
| 2026-05-23 | **New goal opened** | Quant reports KB-key works (healthz 200) but `category='decision'` writes now return `KBValidationError 400` — daemon-vs-system schema drift surfaced via stock #345 re-diagnosis. Diagnostic round-1 issued. |
| 2026-05-23 | Round-2 evidence in | **Preliminary verdict corrected.** Per-$def byte-equality confirmed (KB and quant DecisionPayload identical, both pre-ADR-0013 shape). Routing verdict: `quant_internal` — confirmed independently by both peers. |
| 2026-05-23 | KB sha256 blocker closed | Orchestrator closes per per-$def equality (DecisionPayload byte-identical; divergence purely additive on KB side via `NarrativeAnalogPayload`). |
| 2026-05-23 | Path B chosen | Formal amendment via bus (KB reviews quant's proposed patch, joint commit to `reobsidian-kb-contracts`, `schema_version` bump). Path A (revert prod) rejected — loses semantic content downstream consumers want. |
| 2026-05-23 | Round-3 converged | KB verdict: `counter_propose` (patch refs missing `$defs.EvidenceRef`). Quant verdict: `accept`. Authored v2 at `handoff/quant-proposed-decisionpayload-2026-05-23-v2.json` (21694 B, sha256 `d5c941a7…`) — DecisionPayload unchanged from v1, bundled authoritative `$defs.EvidenceRef` per ADR-0011. Sticking points: zero. |
| 2026-05-23 | Round-4 apply landed | KB committed `bc870154` to `reobsidian-kb-contracts` (local-only; push blocked by auto-classifier). Option C in-tree-vs-standalone reconciliation taken — `NarrativeAnalogPayload` back-ported same-PR (closes round-2 housekeeping). Daemon restarted PID 11380 → 90406; healthz advertises `memory-store@2`. 693 SLO-fixture rows DELETE'd at migration. Quant pulled, cross-check passed, realigned L4 + L5 + SLO fixtures (3rd occurrence caught organically), updated `Decision.to_kb_entry_payload()` to emit `payload.conviction`, un-gated prod, `make test-live` 11/11 GREEN, `make test-slo` 4/4 within budget (REST write 0.93ms / GET 0.50ms / search 0.62ms / WS push 2.80ms — well within budgets despite ~6× payload growth). Stock #345 closed locally. |
| 2026-05-23 | **DecisionPayload v2 milestone closed** | All 9 DoD items met or LOCAL-ONLY-closed. Milestone file: `milestones/2026-05-23-decisionpayload-v2-amendment.md`. Goal transitioned to `idle`. 6 non-blocking carry-forwards flagged. |
