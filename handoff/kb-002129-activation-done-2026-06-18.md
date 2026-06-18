# KB → quant · #138 002129 TCL中环 new_energy slice — PROMOTED + human-pinned (DONE)

**Date:** 2026-06-18 · **From:** KB (graph owner + human sign-pinner) · **To:** quant
**Re:** `handoff/quant-002129-activation-handoff-2026-06-17.md` (which KB had not yet processed — last KB
bus event was 2026-06-16; now acked).

KB processed the 2026-06-17 handoff. The ADR-0076 multi-sector unlock is realized: 002129 is now wired
into the live `new_energy` graph (it previously lived only in ai_compute via Samsung-HBM→002129).

## What KB did (§6.1–6.3)
All 5 edges created in scope `new_energy`, presence-only, `directional_weight 0.0`, `revenue_share null`:

| # | edge | type | state | sign |
|---|---|---|---|---|
| 1 | COMM:POLYSILICON → 002129 | raw_material | **review:approved** | **−1** (human-pinned, cited basis) |
| 2 | 002129 → 688599 天合 | supplier | review:approved | ± |
| 3 | 002129 → 688223 晶科 | supplier | review:approved | ± |
| 4 | PVDEMAND → 002129 | customer | review:approved | ± |
| 5 | POLICY:SUPPLY_SIDE_REFORM → 002129 | policy_driver | review:approved | ± |

- Edges 2/3/4 promoted (new_energy-internal); edges 1/5 inserted against the KB-served synthetic nodes
  (COMM:POLYSILICON / POLICY:SUPPLY_SIDE_REFORM) — both already existed in KB's new_energy graph.
- **Human pinned edge 1 = −1** per §4 (多晶硅价↑→硅片厂成本↑、毛利↓; consistent with the existing
  COMM:POLYSILICON→688223/688599/002459 siblings, all −1). The other 4 stay ± (presence-only) per §4.

## Firewall
The machine pinned **no** sign — KB created presence-only ±; the human pinned the lone −1 as a firewall act
(daemon `SIGN_BASIS_REQUIRED` rail satisfied — −1 carries a non-empty `sign_basis`). All 5 legs propagate at
`directional_weight 0.0` (`_R2_ELIGIBLE_SCOPES` empty) regardless of the pinned sign, per §5.

## Next (§6.4)
KB's served `new_energy` graph now contains the slice → the pin/slice hash has shifted (expected/benign).
Quant: verify 002129 fires under `new_energy` live (match≠propagate, 0.0 legs) per `test_multisector_node_fires_both_scopes`.
revenue_share + per-scope Phase-4 study remain separate/later (§6.5).
