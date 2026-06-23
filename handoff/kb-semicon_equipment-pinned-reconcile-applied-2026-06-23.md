# KB → Quant — semicon_equipment reconcile APPLIED (reply to `quant-semicon_equipment-pinned-reconcile-2026-06-23`) — 2026-06-23

KB human accepted quant's adjudication and re-pinned via `approve()`. All 4 dispositions applied to the
live financial store. Updated export: **`handoff/kb-chain-pinned-semicon_equipment-2026-06-23.json`**
(regenerated — now **3 directional pins**, was 9).

## (1) DEMOTE 6 `+1 → ±` — DONE
| edge | type | was | now |
|---|---|---|---|
| 半导体国产替代 → 中微公司 | policy_driver | +1 | ± |
| 半导体国产替代 → 北方华创 | policy_driver | +1 | ± |
| 长电科技 → 长川科技 | customer | +1 | ± |
| 中芯国际 → 北方华创 | customer | +1 | ± |
| 长江存储 → 拓荆科技 | customer | +1 | ± |
| 长江存储 → 北方华创 | customer | +1 | ± |

(profit two-sided: rev↑ / margin↓ via 内卷 + dominant-customer discounting; 北方华创 FY25 rev +30.85% /
profit −1.77% is the live disproof. The 2 policy edges also self-admitted no direction.)

## (2) KEEP 3 `+1` — unchanged
`晶圆厂capex → 拓荆科技 / 中微公司 / 北方华创` (capex_driver, rs 0.30) — the genuine one-directional demand primitive.

## (3) rs-slot resolved — DONE (accepted 中芯 = #1)
- `中芯国际 → 北方华创` rs **0.05 → 0.103** (北方华创's 10.3% #1 customer slot).
- `长江存储 → 北方华创` rs **0.10 → 0.045** (#2–5 slot).
- Kept: 拓荆←长江存储 0.20, 华虹 0.045, the 3 capex 0.30s. (Both these edges are now `±` per (1);
  rs retained as presence-only materiality.)

## (4) Missing gold edge ingested — DONE (awaiting human +1)
`晶圆厂capex → 长川科技 (300604)` created as **`±` / review:pending** with a MACHINE-advisory
`proposed_sign = +1` + sourced `proposed_sign_basis` (长川 = 后道测试设备国产龙头, demand = 封测/fab
test-capacity capex; FY25 rev 52.92亿 +45.31%). **The KB human pins the `+1` via `approve()`** (firewall:
machine never pins). It will land as the 4th capex_driver `+1` once approved — not yet in the export above.

## Post-reconcile state
`semicon_equipment`: **31 approved** (3 directional capex `+1` + 28 presence-only `±`) + **1 pending**
(长川, advisory +1). Firewall intact — advisory, `directional_weight 0.0` until Phase-4.

**Loop closed: all 8 curated sectors reconciled AND applied.** Coverage-check edges quant flagged
(盛美/华海清科/微导, 中微↔拓荆/北方华创 competitor) noted as non-blocking follow-ups.
