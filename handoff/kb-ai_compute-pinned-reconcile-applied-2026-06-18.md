# KB → quant · #135 reconcile APPLIED — ai_compute pinned graph re-served

**Date:** 2026-06-18 · **From:** KB · **To:** quant
**Re:** `handoff/quant-ai_compute-pinned-reconcile-2026-06-18.md` (your gold reconcile of the pinned export)
**Updated artifact:** `handoff/kb-chain-pinned-ai_compute-2026-06-18.json` (re-served, post-reconcile).

Your reconcile was surfaced in the #41 curation panel and the operator disposed all items. revenue_share
needed no change (your MAE 0.0000 — v0.3 already overrode the distiller confounds).

## Applied (firewall: human re-pinned every direction; KB only ever set ±)
1. **6 over-determined `+1` → `±`** — operator re-pinned all 6 as presence-only (confirmed your gold
   two-sided call): 天孚→旭创 (300394→300308), 天孚→新易盛 (300394→300502), 北方华创→中芯 (002371→688981),
   NVDA→浪潮 (000977), Samsung→中环 (005930→002129), Samsung→长电 (005930→600584). Mechanism: KB flipped
   each to review:pending at ± (approve() can't demote a +1); operator re-approved ± in the panel.
2. **TSMC↔中芯 competitor stray `revenue_share` → null** — cleared (competitor = presence-only by definition).
3. **蓝思** (AAPL→300433.SZ customer) — already ingested + pinned `+1` / `revenue_share 0.49` (gold 0.495).

## Final pinned state (105 approved ai_compute edges)
- Sign distribution: **80 `+1` · 10 `−1` · 15 `±`** (was 86/10/9; the 6 demotes moved +1→±).
- **Directional edges without a `sign_basis`: 0** ✅ (SIGN_BASIS_REQUIRED rail held throughout).
- revenue_share: unchanged except the one competitor clear; provenance 9 GOLD / 17 null / rest estimate.

## Next (the loop)
KB has re-served the pinned ai_compute graph (this artifact) → the slice-hash has shifted (expected).
Quant: re-pin the graph anchor to the new slice-hash → run the ADR-0077 #126 B-aggregate over the pinned
graph (the staged exposure-vector output, mil_defense analogue). (#138 new_energy 002129 verification is
separate/in-flight.)

firewall_ok=true · approve=false (human pinned).
