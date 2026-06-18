# KB → quant · ai_compute revenue_share v0.3 — APPLIED + human-pinned (DONE, #135 → #41)

**Date:** 2026-06-18 · **From:** KB · **To:** quant
**Re:** `handoff/quant-ai_compute-revenue_share-v0.3-recuration-2026-06-18.md` + `…-v0.3-proposed.json`
**Updated artifact:** `handoff/kb-chain-pinned-ai_compute-2026-06-18.json` (schema `kb-pinned-chain-edges@1`).

KB surfaced v0.3 in the #41 `REVENUE_SHARE_BASIS_REQUIRED` curation rail and the operator pinned. Your
gold-corrected v0.3 supersedes the distiller batch KB applied earlier the same day (the distiller's
anonymized top-1 shares were exactly the null-honesty FAIL you flagged → now corrected).

## revenue_share v0.3 applied (23 edges changed, firewall-preserving)
Applied via the daemon PATCH path — payload carried **only** `revenue_share`/`revenue_share_basis`, so
`transmission_sign`/`sign_basis` were preserved (canary-verified on a numeric and a null edge):
- **pin_gold_disclosed:** 立讯 0.71 · 东山 0.50 · 海光 0.90 · 寒武纪 0.80 · 深南 0.15
- **adopt_gold_estimate (incl. the 3 subject-fixes):** 天孚→旭创 0.10 · 天孚→新易盛 0.05 · 北方华创→中芯 0.05 · NVDA→旭创 0.24 · 铜→东山 0.15
- **down_to_presence_only (revenue_share=null, edge present/weightless):** 10 edges — NVDA→天孚, AAPL→歌尔, 浪潮, 沪电, 新易盛(cust), 工业富联×2, 中环, TSM→深南, 005930→长电
- **kept_v0.2 reverts (the 4 distiller conflicts):** 深南/德方纳米×2/紫光 → v0.2 estimate

## Node+edge add + sign pins (human firewall acts)
- **蓝思科技 added:** node `300433.SZ` + `AAPL→300433 customer` — operator pinned **+1**, **revenue_share 0.49** (gold disclosed_point 49.5%), cited basis.
- **3 TSM sign-pins:** TSM→北方华创(002371) **+1** · TSM→长电(600584) **+1** · TSM→中芯(688981) **±** (left two-sided per §4).

## Firewall / final state
104 approved ai_compute edges: **95 directional, 0 without `sign_basis`** (rail held). Sign distribution
86 `+1` / 10 `−1` / 9 `±`. revenue_share provenance: 9 GOLD-adjudicated · 17 null (presence-only) · rest estimate.
The machine pinned no signs — every ±1 is a human, source-cited act.

## Next
The pinned values shifted the slice hash (expected). Quant: re-pin the graph anchor → ADR-0077 B-aggregate
(#126) reads the pinned revenue_share. The 3 浪潮 supplier ambiguities + remaining honest-null edges stay as
flagged (operator disposition pending if needed for the aggregate).
