# Handoff (KB → quant): supplier + raw_material distiller batches — ai_compute (#141 / #135)

**Date:** 2026-06-17
**Artifacts:**
- `handoff/kb-distiller-batch-ai_compute-supplier-2026-06-17.json` (18 edges)
- `handoff/kb-distiller-batch-ai_compute-raw_material-2026-06-17.json` (2 edges)
- schema `kb-distiller-candidates@1`. Companion to the customer batch (`…-customer-2026-06-17.json`).

Same target-scoped, disclosure-grounded method as the customer batch (each target's latest cninfo annual
report → 前五名X window → DeepSeek top-1 share + verbatim span). 5 new supplier targets were ingested
(中芯国际/长电科技/兆易创新/中科曙光/紫光国微, 2025年报). Same FIREWALL: `transmission_sign` ± never
pinned, `directional_weight` 0, citation-required `[AI·待核]`, number≠name, honest-null.

## supplier — 7/18 disclosed (TARGET's top-1 SUPPLIER share = source's % of the buyer's procurement)
| target | revenue_share | cited span |
|---|---|---|
| 中际旭创 | 0.3576 | 供应商A 35.76% |
| 浪潮信息 (×3 edges) | 0.3314 | 供应商一 33.14% |
| 新易盛 | 0.2387 | 第一名 23.87% |
| 紫光国微 | 0.2144 | 供应商一 21.44% |
| 德方纳米 | 0.1302 | 第一名 13.02% |
| 中芯国际 / 长电科技 / 兆易创新 / 中科曙光 / 工业富联 | **null** | 前五大供应商合计 only, no top-1 split — honest-null |

Subject = the **TARGET's procurement** (the buyer's COGS-share to the source), NOT the source's own
customer-concentration (anti-confound enforced in the prompt).

## raw_material — 0/2 disclosed (honest-null)
`COMM:COPPER → 东山精密` and `COMM:COPPER → 深南电路`: both null. Both PCB makers disclose only
**aggregate 直接材料** in 营业成本构成 — no copper-specific cost share. The rule refuses to report the
aggregate 直接材料 % as copper's share (it would overstate). **Structural limitation:** A-share filings
rarely break out a single commodity's cost share, so raw_material is intrinsically low-yield from filings
alone; consider a 研报/industry-data source for commodity cost shares if needed.

## Flags / number≠name
- supplier shares are ANONYMIZED (供应商一/供应商A) — the name→SOURCE attribution is the chain map's
  claim, not proven by the filing. Confirm before pinning.
- The 浪潮信息 0.3314 appears on 3 supplier edges (it's 浪潮's single top-1 supplier share; only one of
  those source attributions can be the actual #1 — human disposes).

## Next
Same as the customer batch: quant scores vs gold (#135) → human pins sign + confirms attribution →
B-aggregate (#129). The cninfo-fetch + target-scoped distiller is reusable for any scope/edge_type.
