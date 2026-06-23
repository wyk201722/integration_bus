# KB → Quant — semicon_equipment human-pinned chain edges READY for reconcile-vs-gold — 2026-06-23

**New sector handed off:** `semicon_equipment` (半导体设备 / 国产替代). This is the **last curated
sector without a quant artifact** — every other sector (ai_compute / optical_comms / ai_pcb /
liquid_cooling / ai_dc_power / new_energy / humanoid_robotics) already has a served or pinned drop.
Curation (approve + selective directional pin) is done; **revenue_share TODO #1 (mis-axis) is cleared**
(see below).

## Artifact
**`handoff/kb-chain-pinned-semicon_equipment-2026-06-23.json`** (`schema: kb-pinned-chain-edges@1`).
Dumped max-version-per-id (current view); one entry per `(source,target,edge_type)` triple.

| field | value |
|---|---|
| approved_total | 31 |
| rejected_total | 0 |
| directional_pinned (±1) | 9 (all `+1`) |
| presence_only (±) | 22 |
| with_revenue_share | 8 |
| **directional_without_sign_basis** | **0** (firewall gate clean) |
| by_edge_type | customer 18 · supplier 6 · policy_driver 4 · capex_driver 3 |

## The 9 directional pins (all `+1`)
| edge | type | rs |
|---|---|---|
| 半导体国产替代 → 中微公司 | policy_driver | — |
| 半导体国产替代 → 北方华创 | policy_driver | — |
| 晶圆厂capex → 拓荆科技 | capex_driver | 0.30 |
| 晶圆厂capex → 中微公司 | capex_driver | 0.30 |
| 晶圆厂capex → 北方华创 | capex_driver | 0.30 |
| 长电科技 → 长川科技 | customer | 0.05 |
| 中芯国际 → 北方华创 | customer | 0.05 |
| **长江存储 → 拓荆科技** | customer | **0.20** ← corrected |
| **长江存储 → 北方华创** | customer | **0.10** ← corrected |

## revenue_share axis fix (TODO #1 — CLEARED 2026-06-23)
3 edges had been curated on the **reverse axis** (target's share of the *source's* tender/procurement,
single-product). Re-derived to target-side (源占目标总营收) and re-pinned:
- 长江存储→拓荆科技 `0.55 → 0.20`, 长江存储→北方华创 `0.2 → 0.10`, 华虹公司→北方华创 `0.24 → 0.045` (±).
- **Disqualifier:** 北方华创 2025 max single-customer = **10.3%** (top-5 = 10.3/4.5/4.5/4.3/4.3% of
  393.53亿) → the old 0.24/0.2 exceeded the disclosed ceiling, impossible target-side.
- The 拓荆 value (0.20) is **`[AI·待核]` LOW-confidence** — A-share reports anonymize 客户一/二, so
  长江存储's exact share of 拓荆's revenue is undisclosed; 0.20 is a bounded estimate inside top-5=62.33%.
  Full rationale: `docs/verification/semicon-rs-axis-corrections-2026-06-23.md`.

## Firewall (verbatim)
- `transmission_sign ±1` set ONLY by KB human `approve()`; 22 edges left at `±` are deliberate
  presence-only (approved without a directional pin).
- capex_driver / policy_driver edges grounded against each TARGET maker's own financials (pure-play
  equipment makers → capex exposure is high, hence the 0.30s).
- **ADVISORY — quant does NOT re-pin.** The only sign-set path is KB's `approve()`.

## Ask
1. Reconcile the 9 `+1` pins vs gold (mirror #135 `ai_compute` pinned-reconcile). Flag over-determined
   `+1`s for demotion to `±`.
2. Sanity-check the corrected target-side rs (esp. 拓荆 0.20 — undisclosed, bounded estimate).
3. The 22 presence-only edges remain KB-side TODO (re-open → pin) — no quant action there yet.

Generators (KB): `scripts/dev/_dump-chain-approved.cjs semicon_equipment` (max-version-aware) → `build-pinned-handoff.mjs semicon_equipment 2026-06-23`.
