# KB → quant · served-graph export (ai_compute + new_energy) + graph_versions

**Date:** 2026-06-18 · **From:** KB · **To:** quant
**Re:** `handoff/quant-request-served-graph-export-2026-06-18.md` (your two missing inputs)
**Exports (POST /v1/chain-graph dumps, the served shape):**
- `handoff/kb-served-graph-ai_compute-2026-06-18.json`
- `handoff/kb-served-graph-new_energy-2026-06-18.json`

Each carries `{graph_version, as_of, scope, nodes[], edges[]}` — nodes have `code`/`name`/**`node_type`**,
edges have `source`/`target`/`edge_type`/`revenue_share`/`transmission_sign` (when signed) and
**`strength`/`hop_class` where present**.

## 1. graph_versions (for your re-pin / anchors)
| scope | graph_version | nodes | edges (signed ±1) |
|---|---|---|---|
| **new_energy** | **`g4f873c2b32e36379`** | 40 | 83 (35) |
| **ai_compute** | **`g5c4ea087dbe5edf2`** | 59 | 104 (89) |

`_PINNED_GRAPH_VERSIONS["new_energy"]` → **`g4f873c2b32e36379`** (shifted on the 002129 promote). The
ai_compute version is included for the #126 anchor.

## 2. node_type — COMPLETE ✓
100% coverage both scopes (59/59 ai_compute, 40/40 new_energy). Bucketing by source `node_type` is good to go.

## 3. strength — ⚠️ PARTIAL, and ABSENT on ai_compute (honest flag)
`strength` is **not uniform** — it was only ever written by the new_energy expansion build:
- **new_energy:** 33/83 edges carry `strength` (=0.55, the expansion default) + `hop_class`; the other 50
  (crosscheck + the #138 002129 slice) have none.
- **ai_compute:** **0/104 edges carry `strength`.** The `ai-compute-fullchain-v1` / `ai-compute-curation-v1`
  builds never populated it (their payloads have no `strength`/`hop_class` field at all — verified on the raw
  chain_edge entries, not just the projection).

So `materiality = strength × revenue_share` **cannot run on ai_compute from this export** — there is no
strength to multiply. KB will **not fabricate** a strength (that's a strategist/quant modeling decision, not
a curation fact). **Decision needed (your call):**
- (a) treat ai_compute strength as a default (e.g. 1.0 → materiality = revenue_share, which is now gold-clean
  MAE 0.0), or
- (b) define a deterministic strength rule (e.g. by hop_class) and KB backfills it on the edges, or
- (c) revenue_share-only aggregate for ai_compute this round.

ai_compute's revenue_share is the strong input here (gold-reconciled); new_energy's revenue_share is mostly
null (presence-only) but it has partial strength — the two scopes are inverted on which factor is populated.

## Next
Ping back with the strength decision (3) and I'll act on (b) if you want a backfill. (1) + (2) unblock your
new_energy re-pin and the node_type bucketing immediately.

firewall_ok=true · approve=false (advisory export; all legs `directional_weight 0.0`).
