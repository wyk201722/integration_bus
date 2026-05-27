# 2026-05-23 — DecisionPayload v2 + EvidenceRef Amendment

## Goal (closed)

Diagnose and resolve `KBValidationError 400` on `POST /v1/entries` for `category='decision'` writes — surfaced via stock #345 re-diagnosis on 2026-05-23, originally framed as a daemon-vs-system schema drift.

## Resolution path

Routing audit traced the symptom to a stock-quant ADR drift (ADR-0013 / ADR-0023 / 2026-05-19-amend, all `Decider: cyril (solo)`, no reobsidian counter-party, no contracts-repo PR). The signed `reobsidian-kb-contracts/schemas/entry.json` was internally consistent across both sides (per-$def byte-equality on all shared $defs including DecisionPayload); the stock-quant production write path had outgrown the contract via unilateral ADRs that never made it onto the bus.

Two legal paths from `quant_internal`: (A) revert prod to the signed `{action, candidate_signal_ids, arbitration}` shape (lossy mapping; loses `evidence_refs[].weight`, `decision_id`, `position_size_recommendation`, etc.); (B) formal amendment via bus-negotiated contracts-repo PR. Orchestrator chose Path B on the grounds that the rich fields carry semantic content downstream KB consumers (RAG queries, narrative pattern matching, lesson extraction, decision audit replay) will want.

Round-3 produced a `v2` proposal (`handoff/quant-proposed-decisionpayload-2026-05-23-v2.json`, 21694 B, sha256 `d5c941a7424619c6491a973fc5abfe691d05f94eb54ab7b00267abf5446acbea`) bundling:
- Replace `$defs.DecisionPayload` (3-field pre-ADR-0013 → 12-field post-ADR-0013 shape)
- Add `$defs.EvidenceRef` (authoritative ADR-0011 form `{signal_id, pn_agent, weight}`, supersedes KB's floor-stub per pre-acceptance)
- Sibling additive doc-update to `#/properties/confidence` description for `category=decision` coupling

Round-4 applied the v2 + a same-PR back-port of `NarrativeAnalogPayload` from the reobsidian in-tree copy to the standalone repo (Option C, closes round-2 structural-drift housekeeping). Both schema files now byte-equal at sha256 `afded066c6a82e54269d8c542765145297b00c688bde7ca17dd345824beee6f0`. Daemon restarted from PID 11380 to 90406 with the new validator compiled at boot. 693 SLO-fixture rows under the old shape deleted at migration step. Stock-quant L4 / L5 / SLO fixtures realigned. `Decision.to_kb_entry_payload()` updated at `src/stock_quant/signals/contract.py:1598` to emit `payload.conviction` (satisfies v2's new required-set; intentional duplication with outer `entry.confidence` per archival-completeness principle). Production write gate (`STOCK_KB_DECISION_WRITES_DISABLED`) removed.

## DoD final state

| # | DoD item | Status | Evidence |
|---|---|---|---|
| 1 | KB posts literal `KBValidationError` ajv detail for probe payload | MET | `state/kb.jsonl` `probe_ajv_errors` event 2026-05-23T17:20:30 — 3 missing-required errors against `{}` probe |
| 2 | KB confirms daemon-loaded `DecisionPayload` schema status vs contracts HEAD | MET | `state/kb.jsonl` `schema_sha256_report` event 2026-05-23T17:20:31 — per-$def byte-equality confirmed across both sides |
| 3 | Quant posts exact failing payload bytes + contracts revision built against | MET | `handoff/quant-decision-probe-2026-05-23.json` (6598 B, sha256 `f7295289…` on-wire 1250 B) + `state/quant.jsonl` 2026-05-23T17:02 |
| 4 | Orchestrator issues routing verdict | MET | `state/orchestrator.jsonl` 2026-05-23T18:00:00 milestone_reached — verdict `quant_internal`, Path B formal-amendment |
| 5 | Re-run reproduces 200 on the same payload | MET | KB own smoke `state/kb.jsonl` `daemon_ready` 2026-05-23T18:02:26 — 200 with ULID `01KSA4GJ5TRCV89QKSGDRD8HF3`; quant own smoke `state/quant.jsonl` `smoke_test` 2026-05-23T20:14:00 — 200 with ULID `01KSA54B06YJ8RDGM5M7GC7KET` |
| 6 | `make test-live` 11/11 GREEN against @2 | MET | `state/quant.jsonl` `instruction_done` 2026-05-23T20:40:00 — L4 8/8 + L5 3/3 = 11/11 PASS (kb_contract scope) |
| 7 | `make test-slo` 4/4 within budget | MET | REST write 0.93ms / GET 0.50ms / search 0.62ms / WS push 2.80ms (all P95) — well within 200/200/500/1000 ms budgets despite ~6× payload growth |
| 8 | Prod un-gated and verified live | MET | env var deleted; in-process spy probe confirms `KBSink.deliver()` no longer short-circuits Decision payloads |
| 9 | Stock #345 closed with cross-project trace | LOCAL ONLY | Closed via stock-side TaskUpdate; GitHub-side closure deferred to operator (gh CLI not authenticated in this session) |

## Contract changes ratified

Single commit on `reobsidian-kb-contracts`: `bc870154c868cf8c475137a748543c81e6d0f6d1` — `feat(contracts): DecisionPayload v2 + EvidenceRef (ADR-0011/0013/0023/0013-amend bus-ratified 2026-05-23)`. **Local-only at present** — push to remote (`wyk201722/reobsidian-kb-contracts`) blocked by auto-classifier on KB side; needs human authorization to publish externally. In-tree copy at `reobsidian/contracts/schemas/entry.json` synced byte-equal in the same operation.

Schema operations applied:
1. **Replace `$defs.DecisionPayload`** — required set changes from `[action, candidate_signal_ids, arbitration]` to a 12-field set (no overlap with the prior set). New required: `agent_id, agent_version, decision_id, symbol, direction, conviction, horizon_bucket, position_size_recommendation, systemic_risk_ceiling, evidence_refs, llm_path_used, conflict_detected`. Optional retained: `llm_cost_usd, conflict_resolved_by, reason, red_team_dissent_id`. Removed entirely (no v0.2 back-compat): `risk_check, redteam, disprove, outcome` (each has a documented separate landing place per stock-quant ADR-0014 / ADR-0035 / ADR-0037; `outcome` stays post-hoc PATCH path).
2. **Add `$defs.EvidenceRef`** — `{signal_id (required), pn_agent (required), weight (required, 0..1)}`. Authoritative ADR-0011 form; supersedes KB's floor-stub per pre-acceptance.
3. **Add `$defs.NarrativeAnalogPayload`** (back-port from reobsidian in-tree copy at commit `52900ab`) — closes round-2 structural-drift housekeeping; same-PR additive op, no schema-break risk.
4. **Update `#/properties/confidence` description** — additive Chinese sentence covering `category=decision` coupling (mirrors the existing `category=event` clause); no shape change.

Schema version bump: `memory-store@1 → memory-store@2`. Major (non-backwards-compatible — required-set fully disjoint). Encoded at: `entry.json` doc-level + `packages/memory-daemon/src/routes/healthz.ts:62` constant. Daemon `/v1/healthz` now advertises `schema_version: memory-store@2`.

Migration: `DELETE FROM entries WHERE category='decision'` — exactly 693 rows (matches expected SLO-fixture count, zero archival value per round-3 audit). No production-shape decision data observed on KB side at migration time. Gated emissions during the production write-gate window (`STOCK_KB_DECISION_WRITES_DISABLED=1`, engaged 2026-05-23T17:16:48 → un-gated 2026-05-23T20:30:00) are unrecoverable per the drain plan (architecture does not journal gated payloads); honest accounting recorded.

## Carry-forward items (non-blocking)

| # | Item | Owner | Notes |
|---|---|---|---|
| 1 | `reobsidian-kb-contracts` commit `bc870154` not pushed to GitHub | KB + human | Auto-classifier blocked external push. Local HEAD satisfies bus trace; quant uses directly. Publish externally when authorization sorted. |
| 2 | `bin/kb-daemon.mjs:278` boot banner still hardcodes `schema=memory-store@1` | KB | Cosmetic only; `/v1/healthz` is the load-bearing source of truth (correctly @2). |
| 3 | Stock #345 GitHub-side closure | Quant + human | Closed via local TaskUpdate; needs gh-CLI auth for formal GitHub closure. |
| 4 | KB-side category-routing bug | KB | `tests/integration/test_rag_client_narrative_analog::test_narrative_analog_filter_disjoint_from_narrative` returns decision rows under `narrative_analog` filter. Surfaced during quant's broader `@l4/@l5` marker run on this round. NOT caused by this amendment — pre-existing. Separate bug to triage. |
| 5 | Pytest `.env` auto-loading | Quant | 6 integration tests under `@l4/@l5` marker scope fail via `make test-live` because pytest doesn't auto-source `.env`. Per-test invocations are clean. Housekeeping; not caused by this amendment. |
| 6 | Persistence design for future gating | Both | Current architecture loses decisions during gating windows (no journal/retry queue). If future fixes require gating again, design needs revisiting. Out of scope here. |

## Session metrics

| Metric | Value |
|---|---|
| Orchestrator decision cycles | 5 (rounds 1 / 2 / 3 / 4 + this closure) |
| Wall clock (cycle open → milestone close) | ~3 h 50 min |
| KB instruction revisions | 4 (00:00 / 11:00 / 18:00 / 19:00) |
| Quant instruction revisions | 4 (00:00 / 11:00 / 18:00 / 19:00) |
| Blockers raised | 2 (KB round-2 sha256 mismatch — closed orchestrator-side as non-substantive; KB round-1 events off-bus — backfilled in round-2) |
| Audits overturning preliminary verdict | 1 (round-1 preliminary "contracts-repo gap" → round-2 corrected to `quant_internal` after per-$def byte-equality finding) |
| Contract amendments ratified | 1 (this one) |
| Schema version bumps | 1 (`memory-store@1 → @2`) |
| Daemon restarts | 1 (PID 11380 → 90406; first restart since 2026-05-20 20:14) |
| Migration rows deleted | 693 |
| Handoff artifacts produced | 3 (`quant-decision-probe-2026-05-23.json`, `quant-proposed-decisionpayload-2026-05-23.json` (v1, frozen), `quant-proposed-decisionpayload-2026-05-23-v2.json`) |
| Production data loss during gating window | 0 (no scheduler ticks fired; both peers' in-process probes were synthetic) |

## Cross-references

- Goal: `goal.md` (this session — transitioning to `idle` post-closure)
- Bus state: `state/orchestrator.jsonl` (5 decision-cycle entries 2026-05-23T00:00 → T18:00), `state/kb.jsonl` lines 13-25, `state/quant.jsonl` lines 43-64
- Prior milestone: `milestones/2026-05-15-m0-l4l5-live.md` (M0 L4+L5 row, closed 2026-05-15 — defined the v1 baseline this amendment evolves from)
- Stock #345: closed via local TaskUpdate; cross-project trace lives in this bus's state files
