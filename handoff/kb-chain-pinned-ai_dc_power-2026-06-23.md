# KB → Quant — ai_dc_power human-pinned chain edges READY for reconcile-vs-gold — 2026-06-23

**New sector handed off:** `ai_dc_power` (AI 数据中心 电源/供电). This completes the AI-DC
physical stack already served — compute=`ai_compute` / interconnect=`optical_comms` /
board=`ai_pcb` / thermal=`liquid_cooling` / **power=THIS**. Scaffolded 2026-06-21; human
curation (approve + selective directional pin) pass is done.

## Artifact
**`handoff/kb-chain-pinned-ai_dc_power-2026-06-23.json`** (`schema: kb-pinned-chain-edges@1`).
Deduped to the canonical `review:approved` layer (the scaffold's redundant `review:pending`
copies are dropped — one entry per `(source,target,edge_type)` triple).

| field | value |
|---|---|
| approved_total | 28 (1 per triple) |
| rejected_total | 0 |
| directional_pinned (±1) | 4 (all `+1`) |
| presence_only (±) | 24 |
| with_revenue_share | 6 |
| **directional_without_sign_basis** | **0** (firewall gate clean) |
| by_edge_type | supplier 11 · customer 14 · capex_driver 3 |

## The 4 directional pins
Each `+1`, each carries a `sign_basis` (no `proposed_sign` populated). The bases are
`[AI·待核]`-prefixed (AI-sourced, eyeball-pending per the established marker) — **operator has
accepted them for this round.**

| edge | type | basis (abridged) |
|---|---|---|
| `UNLISTED:AI_DC_CAPEX → 科华数据 (002335.SZ)` | capex_driver | 互联网大厂收入占比~50%, 2026… |
| `UNLISTED:AI_DC_CAPEX → 中恒电气 (002364.SZ)` | capex_driver | 2024 数据中心电源营收 6.68亿, +111% |
| `GOOGL → 麦格米特 (002851.SZ)` | customer | 谷歌 DC 800VDC 架构电源直接供应商 |
| `NVDA → 麦格米特 (002851.SZ)` | customer | 英伟达指定 AI 服务器电源供应商 |

## Firewall (verbatim)
- `transmission_sign ±1` set ONLY by KB human `approve()`; scaffold/mining writes `±`. The 24
  approved edges left at `±` are deliberate presence-only — the human pinned a direction on
  only the 4 high-conviction ones.
- The 3 `capex_driver` edges were seeded `±` and are grounded with each **TARGET company's own
  AI 年报 financials** (NOT company-to-company), per `optical_comms`/`liquid_cooling`.
- **ADVISORY — quant does NOT re-pin.** The only sign-set path is KB's `approve()` panel.

## Ask
1. Reconcile the 4 directional `+1` pins vs gold (mirror #135 `ai_compute` pinned-reconcile).
   Flag any over-determined `+1` for demotion to `±` — watch the 2 `customer → 麦格米特` edges
   (a single PSU vendor double-counted across NVDA + GOOGL demand) and the 2 `capex_driver`
   edges (the supplier-edge `+1` over-determination rule).
2. The 24 presence-only edges + the `capex_driver` financial grounding remain KB-side TODO;
   no quant action there yet.

Generators (KB side): `scripts/dev/_dump-chain-approved.cjs` → `scripts/dev/build-pinned-handoff.mjs ai_dc_power 2026-06-23`.
