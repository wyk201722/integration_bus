# Handoff (KB → quant): first §5 customer-distiller batch — ai_compute (#141 / #135)

**Date:** 2026-06-17
**Artifact:** `handoff/kb-distiller-batch-ai_compute-customer-2026-06-17.json` (schema `kb-distiller-candidates@1`)
**This is the milestone quant parked on:** KB extract-side emitting `revenue_share` candidates → quant
scores vs gold (#135) → human pins → feeds B-aggregate (#129).

## What this is
KB's first live batch of the §5 **customer** distiller for the `ai_compute` traded universe (13 edges,
12 unique targets). Each `revenue_share` is the **TARGET's top-1 (第一大) customer share** — the
quant-ratified Q2 subject (`= target's sales to that customer ÷ target's own revenue`).

## Method (disclosure-grounded, target-scoped)
- Fetched each target's **latest annual report** from cninfo/巨潮 (2025年报 — recency rule), via the
  announcement API (code→orgId→name). Ingested into the `reobsidian_business` vault.
- **Target-scoped extraction:** read the target's OWN annual-report note (resolved by
  `sourceId == weburl:sha256(url)[:16]`, collision-proof), extracted its 前五名客户/客户集中度 window,
  DeepSeek distilled the top-1 share + the EXACT verbatim span.
  - (An earlier RAG-global retrieval returned mixed-company chunks → all-null; target-scoping fixed it.)

## Results — 11/13 disclosed, 2 honest-null
| edge | target | revenue_share | cited span |
|---|---|---|---|
| AAPL→002475 | 立讯精密 | 0.5668 | 客户一 56.68% |
| NVDA→300394 | 天孚通信 | 0.6331 | Fabrinet 63.31% (filing NAMED it) |
| AAPL→002384 | 东山精密 | 0.4646 | 第一名 46.46% |
| NVDA→000977 | 浪潮信息 | 0.3937 | 客户一 39.37% |
| AAPL→002241 | 歌尔股份 | 0.2972 | 客户一 29.72% |
| NVDA→300308 | 中际旭创 | 0.2406 | 客户A 24.06% |
| NVDA→300502 | 新易盛 | 0.2297 | 第一名 22.97% |
| NVDA→002463 | 沪电股份 | 0.1426 | 客户一 14.26% |
| 005930→002129 | TCL中环 | 0.0991 | 客户一 9.91% |
| NVDA→002916 | 深南电路 | 0.0746 | 第一名 7.46% |
| NVDA→300769 | 德方纳米 | 0.3903 | 第一名 39.03% — ⚠️ see flags |
| AAPL/NVDA→601138 | 工业富联 | **null** | 前五大客户合计 only, no top-1 split (富士康 customer confidentiality) — honest-null |

## Firewall (unchanged, asserted)
- `transmission_sign` = **±** on every candidate (machine NEVER pins). `directional_weight` = 0.0.
- Every `revenue_share` carries a cited `revenue_share_basis` = `[AI·待核] <verbatim span>`. No span → null.
- **number ≠ name:** the filings disclose an ANONYMIZED top-1 share (客户一/客户A/第一名). The NAME
  attribution (is 客户一 = NVDA/AAPL?) is the chain map's claim, NOT proven by the filing. Advisory only.

## Flags for quant / human last-look
- **`NVDA→300769` (德方纳米) is a likely GRAPH ERROR.** 德方纳米 is a lithium-iron-phosphate battery
  cathode maker — not an NVDA compute-chain supplier. The distiller honestly extracted 德方纳米's own
  top-1 customer share (0.39), but that top-1 is almost certainly NOT NVDA. Recommend rejecting the edge
  (the number is real for 德方纳米; the source attribution is wrong).
- **`number ≠ name` applies to ALL rows** — please confirm each anonymized top-1 actually IS the chain
  SOURCE before pinning (esp. multi-customer targets like 工业富联 where Apple/NVDA both appear).

## Next
quant scores these vs gold (#135 MAE) → human pins the sign + confirms the name attribution → feeds
B-aggregate (#129) + ADR-0075 D2. KB can run the same distiller for `supplier`/`raw_material` edge_types
and other scopes on request (the cninfo annual-report fetch + target-scoped pipeline is now reusable).
