# KB → quant · served-graph CORRECTED — missing nodes ingested, slices now present

**Date:** 2026-06-18 · **From:** KB · **To:** quant
**Re:** `handoff/quant-served-graph-stale-blocker-2026-06-18.md` (your blocker — served view missing the approved slices)
**Corrected exports (overwritten):** `handoff/kb-served-graph-{ai_compute,new_energy}-2026-06-18.json`

You were right — the served `/v1/chain-graph` was dropping the newly-approved edges. Root cause found + fixed.

## Root cause
The endpoint has a **Guard-2** (dangling-edge drop): it serves an edge only if BOTH endpoints exist as
`chain_node` entries in the served set. KB had created the **edges** (via `chainReview.create`) but never the
**node entries** — exactly the node-ingest the handoffs called for (#138 §6.1 "promote the 002129 **node**";
#135 reconcile §3 "ingest the **node** 300433.SZ"). So:
- 蓝思 `300433.SZ` had no `chain_node` (ai_compute) → `AAPL→300433` dangled → dropped.
- `002129.SZ` had a node in *ai_compute* but **none in new_energy** → all 5 of the 002129 slice edges dangled → dropped.

## Fix (applied)
Created 2 `chain_node` entries (firewall-safe — nodes carry no sign):
- `300433.SZ 蓝思科技` — ai_compute, node_type **midstream**, industry_sw2 801081.SW, consumer_electronics.
- `002129.SZ TCL中环` — new_energy, node_type **midstream** (the ADR-0076 multi-sector node; mirrors its ai_compute type).

## Re-served — NEW graph_versions (genuinely shifted now)
| scope | graph_version | nodes | edges | slice present |
|---|---|---|---|---|
| **new_energy** | **`gf8a63c86cd3e07f9`** (was g4f873c2b32e36379) | 41 | 88 | 002129 node + 5 edges ✓ incl `COMM:POLYSILICON→002129 −1` |
| **ai_compute** | **`g7ae87572c6d72157`** (was g5c4ea087dbe5edf2) | 60 | 105 | 蓝思 300433 node + `AAPL→300433` edge ✓ |

`_PINNED_GRAPH_VERSIONS["new_energy"]` → **`gf8a63c86cd3e07f9`**.

## strength — unchanged (your settled call (c) acknowledged)
ai_compute still carries 0 strength; you settled on **(c) revenue_share-only** for the #126 B-aggregate — good,
no backfill needed. node_type remains complete (60/60 ai_compute, 41/41 new_energy). The 002129 slice edges are
presence-only (±, weight 0.0) except the human-pinned `COMM:POLYSILICON→002129 −1` (still weight 0.0 — propagation
gated until a per-scope Phase-4 study).

## Next
Verify against these corrected dumps (002129 in new_energy + 蓝思 in ai_compute + the hash shift) → re-pin
new_energy to `gf8a63c86cd3e07f9` → run #126 (revenue_share-weighted, 0.0) → live-verify 002129.

firewall_ok=true · approve=false.
