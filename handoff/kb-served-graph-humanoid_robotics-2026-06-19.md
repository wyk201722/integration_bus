# KB → quant · humanoid_robotics served as a THEMATIC / emerging basket

**Date:** 2026-06-19 · **From:** KB · **To:** quant
**Served export:** `handoff/kb-served-graph-humanoid_robotics-2026-06-19.json` (`POST /v1/chain-graph {scope}` shape)
**firewall_ok=true · approve=false** (advisory deliverable for quant to score)

## graph_version
- **humanoid_robotics = `g8b1386949e76ccd1`** · as_of 2026-06-19T06:00:48Z · **47 nodes / 33 edges** · 0 dangling.

## ⚠️ SECTOR-MATURITY FINDING — score this DIFFERENTLY from ai_compute
humanoid_robotics is an **early-stage / pre-material chain (~Stage 1 of 3, ~2 stages behind ai_compute=Stage 3).**
KB ran the curation copilot (web-grounded, cheap local-crawler path) over **every un-pinned edge** — and they returned
**all `±` (no defensible direction)**. That is the *correct* result, not a miss: every public signal is **intent /
capability** (战略合作框架协议/合资, 产品发布 e.g. Codroid 02, "灵巧手超级工厂"规划, 研究院/平台展示, 柯力六维力
"小批量→批量化过渡" = the only Stage-2 edge) — **not operating revenue.** None of these companies disclose these
relationships in 前五大客户/供应商 (immaterial → undisclosed), so there is **no revenue_share to distill** here.

**Implication for #126 / scoring:** treat humanoid as a **THEMATIC / OPTIONALITY / presence basket** (presence +
stage weighting), **NOT** a revenue-weighted materiality graph. Running `exposure_by_revenue_share` on it would be a
**category error** — most edges are presence-only by nature, not by missing data. (Detail of the per-edge web evidence
lives KB-side at `docs/verification/hr-suggestions-2026-06-19.json`.)

## Composition (33 served edges)
- **signs:** `+1` ×9 (prior **human-pinned** core — established edges), `±` ×14 (presence-only periphery, incl the 10
  KB just approved), unset ×10. → small directional core, large thematic body.
- **edge types:** supplier ×24, customer ×9. **node types:** midstream 24 / upstream 12 / downstream 11.
- 7 edges carry a revenue_share, 19 carry a strength (from the original scaffold; not refreshed — pre-material).
- **FIREWALL:** the machine pinned **no** direction. The 9 `+1` are prior human pins; everything KB touched is `±`.

## What KB did this round (all firewall-safe)
1. Copilot search over all 10 un-pinned edges (cheap path: WebSearch → KB's own crawler → DeepSeek; no Claude-WebFetch
   blowup). All → `±`.
2. Cleaned the queue: rejected 2 inferior **bare duplicate** edges, backfilled source/target names on 5 bare edges.
3. Approved the 10 as **presence-only `±`** + tagged `stage:emerging` (also tagged the 28 prior-approved edges).
4. **Created 5 `chain_node` entries** to clear Guard-2 — 2 expected (873593.BJ 鼎智科技; UNLISTED:TESLA_OPTIMUS) **plus 3
   that fixed a PRE-EXISTING bug**: human-pinned `+1` edges whose targets never had nodes and were silently dropping —
   **UNLISTED:AGIBOT (智元机器人), UNLISTED:UNITREE (宇树科技), 300124.SZ (汇川技术)**. All 3 now serve.

## Flags / cleanup candidates (non-blocking)
- **Orphan node `OPTIMUS`** ("Tesla Optimus 量产需求") is unused — the edges use `UNLISTED:TESLA_OPTIMUS` (now created).
  Merge/delete `OPTIMUS` at leisure.
- **5 duplicate approved edge entries** exist (same source,target,edge_type); the served graph dedupes them (33 distinct
  from 38 entries) — harmless, cleanup candidate.
- **industry_sw2 peer-assigned** on 鼎智科技/汇川/AGIBOT/UNITREE (sector-default 801078.SW / 801731.SW) — quant may refine
  (cf the 002129 precedent).

## Operator pin status
The operator opted **not** to run a directional pin pass on the emerging edges (they stay `±`, which is honest for a
pre-material chain). They may later pin specific `+1` (e.g. 拓普集团→Optimus) from filings/domain knowledge; KB will
re-serve if so (graph_version will shift).
