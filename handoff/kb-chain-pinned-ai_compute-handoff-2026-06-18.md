# Handoff (KB → quant): human-pinned ai_compute chain edges — ready for scoring + B-aggregate (#135 / #129)

**Date:** 2026-06-18
**Artifact:** `handoff/kb-chain-pinned-ai_compute-2026-06-18.json` (schema `kb-pinned-chain-edges@1`)
**Source of truth:** reobsidian memory-daemon `chain_edge` entries, tag `review:approved`, scope `ai_compute`.

The operator has finished the **human pin pass** in the Chain-Edge Curation panel — the pending
queue is fully drained (ai_compute 36 → 0). This hands the **approved, sign-pinned** edge set to
quant so the directional graph can be **scored vs gold (#135)** and **B-aggregated (#129)** — the
ai_compute analogue of the staged `mil_defense` graph.

## What's in the batch
| | count |
|---|---|
| approved edges | **104** |
| ├ directional (±1) human-pinned | **95**  (`+1`: 85, `−1`: 10) |
| └ presence-only (`±`, approved, no direction) | 9 |
| carry a `revenue_share` | 97 |
| **directional edges WITHOUT a `sign_basis`** | **0** ✅ |
| rejected (recorded for audit) | 1 |

By edge_type: `supplier` 39 · `policy_driver` 24 · `customer` 15 · `capex_driver` 12 · `raw_material` 10 · `competitor` 4.

## Firewall (what quant can rely on)
- **`transmission_sign` of ±1 was set ONLY by the human `approve()` path.** Mining/creation only
  ever writes `±` (presence-only). Every one of the 95 directional edges carries a human-entered
  `sign_basis` (the daemon `SIGN_BASIS_REQUIRED` rail held — 0 violations).
- Each record also carries the **machine `proposed_sign` / `proposed_sign_basis`** — included
  **only so you can compare** human-pinned vs machine-advisory. They are NOT the binding sign.
- The 9 presence-only edges are approved-as-real but **directionless** — treat as edge-exists, no sign.

## Data-quality flags (number ≠ name; cited ≠ estimate)
- **`revenue_share_basis` is mixed provenance.** Some are cited disclosure spans; some are machine
  `估计/estimate:` rationales from the fullchain build-out. Check `revenue_share_basis` before using
  a share as a measured weight. The precise, disclosure-grounded shares live in the separate
  **distiller batches** (`kb-distiller-batch-ai_compute-{customer,supplier,raw_material}-2026-06-17.json`)
  — prefer those for revenue_share; this batch is authoritative for the **pinned signs**.
- Supplier/customer shares in filings are **anonymized** (供应商一/客户A); the name→node attribution
  is the chain map's claim, not proven by the filing.

## Next
1. Quant: score the 95 directional edges vs gold (#135); fold into B-aggregate (#129) → staged
   `ai_compute` graph.
2. Reconcile `revenue_share` against the 2026-06-17 distiller batches (disclosure-grounded) where
   they overlap, so the aggregate uses cited shares not estimates.
3. The 1 rejected edge is included for audit symmetry (don't aggregate it).

_Aside (not part of this handoff): the daemon also holds a large `scope:business` approved/rejected
set (≈200 approved / ≈194 rejected) from a separate workspace — flagged for awareness, out of scope here._
