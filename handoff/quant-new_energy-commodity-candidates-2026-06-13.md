# Chain-KG candidate edges — new_energy commodity pass-through (quant → KB)

- **From**: quant peer · **To**: KB peer (Phase 2-EXPAND, KB-led)
- **Date**: 2026-06-13 · **Instruction**: standby/optional candidate feed (`goal.md` Phase 2-EXPAND)
- **Status**: OPTIONAL candidate feed — quality-over-coverage. 39 verified `raw_material` edges, 9 new `commodity` nodes.

## Firewall framing (read first — non-negotiable)

- **Every edge carries `transmission_sign = ±` — NOT pinned.** Quant proposes *evidence and a conditional rationale*, never the polarity. The **human curator pins the sign** (the "backwards-sign-is-loss-making" rule). `proposed_sign_basis` is a PROPOSAL for that curation, not a decision.
- Ingest as `review:pending` `chain_edge` entries with `transmission_sign=±`. The daemon OQ-K6 guard still applies: a signed (`±1`) edge may not be served/approved without a `sign_basis` — which only the curator supplies when pinning.
- **new_energy is R2-eligible, but the validation firewall holds**: even after a human pins a sign, the edge is presence-only at weight 0.0 until the ADR-0073 §8 Phase-4 study passes for the scope. Nothing here can move advice.
- All targets are existing `graph-new_energy-v0.1.json` nodes (roster-verified); no nodes invented. Commodity node-id namespace = `COMM:<UPPER_SNAKE>` (OQ-Q4 frozen).

## Provenance

Produced by an adversarial-verify workflow (per-commodity research → independent skeptic → synthesis; 19 agents). The skeptic stage confirmed the load-bearing exclusions held — **no nickel/cobalt edge to 301358 湖南裕能 (LFP has neither)**, integrated-producer caveats (天赐 002709 makes its own LiPF6; 通威 600438 is poly-integrated) captured in each basis, and copper kept conservative (strength 0.18–0.38). 0 edges killed (research respected exclusions up front); strengths trimmed where noted. 0 pinned signs (must be 0).

## Commodity nodes (new — `node_type: commodity`)

| code | name | subindustry_tag |
|---|---|---|
| `COMM:LITHIUM_CARBONATE` | 碳酸锂 (Lithium Carbonate) | energy_metal_lithium |
| `COMM:POLYSILICON` | 多晶硅 (Polysilicon) | pv_silicon_feedstock |
| `COMM:NICKEL` | 镍 (Nickel) | base_metal_nickel |
| `COMM:COBALT` | 钴 (Cobalt) | energy_metal_cobalt |
| `COMM:LIPF6` | 六氟磷酸锂 (Lithium Hexafluorophosphate, 6F) | electrolyte_lithium_salt |
| `COMM:NEEDLE_COKE` | 针状焦/石油焦 (Needle / Petroleum Coke) | anode_carbon_precursor |
| `COMM:SODA_ASH` | 纯碱 (Soda Ash) | pv_glass_flux |
| `COMM:EVA_POE_RESIN` | EVA/POE 树脂 (EVA / POE Resin) | encapsulant_resin |
| `COMM:COPPER` | 铜 (Copper) | base_metal_copper |

## Candidate edges (`edge_type: raw_material`, `transmission_sign: ±`)

### COMM:LITHIUM_CARBONATE — 碳酸锂 (Lithium Carbonate)  (11 edges)

#### → `002466.SZ` 天齐锂业  · strength 0.95 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): +1 for the miner: lithium carbonate/hydroxide price IS essentially this company's selling price, so revenue and gross profit move directly with the commodity. There is no meaningful −1 case here — as a pure-play upstream lithium producer it benefits unambiguously from rising lithium prices and suffers from falling ones. The only nuance the curator should weigh is that a portion of value sits in its SQM/Greenbushes equity stakes, but those are also lithium-price-levered, so the sign is reinforced, not flipped.
- **materiality**: Pure-play lithium salt and concentrate producer (Greenbushes spodumene + Kwinana hydroxide). Lithium price is the dominant earnings driver; among the highest-beta A-share names to the lithium spot curve. Verified: graph node 002466 = subindustry lithium_salt, '锂盐/锂矿, 碳酸锂-price levered'.
- **evidence**: 天齐锂业 is one of the world's largest lithium producers, controlling a stake in the Greenbushes hard-rock mine (via Tianqi/IGO JV) and holding a large equity stake in Chile's SQM. Its revenue is overwhelmingly lithium concentrate and lithium chemicals, so its profitability tracks the lithium carbonate/hydroxide price cycle (it swung to large profits in the 2021-2022 price spike and saw earnings collapse as prices fell in 2023-2024). This is widely reported and not a fabricated figure. Roster-confirmed: graph-new_energy-v0.1.json node 002466.SZ subindustry_tag=lithium_salt.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002466.SZ); config/commodity-stock-map.yaml (lithium_carbonate, exposure 1.0)

#### → `002460.SZ` 赣锋锂业  · strength 0.93 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): +1 for the miner/converter: lithium salt price is the company's revenue, so earnings rise and fall with the commodity. No material −1 case — as an upstream lithium producer it is a long-the-commodity name. Curator nuance: 赣锋 is more vertically integrated downstream than 天齐 (it also makes batteries/cells), so a sliver of its business is actually short lithium-as-a-cost; but the lithium-salt segment dominates the P&L, so net exposure remains strongly +1.
- **materiality**: Integrated lithium producer: brine/spodumene resources plus lithium carbonate and hydroxide conversion. Lithium price is the primary earnings lever; high-beta to the spot curve, with a small downstream battery hedge. Verified: graph node 002460 = subindustry lithium_salt, '锂盐/锂矿 leader'.
- **evidence**: 赣锋锂业 is a leading global lithium compounds producer with upstream resource interests (e.g. Mariana/Cauchari brine projects in Argentina, Mt Marion spodumene offtake) and large lithium hydroxide/carbonate conversion capacity. Its core revenue is lithium chemicals, so profitability tracks the lithium price cycle, with reported earnings booming in the 2021-2022 spike and compressing as prices fell. It also has a smaller battery business, making it slightly less of a pure-play than 天齐. Roster-confirmed: graph node 002460.SZ subindustry_tag=lithium_salt.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002460.SZ); config/commodity-stock-map.yaml (lithium_carbonate, exposure 1.0)

#### → `301358.SZ` 湖南裕能  · strength 0.85 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): Genuinely two-sided. Lithium carbonate is by far the single largest input cost for LFP cathode. (a) When pricing power / cost-plus tolling contracts hold and inventory is matched, lithium moves are largely passed through to cell-maker customers, so margin is roughly neutral and the company can even book inventory GAINS on a fast rise — a transient +1. (b) When lithium prices FALL sharply (the 2023-2024 case), LFP cathode makers eat inventory write-downs and price down their output faster than cheap lithium reaches COGS — a painful −1. So the curator should pin direction by regime: rising-with-passthrough vs falling-with-destocking. Note: this is LFP, so NO nickel/cobalt exposure — lithium carbonate is the relevant commodity, not lithium hydroxide or sulfate.
- **materiality**: Largest LFP cathode (磷酸铁锂) maker in China. Lithium carbonate is the dominant bill-of-materials line for LFP cathode; revenue and reported margin are heavily distorted by lithium price swings and inventory timing. revenue_share nulled: lithium's COGS share for LFP cathode swings violently with the lithium price (>50% at the 2022 peak, far less after the 2023-2024 collapse), so a fixed figure overstates precision. Verified: graph node 301358 = subindustry cathode, '磷酸铁锂正极 leader'.
- **evidence**: 湖南裕能 is the leading LFP cathode active-material supplier (main customers 宁德时代 and 比亚迪). For LFP cathode, lithium carbonate is the largest single raw-material cost — industry commentary commonly cites lithium as well over half of LFP cathode material cost at high lithium prices, falling sharply after the 2023-2024 price collapse. LFP uses iron phosphate and lithium carbonate only — no nickel or cobalt. Roster-confirmed: graph node 301358.SZ subindustry_tag=cathode (磷酸铁锂正极 leader).
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 301358.SZ)

#### → `688005.SH` 容百科技  · strength 0.72 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): Two-sided cost exposure. Lithium (here largely lithium hydroxide/carbonate, plus nickel/cobalt for ternary) is a major COGS line for NCM cathode. (a) Under cost-plus/tolling pricing with matched inventory, lithium moves pass through → near-neutral to transient +1 (inventory gains on a rise). (b) On a sharp lithium decline, ternary cathode makers take inventory losses and margin compression → −1. Curator pins by regime and by how much of the contract book is true cost-pass-through tolling. Unlike the LFP name, 容百 ALSO carries nickel/cobalt exposure (see the separate NICKEL and COBALT edges for this same code), so lithium is one of several commodity drivers, not the sole one — slightly lower strength than the pure-LFP case.
- **materiality**: Leading ternary (NCM/high-nickel) cathode maker. Lithium hydroxide/carbonate is a major raw-material cost alongside nickel and cobalt; margins and inventory marks are sensitive to the lithium cycle but exposure is shared with Ni/Co. Verified: graph node 688005 = subindustry cathode, '三元正极 leader'. This code legitimately appears under three commodities (LITHIUM_CARBONATE / NICKEL / COBALT) — distinct edges, not duplicates.
- **evidence**: 容百科技 is China's leading high-nickel ternary cathode producer. Ternary cathode bill-of-materials is dominated by lithium (carbonate/hydroxide), nickel sulfate and cobalt sulfate; lithium is one of the top cost lines. Because the commodity basket is split across Li/Ni/Co, lithium is material but not the sole driver — no precise COGS share asserted because it varies with both metal prices and product mix (high-Ni vs mid-Ni). Roster-confirmed: graph node 688005.SH subindustry_tag=cathode.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688005.SH)

#### → `300073.SZ` 当升科技  · strength 0.7 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): Same two-sided structure as the other ternary cathode maker: lithium (hydroxide/carbonate) is a major COGS line shared with nickel/cobalt. (a) Cost-plus pass-through + matched inventory → neutral/transient +1 on a rise. (b) Sharp lithium decline → inventory write-downs and margin squeeze → −1. Curator pins by price regime and contract structure. Lithium is material but co-exists with Ni/Co exposure (and a nickel-free LFP segment), so it is not the single dominant commodity the way it is for an LFP-only cathode maker.
- **materiality**: Ternary (NCM) cathode maker with significant export/overseas customer base. Lithium hydroxide/carbonate is a major input cost alongside nickel and cobalt; sensitive to lithium cycle and inventory timing. Verified: graph node 300073 = subindustry cathode, '正极 (三元 + 磷酸铁锂)'. This code also appears under NICKEL and COBALT — distinct edges.
- **evidence**: 当升科技 is a major Chinese ternary cathode active-material supplier with a notable international customer mix. As with all NCM cathode producers, lithium compounds are among the largest raw-material costs together with nickel and cobalt salts. The exact lithium COGS share varies with metal prices and product mix, so no fixed percentage is asserted. Roster-confirmed: graph node 300073.SZ subindustry_tag=cathode (三元 + 磷酸铁锂).
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300073.SZ)

#### → `300750.SZ` 宁德时代  · strength 0.75 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): Two-sided, and the polarity hinges on contractual pass-through. Lithium (carbonate, via cathode) is the single largest material cost embedded in a battery cell. (a) CATL runs metal-price linked pricing clauses with many large customers (lithium-carbonate-indexed pricing, e.g. the 锂矿返利/metal-linkage mechanisms), so it can pass much of the lithium move through to OEMs → cost rises are largely neutralized, and falling lithium can even EXPAND unit margin if ASPs lag the input drop (transient +1 on a decline). (b) Where pass-through is incomplete or lithium spikes faster than repricing, margin compresses and inventory can be marked down → −1. So unusually for a downstream name, the curator may find that FALLING lithium is net positive for CATL margins — direction is genuinely regime- and contract-dependent, which is exactly why the sign must stay ±. (NB the graph's SIGN INVERSION REGISTRY pre-notes 碳酸锂↑ => −1 电芯; that is the naive cost leg, which the pass-through mechanism can override — leave ± for the curator.)
- **materiality**: World's largest battery cell/pack maker. Lithium (through cathode) is the largest single material cost in a cell, but strong metal-price-linked customer contracts mute and can even invert the naive cost sign. Hop is via cathode but exposure is direct and very material. Verified: graph node 300750 = subindustry battery_cell, 'margin COMPRESSES when 碳酸锂 spikes (cost)'. Also carries a COPPER edge (copper-foil) — distinct.
- **evidence**: 宁德时代 is the global leader in lithium-ion battery cells and packs. Cathode (where lithium carbonate sits) is the most expensive cell material, so lithium is CATL's largest indirect raw-material exposure. CATL is widely reported to use metal-price-linked pricing and rebate mechanisms with major customers, which transmit lithium-price moves to OEMs; this is why its battery gross margin held up and in some periods improved even as lithium prices fell sharply in 2023-2024. Mechanism asserted, not a precise COGS percentage. Roster-confirmed: graph node 300750.SZ subindustry_tag=battery_cell.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300750.SZ)

#### → `300014.SZ` 亿纬锂能  · strength 0.65 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): Two-sided cell-maker exposure: lithium (via cathode) is the largest material cost. (a) To the extent power/storage cell pricing is metal-linked or repriced quickly, lithium moves pass to customers → neutral to transient +1 on a decline (margin recovery as cheap lithium reaches COGS). (b) When lithium spikes faster than cell ASPs or pass-through is weak (it has less pricing power than CATL), margin compresses and inventory marks bite → −1. Curator pins by regime and by 亿纬's weaker contractual leverage vs the market leader.
- **materiality**: Major power and energy-storage cell maker. Lithium-through-cathode is the largest material cost; pass-through pricing power is real but weaker than the market leader, so margin sensitivity to the lithium cycle is somewhat higher. Verified: graph node 300014 = subindustry battery_cell. Also carries a COPPER edge — distinct.
- **evidence**: 亿纬锂能 is a top-tier Chinese battery cell producer across consumer, power and energy-storage segments. As with any lithium-ion cell maker, the cathode (lithium-bearing) is the dominant material cost, so the lithium price cycle and inventory timing materially affect cost and reported margin. It generally commands less customer pricing power than 宁德时代, so it absorbs more of the lithium swing. Mechanism asserted, no fabricated COGS figure. Roster-confirmed: graph node 300014.SZ subindustry_tag=battery_cell.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300014.SZ)

#### → `002074.SZ` 国轩高科  · strength 0.65 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): Two-sided, and especially lithium-carbonate-centric because 国轩 is LFP-heavy (LFP cells use lithium carbonate, not hydroxide, and have NO nickel/cobalt). (a) With pass-through/repricing, lithium moves transmit to customers → neutral/transient +1 on a falling-lithium regime as cheaper carbonate reaches COGS. (b) On a sharp rise with incomplete pass-through, margin compresses → −1; on a sharp fall it can take inventory losses on high-cost lithium and cathode stock. Curator pins by regime; note the LFP mix makes lithium carbonate the cleanest single commodity driver for this name.
- **materiality**: LFP-focused power and storage cell maker. Lithium carbonate (through LFP cathode) is the dominant material cost; no nickel/cobalt exposure. Margin and inventory marks track the lithium-carbonate cycle. Verified: graph node 002074 = subindustry battery_cell, '电芯 (磷酸铁锂-heavy)'. Also carries a COPPER edge — distinct.
- **evidence**: 国轩高科 is a major Chinese battery maker with a strong LFP product weighting (power and increasingly energy storage). LFP cells embed lithium carbonate via the cathode as the largest material cost and carry no nickel or cobalt, so lithium carbonate is the cleanest commodity driver of its unit economics. Mechanism asserted; COGS share left null because it swings with the lithium price. Roster-confirmed: graph node 002074.SZ subindustry_tag=battery_cell (磷酸铁锂-heavy).
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002074.SZ)

#### → `688063.SH` 派能科技  · strength 0.55 · revenue_share None · hop 1 · confidence medium
- **proposed_sign_basis** (for curator; NOT a pin): Two-sided storage-cell exposure, LFP-based (lithium carbonate, no Ni/Co). (a) Falling lithium lowers cell BOM cost and, if system ASPs lag, can support margin → transient +1; pass-through to its residential/commercial storage customers neutralizes part of the move. (b) Rising lithium or being caught long high-cost inventory during the 2023-2024 destock → −1 (派能 was notably hit by inventory/overstock dynamics in the storage channel). Curator pins by regime; somewhat lower strength because 派能 sells integrated storage SYSTEMS, so the cell/lithium cost is one layer beneath system-level and channel-inventory dynamics.
- **materiality**: Residential/C&I energy-storage cell and system maker, LFP chemistry. Lithium carbonate (via LFP cathode) is a major cell cost; exposure is real but diluted by system-level integration and storage-channel inventory cycles. Verified: graph node 688063 = subindustry energy_storage_cell, '户储 pure-play'. Also carries a COPPER edge — distinct.
- **evidence**: 派能科技 is a leading independent residential energy-storage battery/system supplier using LFP chemistry. Its cells embed lithium carbonate via the LFP cathode as a major cost. Because it sells integrated storage systems and was exposed to the 2023-2024 storage-channel inventory glut, the lithium commodity effect is mediated by system pricing and destocking. Mechanism asserted; no fabricated figures. Roster-confirmed: graph node 688063.SH subindustry_tag=energy_storage_cell.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688063.SH)

#### → `002407.SZ` 多氟多  · strength 0.55 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): Two-sided. Lithium carbonate is a direct feedstock for lithium hexafluorophosphate (LiPF6, 六氟磷酸锂) — the lithium atom in LiPF6 comes from lithium carbonate. (a) When LiPF6 pricing tracks lithium feedstock and demand is firm, cost rises pass through → neutral/+1, and 多氟多 can book gains on a lithium/LiPF6 price spike (it earned outsized profits during the 2021-2022 LiPF6 boom). (b) When lithium and LiPF6 prices collapse with overcapacity (2023-2024), it suffers both lower ASPs and inventory losses → −1. Curator pins by LiPF6 price regime; lithium carbonate is a real but partial input (fluorine chemistry/HF and phosphorus also matter), and the dominant earnings swing is the LiPF6 SPREAD rather than lithium-carbonate cost in isolation, so it is material but not the sole driver. NB this is the lithium-FEEDSTOCK-cost view of 多氟多; the separate LIPF6 edge for the same code is the producer-REVENUE view — both are kept deliberately.
- **materiality**: Major LiPF6 (六氟磷酸锂) producer. Lithium carbonate is a direct chemical feedstock for LiPF6; profitability tracks the LiPF6 cycle, which is itself partly driven by lithium-carbonate cost. Exposure shared with fluorine/HF chemistry; the LiPF6 spread, not lithium cost alone, is the primary lever. Verified: graph node 002407 = subindustry lithium_hexafluorophosphate (6F), SW2 化学制品 801034.SW.
- **evidence**: 多氟多 is one of China's largest producers of lithium hexafluorophosphate (LiPF6), the key lithium salt in electrolyte. LiPF6 synthesis consumes lithium carbonate (along with HF/fluorine chemistry), so lithium-carbonate cost feeds directly into its product cost, while its selling price is the LiPF6 price. It posted very large profits during the 2021-2022 LiPF6 price spike and then saw earnings fall sharply as LiPF6 prices collapsed on overcapacity. Mechanism well established; no precise COGS share asserted. Roster-confirmed: graph node 002407.SZ subindustry_tag=lithium_hexafluorophosphate.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002407.SZ)

#### → `002709.SZ` 天赐材料  · strength 0.4 · revenue_share None · hop 1 · confidence medium
- **proposed_sign_basis** (for curator; NOT a pin): Two-sided, mediated by its integrated LiPF6 position and weaker on a lithium-carbonate-SPECIFIC basis than the other names. 天赐 makes its own LiPF6, which consumes lithium carbonate; lithium-carbonate cost therefore flows into its electrolyte COGS, but two hops removed (lithium → LiPF6 → electrolyte) and LiPF6 is only a slice of electrolyte cost while lithium carbonate is only a slice of LiPF6 cost. (a) During the LiPF6 shortage/price boom its self-supply was a huge margin tailwind → +1; cost rises in lithium were more than offset by LiPF6 ASP. (b) When LiPF6/electrolyte prices collapsed (2023-2024) its self-made-LiPF6 advantage compressed and it carried high-cost lithium/LiPF6 inventory → −1. Curator pins by the electrolyte/LiPF6 price regime; the dominant swing factor is the electrolyte/LiPF6 spread, NOT lithium carbonate alone — strength trimmed accordingly. NB distinct from the LIPF6 edge for the same code, which captures the integrated-producer 6F view.
- **materiality**: Integrated electrolyte leader that self-produces LiPF6. Lithium carbonate is a feedstock for its in-house LiPF6, so it has real but indirect (two-hop) lithium exposure that is the smallest and most diluted in this set; the dominant swing factor is the electrolyte/LiPF6 spread rather than lithium-carbonate cost. Strength downgraded from 0.5 to 0.4 to reflect that lithium-carbonate-specific materiality is modest. Verified: graph node 002709 = subindustry electrolyte, 'integrated into 6F'. Same code also appears under LIPF6 — distinct edges.
- **evidence**: 天赐材料 is China's largest electrolyte maker and is vertically integrated into LiPF6 (it produces its own lithium salt), which was a major competitive advantage during the 2021-2022 LiPF6 shortage. Because LiPF6 is made from lithium carbonate, lithium-carbonate cost feeds its electrolyte COGS; however LiPF6 is only part of electrolyte cost and lithium carbonate only part of LiPF6 cost (HF/fluorine chemistry dominates), so earnings are driven far more by the electrolyte/LiPF6 spread than by lithium carbonate in isolation. Mechanism established; no fabricated figure. Roster-confirmed: graph node 002709.SZ subindustry_tag=electrolyte.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002709.SZ)

### COMM:COPPER — 铜 (Copper)  (9 edges)

#### → `300750.SZ` 宁德时代  · strength 0.35 · revenue_share 0.08 · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): For the cell maker, copper is a COST input via copper foil (anode current collector), so the conditional polarity is −1 on margin when copper rises absent pass-through; copper foil is ~8-10% of cell cost, a modest single-digit COGS line. Copper-foil converters (嘉元/诺德) price on a processing-fee + LME-copper pass-through basis, so the cell maker effectively bears most of the copper move; pass-through to OEM/auto customers is partial and lagged, so a sustained copper spike compresses margin in the gap before contracts reset, and the sign flips toward neutral once they reprice. Curator to pin direction.
- **materiality**: Modest: copper foil ~8-10% of cell COGS — a minority cost line dwarfed by cathode/lithium. Largest cell maker so absolute copper tonnage is huge, but as a % of its diversified COGS it remains single-to-low-double digit. Strength trimmed from 0.4 to 0.35 so a sub-10% COGS input is not overweighted relative to the lithium/cathode story. Same code also carries the flagship LITHIUM_CARBONATE edge — distinct, complementary cost lines.
- **evidence**: Copper foil serves as the anode current collector in Li-ion cells and is widely cited at ~10-13% of cell mass and ~8-10% of cell cost (industry references on lithium-battery copper foil). 嘉元科技 and 诺德股份 are well-known copper-foil suppliers into CATL, and copper-foil contracts are typically processing-fee + copper pass-through. Exact % varies by chemistry/format and copper price; the 8-10% is an honest industry range, not a firm figure. Roster-confirmed: graph node 300750.SH subindustry_tag=battery_cell.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300750.SZ)

#### → `300014.SZ` 亿纬锂能  · strength 0.38 · revenue_share 0.08 · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): Same channel as CATL: copper foil is the anode current collector, a COST input → −1 on margin when copper rises absent full pass-through; copper foil ~8-10% of cell cost. Converters price processing-fee + copper pass-through, so the cell maker bears the copper move; pass-through to customers is partial/lagged and the sign neutralizes once contracts reprice. Curator pins direction.
- **materiality**: Modest single-digit COGS fraction via copper foil. Consumer + power + storage cell mix; copper foil exposure applies across all Li-ion formats. Minority cost line relative to lithium/cathode. Same code also carries the LITHIUM_CARBONATE edge — distinct.
- **evidence**: 亿纬锂能 is a major Li-ion cell maker (power, consumer, storage); all its Li-ion cells use copper foil as the anode current collector, the ~8-10%-of-cost industry range. Honest range, not a firm per-company figure. Roster-confirmed: graph node 300014.SZ subindustry_tag=battery_cell.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300014.SZ)

#### → `002074.SZ` 国轩高科  · strength 0.38 · revenue_share 0.08 · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): Copper foil as anode current collector is a COST input → −1 on margin when copper rises absent pass-through; ~8-10% of cell cost. 国轩 is LFP-heavy; copper-foil intensity is largely chemistry-independent (the collector is copper regardless of cathode chemistry), so exposure is similar to peers. Partial/lagged pass-through to auto/storage customers neutralizes the sign over a contract cycle. Curator pins direction.
- **materiality**: Modest. LFP focus does NOT reduce copper-foil exposure (the anode collector is copper regardless of cathode chemistry — correctly avoids a chemistry type-error). Minority cost line vs LFP cathode + lithium carbonate. Same code also carries the LITHIUM_CARBONATE edge — distinct.
- **evidence**: 国轩高科 is a major (LFP-leaning) cell maker; copper foil is the universal anode current collector in Li-ion cells at the ~8-10%-of-cost industry range. Range is honest, not a firm figure. Roster-confirmed: graph node 002074.SZ subindustry_tag=battery_cell.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002074.SZ)

#### → `688063.SH` 派能科技  · strength 0.32 · revenue_share 0.07 · hop 1 · confidence medium
- **proposed_sign_basis** (for curator; NOT a pin): 派能 makes its own storage Li-ion cells, which use copper foil as the anode current collector → COST input, −1 on margin when copper rises absent pass-through; ~8-10% of cell cost. As a system integrator too, copper also enters via internal wiring/busbars, marginally. Pass-through to residential-storage customers is slow (channel-priced), so margin sensitivity exists in the gap. Curator pins direction.
- **materiality**: Modest and slightly lower-confidence than the three big cell makers: 派能 is a storage-cell + system maker, so copper foil applies to its in-house cells but a portion of revenue is system-level where copper is a smaller fraction. Minority cost line. Same code also carries the LITHIUM_CARBONATE edge — distinct.
- **evidence**: 派能科技 manufactures lithium iron phosphate storage cells in-house; like all Li-ion cells these use copper foil anode current collectors (~8-10% of cell cost industry range). Honest range. Lower strength reflects its mixed cell/system business vs pure cell makers. Roster-confirmed: graph node 688063.SH subindustry_tag=energy_storage_cell.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688063.SH)

#### → `300274.SZ` 阳光电源  · strength 0.3 · revenue_share None · hop 1 · confidence medium
- **proposed_sign_basis** (for curator; NOT a pin): Copper enters inverters via magnetics windings (transformers/inductors/chokes), DC/AC busbars and internal wiring → COST input, so −1 on margin when copper rises absent pass-through. Copper is a real but modest BOM line (semiconductors/IGBT, magnetic cores, capacitors dominate). 阳光 spans string + central + storage PCS, the larger units carry more copper magnetics/busbar. Pass-through via project pricing is partial; sign neutralizes on order repricing. Curator pins direction.
- **materiality**: Modest. Copper is a minority of inverter BOM (power semis + magnetic cores + capacitors larger). Central/large inverters and storage PCS carry more copper (busbars, transformer windings) than string units, slightly raising 阳光's exposure within the modest band. No reliable public single % — left null (correct discipline, not fabricated). Verified: graph node 300274 = subindustry inverter, '逆变器 + 储能PCS + 电站EPC'.
- **evidence**: Solar inverters use copper extensively in inductor/transformer windings and busbars (copper chosen for low resistivity/cost); busbar conductors are near-universally copper. 阳光电源 is the largest A-share inverter/PCS maker. No trustworthy public copper-COGS % exists per company, so revenue_share is null rather than fabricated. Roster-confirmed: graph node 300274.SZ subindustry_tag=inverter.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300274.SZ)

#### → `300763.SZ` 锦浪科技  · strength 0.27 · revenue_share None · hop 1 · confidence medium
- **proposed_sign_basis** (for curator; NOT a pin): String-inverter maker: copper in inductor/transformer windings, chokes and internal busbars/wiring → COST input, −1 on margin when copper rises absent pass-through. Modest BOM share (power semis + magnetic cores dominate). Distributor/project pricing gives partial, lagged pass-through; sign neutralizes on repricing. Curator pins direction.
- **materiality**: Modest, slightly below 阳光: 锦浪 is string/residential + some storage, so per-unit copper magnetics smaller than central inverters. Minority BOM line. No reliable public % — null. Verified: graph node 300763 = subindustry inverter, '组串逆变器 pure-play'.
- **evidence**: String solar inverters contain copper-wound inductors/transformers and copper busbars (copper standard for conductors due to conductivity/cost). 锦浪科技 is a leading string-inverter exporter. No credible public copper-COGS % per company; revenue_share left null. Roster-confirmed: graph node 300763.SZ subindustry_tag=inverter.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300763.SZ)

#### → `688390.SH` 固德威  · strength 0.27 · revenue_share None · hop 1 · confidence medium
- **proposed_sign_basis** (for curator; NOT a pin): String + hybrid/storage inverter maker: copper in winding magnetics, chokes, busbars and wiring → COST input, −1 on margin when copper rises absent pass-through. Hybrid/storage units add a bit more copper magnetics. Modest BOM share; partial lagged pass-through neutralizes sign over repricing. Curator pins direction.
- **materiality**: Modest. Hybrid/storage inverter mix gives slightly more copper-wound magnetics than pure string, but still a minority BOM line behind power semis and magnetic cores. No reliable public % — null. Verified: graph node 688390 = subindustry inverter, '逆变器/储能逆变器'.
- **evidence**: 固德威 makes string and hybrid/storage inverters, which use copper-wound inductors/transformers and copper busbars (copper standard for conductors). No credible public copper-COGS % per company; revenue_share null rather than fabricated. Roster-confirmed: graph node 688390.SH subindustry_tag=inverter.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688390.SH)

#### → `605117.SH` 德业股份  · strength 0.3 · revenue_share None · hop 1 · confidence medium
- **proposed_sign_basis** (for curator; NOT a pin): Storage/hybrid + string inverter maker: copper in transformer/inductor windings, chokes, busbars and wiring → COST input, −1 on margin when copper rises absent pass-through. Storage/hybrid inverters carry meaningful copper magnetics. Modest BOM share; partial lagged pass-through neutralizes sign on repricing. Note 德业 also has a non-inverter (dehumidifier/heat-exchanger) segment with its own copper-tube exposure, reinforcing aggregate copper sensitivity. Curator pins direction.
- **materiality**: Modest, comparable to 阳光 within the band: storage/hybrid inverter copper magnetics PLUS a heat-exchange/appliance segment that uses copper tubing, so aggregate copper exposure is a touch broader than pure-inverter peers. Still a minority of total COGS. No reliable public % — null. Verified: graph node 605117 = subindustry inverter, '储能逆变器 + 微逆; HEAVILY EXPORT-levered'.
- **evidence**: 德业股份 is a leading storage/hybrid inverter maker (and also makes heat-exchangers/dehumidifiers using copper tube). Storage inverters use copper-wound magnetics and busbars. No credible public copper-COGS % per company; revenue_share null. Roster-confirmed: graph node 605117.SH subindustry_tag=inverter.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 605117.SH)

#### → `688032.SH` 禾迈股份  · strength 0.18 · revenue_share None · hop 1 · confidence medium
- **proposed_sign_basis** (for curator; NOT a pin): Microinverter maker: isolated topologies use small copper-wound transformers/inductors → COST input, −1 on margin when copper rises absent pass-through. Per-unit copper is small; microinverter BOM is dominated by control ICs, power semis and PCB. Minor share; partial lagged pass-through neutralizes sign. Curator pins direction.
- **materiality**: Minor — lowest of the inverter set and sits at the materiality floor: microinverters use small copper magnetics but are semiconductor/IC-heavy, so copper is a small BOM fraction. Kept because the channel is genuinely real and the strength is honestly de-rated to minor rather than overstated. No reliable public % — null. Verified: graph node 688032 = subindustry microinverter, '微逆 (microinverter) leader'.
- **evidence**: Microinverters use isolated transformer topologies (e.g. flyback) with copper windings, but the dominant cost is semiconductors/control electronics. 禾迈股份 is a leading microinverter maker. Copper exposure is genuinely minor; revenue_share null, low strength reflects honest low materiality. Roster-confirmed: graph node 688032.SH subindustry_tag=microinverter.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688032.SH)

### COMM:POLYSILICON — 多晶硅 (Polysilicon)  (8 edges)

#### → `688303.SH` 大全能源  · strength 0.95 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): PROPOSED +1 (producer-revenue): polysilicon price IS Daquan's selling price — it is a near-pure-play poly producer, so poly price moves are revenue moves and (given a large fixed/cash-cost base) flow even more strongly to margin/profit. No offsetting downstream-cost leg. Curator should pin +1.
- **materiality**: Pure-play polysilicon producer; poly is effectively ~100% of revenue. Highest-purity exposure on the roster. Profit is highly geared to poly price given the fixed/cash-cost base, so price→earnings sensitivity is amplified vs revenue alone. Verified: graph node 688303 = subindustry polysilicon, '硅料 pure-play'.
- **evidence**: Daquan Energy (大全能源) is one of China's largest dedicated polysilicon producers and is essentially a single-product company; sales are overwhelmingly polysilicon. Pure-play status is uncontested. No exact revenue-share cited to avoid fabricated precision. Roster-confirmed: graph node 688303.SH subindustry_tag=polysilicon.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688303.SH)

#### → `600438.SH` 通威股份  · strength 0.85 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): PROPOSED net +1 but INTEGRATED/AMBIGUOUS — curator must weigh: (a) +1 producer-revenue leg dominates — Tongwei is the world's largest polysilicon producer and poly is a major revenue/profit line; rising poly price lifts the poly segment. (b) −1 partial internal-cost offset — its large captive solar-cell capacity (TW Solar) CONSUMES poly, so a higher poly price raises its own cell-segment input cost, partially hedging the gain. Net exposure historically positive because merchant-poly economics swamp the captive-cell drag, but integration mutes sensitivity vs a pure-play. Curator likely pins +1 with reduced magnitude.
- **materiality**: World's largest polysilicon producer AND a top solar-cell maker (integrated); also has a 饲料 segment. Poly is a dominant earnings driver; the captive cell business is a partial internal hedge — net long poly price but less geared than a pure-play. The integration is the key nuance to encode. Verified: graph node 600438 = subindustry polysilicon, 'DIVERSIFIED (硅料 + 电池 + 饲料)'.
- **evidence**: Tongwei (通威) is consistently ranked the largest global polysilicon producer by capacity and is simultaneously a leading solar-cell manufacturer (TW Solar / 通威太阳能). The dual role is why its poly-price sensitivity is net positive but partly self-hedged. Roster-confirmed: graph node 600438.SH subindustry_tag=polysilicon (diversified).
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 600438.SH)

#### → `601012.SH` 隆基绿能  · strength 0.8 · revenue_share 0.35 · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): PROPOSED −1 (downstream-cost, absent full pass-through): LONGi is a wafer+module maker that consumes polysilicon as its primary feedstock. Higher poly price raises wafer/module COGS; if ASPs do not pass through fully (the usual case in a competitive, oversupplied module market), margin compresses → −1. Conditional +1 only where LONGi holds low-cost poly inventory/contracts into a rising-price environment and can widen spread, but the durable sign is −1. Curator pins −1. (NB the graph node flags 隆基 sits on BOTH sides of the 硅料-price inversion via its own 硅片 margin — a second-order nuance the curator may weigh.)
- **materiality**: Polysilicon is the dominant non-glass raw-material cost in the wafer/module stack. Silicon's share of module cost is highly cyclical — roughly 30-50%+ at the wafer/cell stage depending on the poly-price cycle (peaked in the 2021-22 shortage, collapsed 2023-24). revenue_share is an order-of-magnitude COGS fraction, not a precise figure. Verified: graph node 601012 = subindustry pv_module, '硅片+组件 integrated'.
- **evidence**: LONGi (隆基绿能) is the world's largest monocrystalline wafer maker and a top module producer; polysilicon is the feedstock for its wafers. Silicon material being the single largest non-glass input cost in the wafer→module chain is uncontested. COGS share given as a range to avoid a fabricated point estimate. Roster-confirmed: graph node 601012.SH subindustry_tag=pv_module.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 601012.SH)

#### → `002459.SZ` 晶澳科技  · strength 0.78 · revenue_share 0.35 · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): PROPOSED −1 (downstream-cost, absent full pass-through): JA Solar is a vertically-integrated module maker for whom polysilicon (directly and via wafers) is the dominant non-glass COGS. Rising poly price raises module cost; without full ASP pass-through margin compresses → −1. Conditional +1 only on favorable poly-inventory timing in a rising market. Durable sign −1; curator pins −1.
- **materiality**: Integrated module maker; poly is the dominant non-glass module COGS. Same cyclical 30-50%+ silicon-cost band as the rest of the module group. revenue_share is an order-of-magnitude estimate. Verified: graph node 002459 = subindustry pv_module, '组件 leader'.
- **evidence**: JA Solar (晶澳科技) is a top-tier integrated PV module manufacturer (wafer/cell/module); polysilicon is the foundational feedstock. Module-maker poly cost exposure is well-established industry structure. Roster-confirmed: graph node 002459.SZ subindustry_tag=pv_module.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002459.SZ)

#### → `688599.SH` 天合光能  · strength 0.78 · revenue_share 0.35 · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): PROPOSED −1 (downstream-cost, absent full pass-through): Trina Solar is a module maker consuming polysilicon (directly and embedded in wafers/cells). Higher poly price raises COGS; absent full ASP pass-through, margin compresses → −1. Conditional +1 only on favorable inventory/contract timing. Durable sign −1; curator pins −1.
- **materiality**: Top-tier integrated module maker; poly is the dominant non-glass module COGS, same cyclical 30-50%+ band. revenue_share is an order-of-magnitude estimate. Verified: graph node 688599 = subindustry pv_module, '组件 leader (科创板 ±20%)'.
- **evidence**: Trina Solar (天合光能) is a leading global PV module manufacturer; polysilicon is its core feedstock via the wafer/cell stack. Standard, well-established module-chain cost exposure. Roster-confirmed: graph node 688599.SH subindustry_tag=pv_module.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688599.SH)

#### → `688223.SH` 晶科能源  · strength 0.78 · revenue_share 0.35 · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): PROPOSED −1 (downstream-cost, absent full pass-through): JinkoSolar is a module maker consuming polysilicon. Higher poly price raises module COGS; without full ASP pass-through margin compresses → −1. Conditional +1 only on favorable poly-inventory timing in a rising market. Durable sign −1; curator pins −1.
- **materiality**: Top-tier integrated module maker; poly is the dominant non-glass module COGS, same cyclical 30-50%+ band. revenue_share is an order-of-magnitude estimate. Verified: graph node 688223 = subindustry pv_module, '组件 leader (科创板 ±20%)'.
- **evidence**: JinkoSolar (晶科能源) is a leading global PV module manufacturer with vertically-integrated wafer/cell/module operations; polysilicon is the foundational feedstock. Well-established industry structure. Roster-confirmed: graph node 688223.SH subindustry_tag=pv_module.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688223.SH)

#### → `002865.SZ` 钧达股份  · strength 0.55 · revenue_share None · hop 1 · confidence medium
- **proposed_sign_basis** (for curator; NOT a pin): PROPOSED −1 (downstream-cost, absent full pass-through), ONE STEP REMOVED: Jinko Junda is a dedicated solar-cell maker — it buys WAFERS (which already embed polysilicon) rather than poly directly, so the exposure is one transformation step removed but still material (silicon cost dominates the wafer it purchases). Higher poly price raises wafer cost → raises cell COGS; absent pass-through to cell ASP, margin compresses → −1. Weaker/less direct than a poly buyer. Curator pins −1 with reduced magnitude. NOTE: exposure is genuinely wafer-mediated (effectively hop ~1.5); treat the hop_class=1 tag as a directness flag, not a literal direct-purchase claim.
- **materiality**: Pure-play solar-CELL maker (does not make poly). Poly exposure is transmitted via the price of purchased wafers, where silicon is the dominant cost — real and material but one step removed and buffered by the cell processing margin. Strength trimmed 0.62→0.55 to reflect the indirection (wafer-mediated, plus partial cost pass-through in wafer contracts). revenue_share left null — poly is not a directly-purchased line item for a cell maker. Verified: graph node 002865 = subindustry solar_cell, 'TOPCon 电池片 pure-play'.
- **evidence**: Junda (钧达股份) is a specialist solar-cell manufacturer that purchases silicon wafers as its main input; polysilicon is the dominant cost embedded in those wafers. Cell-maker poly exposure being wafer-mediated is standard PV-chain structure. Roster-confirmed: graph node 002865.SZ subindustry_tag=solar_cell.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002865.SZ)

#### → `600732.SH` 爱旭股份  · strength 0.55 · revenue_share None · hop 1 · confidence medium
- **proposed_sign_basis** (for curator; NOT a pin): PROPOSED −1 (downstream-cost, absent full pass-through), ONE STEP REMOVED: Aiko is a dedicated solar-cell maker (incl. ABC/back-contact cells) that buys WAFERS embedding polysilicon rather than poly directly. Higher poly price raises wafer cost → raises cell COGS; without pass-through to cell ASP, margin compresses → −1. Exposure is one transformation step removed and buffered by cell margin. Curator pins −1 with reduced magnitude. NOTE: genuinely wafer-mediated (effectively hop ~1.5); hop_class=1 is a directness flag, not a direct-purchase claim.
- **materiality**: Pure-play solar-CELL maker (does not make poly). Poly exposure transmitted via purchased-wafer prices, where silicon is the dominant cost — real and material but indirect and buffered by the cell processing margin. Strength trimmed 0.62→0.55 to reflect the wafer-mediation and partial pass-through. revenue_share left null — poly is not a directly-purchased line item for a cell maker. Verified: graph node 600732 = subindustry solar_cell, '电池片 — BC (ABC/xBC) franchise'.
- **evidence**: Aiko Solar (爱旭股份) is a specialist solar-cell manufacturer purchasing silicon wafers as its primary input; polysilicon is the dominant embedded cost in those wafers. Standard wafer-mediated cell-maker exposure. Roster-confirmed: graph node 600732.SH subindustry_tag=solar_cell.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 600732.SH)

### COMM:LIPF6 — 六氟磷酸锂 (Lithium Hexafluorophosphate, 6F)  (3 edges)

#### → `002407.SZ` 多氟多  · strength 0.7 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): PRODUCER-REVENUE leg. Propose +1 for 多氟多: LiPF6 (六氟磷酸锂, 6F) is one of its flagship products, so the 6F market price IS its selling price / revenue line — a 6F price spike lifts revenue and margin (and the 2021-22 6F super-cycle drove its earnings; the post-2022 collapse compressed them). This is the cleanest producer-side +1 in the LiPF6 chain. NOTE the curator should weigh that 多氟多 is DIVERSIFIED (also 电子级氢氟酸/电子化学品, 锂电池, 新材料), so 6F is a material but not whole-name driver — a +1 on the 6F line is real yet partial. The human curator pins the sign; this is a proposal, not a pin.
- **materiality**: 002407 多氟多 is a (the) leading domestic LiPF6 producer; 6F is a flagship revenue line, NOT a cost. Producer-side exposure: 6F price = its ASP. Diversified across 氟化工/电子化学品/锂电, so 6F is material-but-partial to the consolidated name. SW2 classified 化学制品 801034.SW (氟化工), not 电池 (confirmed in graph node 002407). revenue_share=null — no segment % cited (avoid fabrication); honestly a meaningful minority-to-substantial fraction depending on 6F price regime. VERIFIED: no type error — this is correctly the producer-revenue leg, not a cost leg; complementary to the LITHIUM_CARBONATE feedstock-cost edge for the same code.
- **evidence**: Well-known A-share supply-chain fact: 多氟多 (002407) is one of China's largest lithium hexafluorophosphate (六氟磷酸锂 / 6F) producers; LiPF6 is a named product line and its earnings were highly geared to the 2021-2022 6F price super-cycle (6F spot rose from ~10万元/吨 to a 2022 peak well above 50万元/吨, then collapsed below ~10万元/吨 by 2023-24). Exact segment revenue % not cited here to avoid fabricating a figure. Roster-confirmed: graph node 002407.SZ subindustry_tag=lithium_hexafluorophosphate.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002407.SZ)

#### → `002709.SZ` 天赐材料  · strength 0.55 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): INTEGRATED-PRODUCER leg — basis differs MATERIALLY from a pure electrolyte buyer (this is the chain's key distinction). 天赐 is the electrolyte leader but is BACK-INTEGRATED into 6F (large captive solid + liquid LiPF6 capacity), so the LiPF6 market price is largely an INTERNAL TRANSFER, not a pure external cost. Propose treating this NOT as a clean cost-side −1: when 6F price rises, 天赐 captures producer-side margin on its self-supplied 6F that offsets the higher electrolyte input cost (a natural hedge / vertical-integration moat). So the net sign is ambiguous and closer to producer-like-than-cost-taker — leaning mildly + or roughly neutral on a 6F spike, the OPPOSITE of a pure buyer's −1. The curator should explicitly pin this differently from 新宙邦's cost-taker −1; that contrast is the whole point of carrying both edges. Sign stays ± pending curator pin.
- **materiality**: 002709 天赐材料 is the 电解液 leader AND integrated into 6F (liquid LiPF6 self-supply). LiPF6 is the dominant cost component of electrolyte, BUT because 天赐 makes its own, the external-price exposure is materially BLUNTED vs a buyer — vertical integration converts most of the 6F cost line into an internal transfer + producer margin. Basis is hedged / producer-leaning, NOT cost-taker −1. This is exactly why it must be encoded distinctly from 新宙邦. revenue_share=null (electrolyte BOM share known qualitatively, captive offset not cited as a hard %). VERIFIED against graph node 002709 which states '电解液 leader, integrated into 6F (六氟磷酸锂) — partial overlap with 多氟多.' Same code also appears under LITHIUM_CARBONATE (feedstock-cost two-hop view) — distinct edges.
- **evidence**: Well-known A-share supply-chain fact: 天赐材料 (002709) is the domestic electrolyte market leader and is notably vertically integrated into lithium hexafluorophosphate — it pioneered large-scale LIQUID LiPF6 self-supply, giving it among the highest 6F self-sufficiency in the industry. The existing graph node note already flags '电解液 leader, integrated into 6F (六氟磷酸锂) — partial overlap with 多氟多.' This integration is the textbook reason its 6F exposure is structurally different from a pure electrolyte buyer.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002709.SZ)

#### → `300037.SZ` 新宙邦  · strength 0.55 · revenue_share 0.5 · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): COST-TAKER leg — the clean downstream-cost case. Propose −1 for 新宙邦 ABSENT FULL PASS-THROUGH: it is an electrolyte maker that primarily BUYS LiPF6 (lower 6F self-supply than the integrated 天赐), so 6F is a genuine external raw-material cost. LiPF6 is the single largest cost component of electrolyte (commonly cited at roughly ~40-60% of electrolyte material cost, varying strongly with the 6F price regime — higher share when 6F spikes), so a 6F price spike compresses electrolyte gross margin to the extent it cannot be passed to battery-cell customers; a 6F price fall RELIEVES cost (margin tailwind) — i.e. −1 to the input price. The pass-through caveat is load-bearing: if electrolyte ASP fully indexes to 6F (common in long-term cell contracts), the sign attenuates toward 0; in a price war with weak pass-through the −1 bites. Contrast with 天赐: same chain position, OPPOSITE net basis because 新宙邦 lacks the captive-6F hedge. Curator pins the sign.
- **materiality**: 300037 新宙邦 is an electrolyte maker that mainly PURCHASES LiPF6 (not integrated like 天赐), so 6F is a real external COGS input — the largest single material cost of electrolyte. revenue_share≈0.5 is an HONEST RANGE-MIDPOINT for LiPF6 as a fraction of ELECTROLYTE-SEGMENT material COST (commonly ~40-60%, regime-dependent), NOT a fraction of total company revenue/COGS — 新宙邦 also has 氟化工/电容化学品/半导体化学品 segments diluting the whole-name 6F-COGS share BELOW this electrolyte-only figure (graph node 300037 confirms 新宙邦 carries 氟化工/电容化学品). strength=0.55 (below the 0.5 electrolyte-segment COGS share would imply at full concentration) appropriately reflects that whole-name dilution. Cost-taker −1 absent pass-through; attenuates if ASP indexes to 6F. VERIFIED: no type error — correct cost leg for a 6F buyer, sign genuinely opposite to 天赐's hedged basis. Roster-confirmed: graph node 300037 = subindustry electrolyte.
- **evidence**: Well-known electrolyte BOM fact: lithium hexafluorophosphate (LiPF6 / 6F) is the highest-value and largest single cost component of lithium-ion battery electrolyte — industry-cited at roughly 40-60% of electrolyte material cost, rising as a share when 6F prices spike (e.g. 2021-22). 新宙邦 (300037) is a leading electrolyte maker with materially LOWER 6F self-supply than the integrated 天赐, so it is structurally a 6F price-taker on the cost side. Exact pass-through and self-supply ratios vary by year/contract; share given as an honest range, not a pinned figure.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300037.SZ)

### COMM:NICKEL — 镍 (Nickel)  (2 edges)

#### → `688005.SH` 容百科技  · strength 0.78 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): Curator to pin. 容百 is a ternary-cathode BUYER of nickel (not a producer), so the natural pin is -1 for 容百 absent full pass-through: nickel (delivered as nickel sulfate -> NCM/NCA precursor) is the single largest metal-cost component in high-nickel cathode, so rising nickel compresses gross margin in the window before price is passed through. Counter-direction (+1) applies only under metal-linked / cost-plus '金属价+加工费'-style pricing, where higher nickel mechanically inflates pass-through revenue and produces inventory gains in a rising market; A-share ternary cathode contracts commonly carry PARTIAL metal-price linkage, which dampens but rarely fully neutralizes the cost shock, so the lag/regime determines which polarity dominates. Curator decides given the prevailing pass-through regime.
- **materiality**: 容百 is a pure-play high-nickel ternary (NCM/NCA) cathode leader; high-nickel chemistries (NCM8-series/NCA) are its core product, making nickel its most-exposed single metal input via the nickel-sulfate -> 前驱体 -> cathode BOM path. High strength (0.78) reflects pure-play status. revenue_share left null deliberately: exact nickel COGS fraction NOT fabricated. Verified: KB graph-new_energy-v0.1.json node 688005 = subindustry 'cathode', note '三元正极 leader'. (Distinct from roster's 301358 湖南裕能 LFP, which has NO nickel.) Residual caveat the curator should weigh: partial cost-plus pass-through and 容百's gradual mix diversification (LMFP/钠电/Mn-rich exploration) can dilute sensitivity at the margin, but core revenue remains high-nickel ternary.
- **evidence**: 容百科技 (688005) is the leading A-share high-nickel ternary (NCM/NCA) cathode producer; ternary cathode is made from ternary precursor (前驱体) whose dominant metal input is nickel delivered as nickel sulfate (硫酸镍). High-nickel chemistries by definition maximize nickel content, so nickel price is the primary metal-cost swing factor for this product line. KB graph-new_energy-v0.1.json node 688005 describes it as '三元正极 leader' (subindustry_tag cathode), confirming the type. Exact COGS fraction not asserted to avoid fabricating a figure.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688005.SH)

#### → `300073.SZ` 当升科技  · strength 0.62 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): Curator to pin. 当升 is a ternary-cathode BUYER of nickel, so the natural pin is -1 for 当升 absent full pass-through: nickel sulfate flows through ternary precursor into its NCM/NCA cathode and is a major metal-cost component, compressing margin on a price spike before contractual pass-through catches up. (+1) applies only under metal-linked/cost-plus pricing where rising nickel lifts pass-through revenue and inventory value. Materiality qualifier vs 容百: 当升's product mix includes 磷酸铁锂 (LFP), which contains NO nickel, so a portion of output is unexposed and its BLENDED nickel sensitivity is diluted relative to a pure-play ternary maker. Curator pins dominant polarity given pass-through regime and the ternary share of mix.
- **materiality**: 当升 produces ternary (三元) cathode, giving a direct nickel-sulfate-via-precursor exposure on the same BOM path as 容百. KB node note flags it also makes 磷酸铁锂 (LFP), which is nickel-free, so overall nickel sensitivity is material but PARTIAL/diluted — hence a correctly lower strength (0.62) than pure-play 容百 (0.78). revenue_share null: precise nickel COGS fraction not fabricated, and is blended down by the LFP portion of mix. Verified: KB graph-new_energy-v0.1.json node 300073 = subindustry 'cathode', note '正极 (三元 + 磷酸铁锂)' — confirms BOTH the real ternary/nickel exposure AND the nickel-free LFP dilution.
- **evidence**: 当升科技 (300073) is an A-share cathode maker whose product line includes ternary (NCM/NCA) cathode, which consumes nickel sulfate via ternary precursor. KB graph-new_energy-v0.1.json node 300073 explicitly notes scope as '正极 (三元 + 磷酸铁锂)', confirming a real ternary/nickel exposure AND a nickel-free LFP segment that dilutes blended sensitivity. Exact COGS share not asserted to avoid fabrication.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300073.SH)

### COMM:COBALT — 钴 (Cobalt)  (2 edges)

#### → `688005.SH` 容百科技  · strength 0.5 · revenue_share 0.25 · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): Conditional polarity for the high-nickel NCM-cathode maker; 容百 is a cathode BUYER of cobalt (via 硫酸钴 precursor), NOT a cobalt seller, so the lithium-miner-style +1 'price IS revenue' logic does NOT apply. (a) COST-channel, -1: a cobalt price rise lifts ternary-cathode COGS and compresses 容百's unit margin TO THE EXTENT the move is NOT recovered from customers. (b) PASS-THROUGH / margin-neutral, ~0 net: China ternary-cathode commercial terms are predominantly metal-price-linked cost-plus (金属价格联动 + 加工费), so most of the cobalt move flows straight to the downstream customer and the processing fee (加工费) is the true steady-state margin driver -> net P&L sensitivity is muted. (c) INVENTORY-revaluation, ±: a sharp cobalt move can mark up low-cost metal/precursor inventory on a rising tape (+) or force a write-down on a falling tape (-), independent of steady-state pass-through. Curator pins which channel dominates for the studied horizon.
- **materiality**: Cobalt is a genuine BOM line for NCM cathode but secondary to nickel and lithium by cost, and 容百 specializes in HIGH-nickel chemistry (NCM811 / 9-series) where the cobalt fraction is at the LOWER end of the honest ~15-35% of cathode-metals-cost range. revenue_share 0.25 is a sell-side-grade COGS-fraction ESTIMATE (not disclosed) and approximate. Net equity sensitivity is materially dampened by cost-plus 加工费 pass-through -> strength held at mid (0.5), not high. Consistent with the house P11 commodity-stock-map.yaml, which lists ONLY cobalt MINERS (华友钴业/寒锐钴业/洛阳钼业/格林美) under `cobalt` (not cathode makers) precisely because the cathode-maker net price-sensitivity is muted; this raw_material edge is the complementary BOM-cost view, honestly down-weighted.
- **evidence**: Cobalt is the 'C' in NCM (nickel-cobalt-manganese) ternary cathodes; cobalt sulfate (硫酸钴) is the standard cobalt-bearing precursor input. 容百科技 is a leading Chinese high-nickel NCM cathode maker (chain graph node: 三元正极 leader, SW2021 电池 801737.SW). Chinese ternary-cathode commercial terms are widely structured as metal-price-linked cost-plus processing-fee (加工费) contracts, so raw-metal moves are largely passed downstream; exact per-name pass-through ratio and cobalt COGS share are not publicly disclosed.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688005.SH); config/commodity-stock-map.yaml (cobalt: miners-only list 华友/寒锐/洛阳钼业/格林美)

#### → `300073.SZ` 当升科技  · strength 0.4 · revenue_share 0.18 · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): Same conditional structure as 容百, but 当升's net cobalt intensity is DILUTED by a meaningful LFP (磷酸铁锂) segment that contains NO cobalt. 当升 is a cathode BUYER of cobalt, not a seller -> no +1 'price-IS-revenue' leg. (a) COST-channel, -1: higher cobalt raises COGS on 当升's TERNARY (NCM/NCA) line and squeezes unit margin only to the extent not recovered from customers; the LFP line is unaffected. (b) PASS-THROUGH / margin-neutral, ~0 net: 当升 sells ternary under metal-price-linked cost-plus terms (加工费 is the margin), so the bulk of a cobalt move transmits to the buyer and steady-state P&L sensitivity is small. (c) INVENTORY-revaluation, ±: sharp cobalt moves drive one-off inventory gains (rising) or write-downs (falling) on the ternary-precursor stock. Curator pins the dominant channel.
- **materiality**: FIXED DOWN from candidate's 0.5/0.25. 当升 is NOT a pure-ternary maker: the roster and house chain-graph node both flag a 三元 + 磷酸铁锂 (LFP) product mix, and the LFP segment has ZERO cobalt. Group-level cobalt COGS share and net sensitivity are therefore lower than for pure-ternary 容百, so strength 0.4 and revenue_share ~0.18 (group-blended COGS-fraction estimate, sell-side-grade, not disclosed). Cobalt remains secondary to nickel/lithium even within the ternary line. Net sensitivity further dampened by cost-plus pass-through.
- **evidence**: 当升科技 is a major Chinese ternary (NCM/NCA) cathode producer that ALSO makes LFP cathode (roster sub: cathode (ternary/NCM); house chain-graph node 300073.SH notes '正极 (三元 + 磷酸铁锂)'). Cobalt (via 硫酸钴) is an intrinsic input to its nickel-cobalt-manganese line but absent from its LFP line. Like the rest of the Chinese ternary-cathode segment its customer contracts are broadly metal-price-linked cost-plus (加工费) structures, passing most raw-metal moves downstream. Exact per-name pass-through and cobalt COGS share are not publicly disclosed.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300073.SH: '正极 (三元 + 磷酸铁锂)')

### COMM:NEEDLE_COKE — 针状焦/石油焦 (Needle / Petroleum Coke)  (2 edges)

#### → `603659.SH` 璞泰来  · strength 0.65 · revenue_share 0.4 · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): 璞泰来 is a coke BUYER (artificial-graphite anode maker), not a coke producer — no producer-revenue leg exists for this roster name. Dominant polarity is the COST side: −1 for 璞泰来 when needle/petroleum coke prices rise absent full pass-through, because coke is the principal carbon precursor for artificial graphite anodes (industry-cited at roughly one-third to one-half of anode MATERIAL cost, with graphitization electricity the other major cost bucket). Sign flips to +1 only on successful cost pass-through to cell customers (CATL/BYD etc.), which is sticky and lagged on long-term supply contracts. Net: a gross-margin-compression channel, not a revenue channel.
- **materiality**: FIXED: anode/负极 materials is 璞泰来's DOMINANT but not sole segment — it also has separator coating/base-film, lithium-ion coating materials, and automation-equipment businesses, so the original 'near pure-play' framing is slightly overstated. Coke is the primary raw material for its graphite anodes; the secondary in-segment driver is graphitization power, so coke alone is not 100% of anode COGS. revenue_share=0.4 is an HONEST mid-point of coke's share of anode MATERIAL cost — treat as a ~30-50% range, not a precise figure. strength trimmed 0.70→0.65 to reflect modest non-anode dilution while keeping it the highest-exposure roster name to this commodity. Verified: graph node 603659 = subindustry anode, '负极 leader'.
- **evidence**: Artificial graphite anodes (the dominant anode chemistry for Chinese cells) are produced from needle coke or petroleum coke as the carbon precursor, followed by graphitization; coke is widely recognized as the principal raw-material input to graphite anodes, with graphitization electricity the other major cost. 璞泰来 is one of China's largest dedicated graphite-anode producers, with anode materials its largest revenue segment. Roster-confirmed: graph node 603659.SH subindustry_tag=anode.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 603659.SH)

#### → `600884.SH` 杉杉股份  · strength 0.45 · revenue_share None · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): Same cost-side logic as the anode peer: 杉杉 is a coke BUYER, not a producer, so no producer-revenue leg. −1 for 杉杉's anode segment when coke prices rise absent pass-through (coke is the primary precursor for its graphite anodes); +1 only on successful, lagged cost pass-through to cell customers. KEY DIFFERENCE vs 璞泰来: 杉杉 is DIVERSIFIED — it also runs a large LCD polarizer-film (偏光片) business with ZERO coke exposure — so consolidated/full-name sensitivity to coke is materially diluted and a coke move must NOT be read as a full-company signal.
- **materiality**: 杉杉股份's anode (负极) business has the same direct coke dependence as 璞泰来, but at the consolidated/full-name level exposure is diluted by its sizeable non-battery polarizer-film segment. strength held at 0.45 (vs 璞泰来's 0.65) to reflect that dilution. revenue_share left null because coke's share of TOTAL company COGS is not estimable given the multi-segment mix — within the anode segment alone it is comparable to the ~30-50% precursor range, but no whole-company figure is asserted. Verified: graph node 600884 = subindustry anode, '负极 + 偏光片 — DIVERSIFIED'.
- **evidence**: 杉杉股份 operates a major graphite-anode (负极) business that, like all artificial-graphite anode makers, uses needle/petroleum coke as its primary carbon precursor; the company also has a large LCD polarizer-film segment unrelated to batteries, making it a diversified name where anode-input shocks transmit only partially to the consolidated result. Roster-confirmed: graph node 600884.SH subindustry_tag=anode (diversified, 偏光片 flagged).
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 600884.SH)

### COMM:SODA_ASH — 纯碱 (Soda Ash)  (1 edges)

#### → `601865.SH` 福莱特  · strength 0.5 · revenue_share 0.2 · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): Conditional, for the curator to pin. 福莱特 is a PV-glass BUYER of soda ash, not a producer, so only the cost-side leg exists: PROPOSE −1 for 福莱特 when soda-ash prices rise absent full pass-through (soda ash is the principal NON-energy raw material in the 光伏玻璃 melt, so a price spike compresses gross margin), and symmetric +1 (margin tailwind) when soda ash falls. The pass-through condition is the gate: PV-glass ASP is set on its OWN duopoly capacity/demand cycle (with 信义光能 HK, tracked weekly), so cost relief/burden reaches the P&L only to the extent the glass cycle is loose/tight enough to (not) pass it through — when glass is tight and pricing power is high, cost moves are largely passed through and the margin sensitivity attenuates; when glass is loose/oversupplied, the buyer eats it and the −/+ sign bites hardest. There is NO producer-revenue (+1) leg here because no roster name produces soda ash. Curator pins the sign and the regime weighting.
- **materiality**: Moderate, margin-channel (NOT revenue). Soda ash is a direct, genuine batch input to 光伏玻璃 (real glass chemistry: silica + soda ash + carbonate flux), and is the single largest NON-energy raw material in the glass melt. As a near-pure-play PV-glass leader, 福莱特's gross margin is genuinely sensitive to soda-ash price swings. But the effect is second-order to (a) the PV-glass price cycle itself and (b) natural-gas/energy cost (typically the single largest cost line), so materiality is moderate, not dominant. Corrected vs candidate: trimmed revenue_share 0.25->0.20 and strength 0.55->0.50 — the candidate's 0.25 sat at the optimistic top of the honest range and mixed the raw-material-cost denominator with the COGS denominator; soda ash is closer to ~15-25% of TOTAL manufacturing cost (COGS), mid ~0.20, not 0.25.
- **evidence**: Well-established industry fact: the PV-glass (光伏玻璃) furnace batch is dominated by 石英砂 (silica/quartz sand) and 纯碱 (soda ash), melted with natural gas; soda ash is the principal non-energy raw material and the standard glass-making flux that lowers silica's melting point. Sell-side/industry cost decompositions commonly place soda ash at roughly 20-35% of PV-glass RAW-MATERIAL cost or ~15-25% of TOTAL manufacturing cost — given as an honest range (exact share varies with energy mix, quartz cost, and the soda-ash price level), NOT a pinned figure. 福莱特 (601865.SH) is a dedicated PV-glass leader (duopoly with 信义光能 HK), so this commodity flows straight into COGS. Corroborated by the project's own new-energy graph (graph-new_energy-v0.1.json), which tags 601865 subindustry_tag='pv_glass' / '光伏玻璃 leader … 组件 BOM; own price cycle (price-weekly tracked)', and by config/commodity-stock-map.yaml CONTENT GAP §F, which explicitly recognizes 纯碱/soda ash and 玻璃 as deferred commodity classes.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 601865.SH); config/commodity-stock-map.yaml (CONTENT GAP §F: 纯碱/玻璃 deferred)

### COMM:EVA_POE_RESIN — EVA/POE 树脂 (EVA / POE Resin)  (1 edges)

#### → `603806.SH` 福斯特  · strength 0.85 · revenue_share 0.75 · hop 1 · confidence high
- **proposed_sign_basis** (for curator; NOT a pin): 福斯特 is a downstream CONSUMER of EVA/POE resin (粒子), not a producer, so the cost-side polarity dominates: −1 for 福斯特 when resin prices rise AND pass-through to film ASP is incomplete/lagged (resin is the overwhelming-majority COGS of encapsulant film, so a margin squeeze is the default short-horizon read). The +1 leg applies only conditionally: if 福斯特 fully or over-passes resin cost into film price (it is the >50%-share film leader with pricing power and largely cost-plus contracts that re-price on a lag), rising resin can be margin-neutral or even widen nominal spread, and falling resin can compress ASP faster than COGS. Net: margin/timing-driven, predominantly an inverse cost exposure with pass-through completeness/lag the swing factor — curator to pin direction.
- **materiality**: EVA/POE resin (粒子) is the single dominant raw material in solar encapsulant film and by far the largest component of 福斯特's COGS. Cited resin-share-of-film-COGS spans a wide band — Western trade sources put the EVA portion at ~60-70% of production cost, while CN annual-report-based sources put total direct material (EVA+POE) near ~85-90%; 0.75 is a defensible mid-band estimate. Film margins are highly sensitive to the resin price cycle and to the lag between resin moves and film ASP re-pricing; this is the textbook pass-through margin node of the PV auxiliary-materials chain. POE in particular is import/oligopoly-constrained (三井化学/LG化学/陶氏), amplifying input-cost and margin volatility. Empirically validated: 2023 EVA price swings of ~±40% directly compressed film-maker profits and 福斯特 net profit fell ~29% in 2024 despite >50% share. Verified: graph node 603806 = subindustry encapsulant_film, 'EVA/POE 树脂 price pass-through'.
- **evidence**: 福斯特 is the dominant global solar encapsulant film maker (光伏胶膜 leader, >50% global share). Encapsulant film is manufactured from EVA and POE resin pellets, which constitute the overwhelming majority of film bill-of-materials cost — sources range from ~60-70% (EVA portion, Western trade research) to ~85-90% (total direct material incl. POE, CN annual-report sources); honest band, exact share varies by EVA-vs-POE mix and period. POE resin is supply-tight and largely imported from a small oligopoly of petrochemical producers (三井化学/LG化学/陶氏), making 福斯特's input cost and gross margin closely tracked against the resin price cycle. Internal chain graph (graph-new_energy-v0.1.json) independently encodes 603806.SH subindustry_tag=encapsulant_film with note 'EVA/POE 树脂 price pass-through'.
- **source_ref**: data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 603806.SH)

## Quality summary

39 verified raw_material edges across 9 commodity nodes, handed off for the KB curator's sign-pinning pilot. Counts by commodity: LITHIUM_CARBONATE 11, POLYSILICON 8, COPPER 9, LIPF6 3, NICKEL 2, COBALT 2, NEEDLE_COKE 2, SODA_ASH 1, EVA_POE_RESIN 1. Dedup: zero exact duplicates removed (none existed); the candidate set was already distinct at the (commodity -> target) grain. Five codes legitimately recur across multiple commodities and are KEPT as separate, complementary edges (this is the point of the exercise, not a dup): 688005 容百 (Li / Ni / Co), 300073 当升 (Li / Ni / Co), 002407 多氟多 (Li-feedstock-cost + LiPF6-producer-revenue), 002709 天赐 (Li two-hop + LiPF6 integrated-producer), and the four cell makers 300750/300014/002074/688063 (Li-cathode + copper-foil). Sign discipline: EVERY edge carries transmission_sign='±' — none was pinned in the input and none was changed; the proposed_sign_basis fields are explicitly framed as proposals for the human curator, including the deliberately counterintuitive cases (e.g. CATL where metal-linked pricing can make FALLING lithium net-positive). Every target was cross-checked against the live roster of 31 tradeable codes in data/operator-feeds/industry-chain/graph-new_energy-v0.1.json; all 39 targets are on-roster and each materiality_note now cites the verified node subindustry_tag. Highest-confidence FLAGSHIP edges (clean producer-revenue +1, near-pure-play, strength >=0.93): LITHIUM_CARBONATE->002466 天齐 (0.95), LITHIUM_CARBONATE->002460 赣锋 (0.93), POLYSILICON->688303 大全 (0.95) — these are the textbook 'price IS revenue' upstream names where the only nuance is magnitude, not direction. Materiality honesty is the spine of the set: strengths span 0.95 down to a deliberate 0.18 floor (COPPER->688032 禾迈, a semiconductor-heavy microinverter where copper is genuinely minor but the channel is real); revenue_share is left null wherever a precise COGS fraction is not disclosable (lithium/cathode/cell BOM swings violently with price; inverter copper has no credible public %) and is given only as an honest range-midpoint where the literature supports one (poly ~0.35, electrolyte-segment 6F ~0.5, soda ash ~0.20 of total mfg cost, EVA/POE ~0.75). Two-sided cost edges (cathode/cell/electrolyte/film/glass/coke/copper) carry an explicit pass-through gate so the curator pins by price regime; pure-producer edges (miners, poly, 6F-producer) carry a one-sided +1 proposal. The COBALT and one NICKEL/Li strength were trimmed from the candidate values to respect the LFP-dilution in 当升 (cobalt 0.5/0.25 -> 0.4/0.18) and the LiPF6-spread dominance in 天赐 (Li 0.5 -> 0.4).

## Gaps deliberately excluded

Deliberately EXCLUDED relationships, with reasons (quality-over-coverage discipline; this is a curated pilot, not a dump):

1. RARE EARTH / 磁材 (NdFeB EV-motor magnets) — EXCLUDED, no target node. The natural downstream magnet makers (金力永磁 300748, 宁波韵升 600366) and rare-earth miners (北方稀土 600111, 中国稀土 000831, 广晟有色 600259) exist in config/commodity-stock-map.yaml under commodity_class: rare_earths, but NONE are nodes in graph-new_energy-v0.1.json. The new_energy roster covers PV (硅料->组件/逆变器/辅材) and the lithium-battery chain (锂盐->正/负极/电解液/隔膜->电芯/储能), and stops at the cell; it has NO EV-motor / magnet / 永磁 sub-tree. With no on-roster target, a COMM:RARE_EARTH or COMM:NDFEB edge would have to point at a code that does not exist in this graph, so the entire rare-earth->magnet->EV-motor relationship is dropped rather than fabricated. Flag for the curator: if a magnet/motor sub-tree is later added (or the rare_earths cohort from commodity-stock-map is promoted into the KB graph), this is the first gap to backfill.

2. SEPARATOR raw materials (隔膜) — EXCLUDED, insufficiently clean commodity. The roster DOES contain separator makers 恩捷 002812 and 星源材质 300568 (subindustry_tag=separator), but the wet/dry-process separator BOM is dominated by base-film PE/PP polymer + capex/equipment + line yield, not a cleanly-priced exchange-traded commodity. There is no COMM node for separator-grade polyethylene that would carry a defensible, materiality-honest pass-through edge, so these two roster names get no commodity edge here. (They remain reachable in the graph via the EVDEMAND customer edges.)

3. SILVER PASTE (银浆) into solar cells — EXCLUDED, no silver-paste / silver commodity node in scope and the cell makers (钧达 002865, 爱旭 600732) are already carried under POLYSILICON via wafer-mediated exposure. Silver is a real and topical cost line for TOPCon/HJT cells (and 钧达's node note explicitly flags 银浆耗量降本), but adding a COMM:SILVER edge would require a silver-paste sub-node and would overlap awkwardly with the precious-metals silver class in commodity-stock-map (which maps to zinc/lead smelters, not PV). Deferred pending an explicit silver-paste node.

4. NATURAL GAS / ENERGY into PV glass — EXCLUDED by materiality framing, not by error. Natural gas (furnace fuel) is typically the SINGLE LARGEST cost line for 福莱特's PV glass, larger than soda ash. It is omitted only because there is no COMM:NATURAL_GAS node in this hand-off scope; the SODA_ASH edge explicitly notes gas/energy as the dominant cost the curator should keep in view. Worth adding if an energy-commodity node is introduced.

5. PHOSPHORUS / IRON PHOSPHATE into LFP cathode (湖南裕能 301358) — EXCLUDED, no phosphate/磷化工 commodity node in scope. LFP cathode BOM is lithium carbonate + iron phosphate; only the lithium-carbonate leg is carried (it is the dominant and most price-volatile input). The phosphate leg is real but secondary and has no on-roster commodity node; deferred per commodity-stock-map CONTENT GAP §F (phosphate 磷化工 is a v0.2 deferral).

6. POLYSILICON / soda ash / glass as commodity CLASSES are themselves flagged DEFERRED in config/commodity-stock-map.yaml CONTENT GAP §F (多晶硅 PS.GFE, 纯碱, 玻璃 FG.CZC). They are included HERE as commodity NODES anyway because the new_energy graph has clean, well-known downstream target nodes for them (poly -> 大全/通威/module makers/cell makers; soda ash -> 福莱特); the deferral in the YAML is about futures-feed plumbing for the P11 quant signal, not about the supply-chain fact, so the raw_material edge is still well-grounded.

Nothing was KILLED from the supplied verified-kept list (the 'Killed' input was empty); all 39 supplied edges survived verification with only the noted strength/revenue_share trims that were already baked into the candidate values.

## Machine-readable (for KB ingest — review:pending ±)

```json
{
  "commodity_nodes": [
    {
      "code": "COMM:LITHIUM_CARBONATE",
      "name": "碳酸锂 (Lithium Carbonate)",
      "node_type": "commodity",
      "subindustry_tag": "energy_metal_lithium"
    },
    {
      "code": "COMM:POLYSILICON",
      "name": "多晶硅 (Polysilicon)",
      "node_type": "commodity",
      "subindustry_tag": "pv_silicon_feedstock"
    },
    {
      "code": "COMM:NICKEL",
      "name": "镍 (Nickel)",
      "node_type": "commodity",
      "subindustry_tag": "base_metal_nickel"
    },
    {
      "code": "COMM:COBALT",
      "name": "钴 (Cobalt)",
      "node_type": "commodity",
      "subindustry_tag": "energy_metal_cobalt"
    },
    {
      "code": "COMM:LIPF6",
      "name": "六氟磷酸锂 (Lithium Hexafluorophosphate, 6F)",
      "node_type": "commodity",
      "subindustry_tag": "electrolyte_lithium_salt"
    },
    {
      "code": "COMM:NEEDLE_COKE",
      "name": "针状焦/石油焦 (Needle / Petroleum Coke)",
      "node_type": "commodity",
      "subindustry_tag": "anode_carbon_precursor"
    },
    {
      "code": "COMM:SODA_ASH",
      "name": "纯碱 (Soda Ash)",
      "node_type": "commodity",
      "subindustry_tag": "pv_glass_flux"
    },
    {
      "code": "COMM:EVA_POE_RESIN",
      "name": "EVA/POE 树脂 (EVA / POE Resin)",
      "node_type": "commodity",
      "subindustry_tag": "encapsulant_resin"
    },
    {
      "code": "COMM:COPPER",
      "name": "铜 (Copper)",
      "node_type": "commodity",
      "subindustry_tag": "base_metal_copper"
    }
  ],
  "candidate_edges": [
    {
      "source": "COMM:LITHIUM_CARBONATE",
      "target": "002466.SZ",
      "target_name": "天齐锂业",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "+1 for the miner: lithium carbonate/hydroxide price IS essentially this company's selling price, so revenue and gross profit move directly with the commodity. There is no meaningful −1 case here — as a pure-play upstream lithium producer it benefits unambiguously from rising lithium prices and suffers from falling ones. The only nuance the curator should weigh is that a portion of value sits in its SQM/Greenbushes equity stakes, but those are also lithium-price-levered, so the sign is reinforced, not flipped.",
      "strength": 0.95,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Pure-play lithium salt and concentrate producer (Greenbushes spodumene + Kwinana hydroxide). Lithium price is the dominant earnings driver; among the highest-beta A-share names to the lithium spot curve. Verified: graph node 002466 = subindustry lithium_salt, '锂盐/锂矿, 碳酸锂-price levered'.",
      "evidence": "天齐锂业 is one of the world's largest lithium producers, controlling a stake in the Greenbushes hard-rock mine (via Tianqi/IGO JV) and holding a large equity stake in Chile's SQM. Its revenue is overwhelmingly lithium concentrate and lithium chemicals, so its profitability tracks the lithium carbonate/hydroxide price cycle (it swung to large profits in the 2021-2022 price spike and saw earnings collapse as prices fell in 2023-2024). This is widely reported and not a fabricated figure. Roster-confirmed: graph-new_energy-v0.1.json node 002466.SZ subindustry_tag=lithium_salt.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002466.SZ); config/commodity-stock-map.yaml (lithium_carbonate, exposure 1.0)"
    },
    {
      "source": "COMM:LITHIUM_CARBONATE",
      "target": "002460.SZ",
      "target_name": "赣锋锂业",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "+1 for the miner/converter: lithium salt price is the company's revenue, so earnings rise and fall with the commodity. No material −1 case — as an upstream lithium producer it is a long-the-commodity name. Curator nuance: 赣锋 is more vertically integrated downstream than 天齐 (it also makes batteries/cells), so a sliver of its business is actually short lithium-as-a-cost; but the lithium-salt segment dominates the P&L, so net exposure remains strongly +1.",
      "strength": 0.93,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Integrated lithium producer: brine/spodumene resources plus lithium carbonate and hydroxide conversion. Lithium price is the primary earnings lever; high-beta to the spot curve, with a small downstream battery hedge. Verified: graph node 002460 = subindustry lithium_salt, '锂盐/锂矿 leader'.",
      "evidence": "赣锋锂业 is a leading global lithium compounds producer with upstream resource interests (e.g. Mariana/Cauchari brine projects in Argentina, Mt Marion spodumene offtake) and large lithium hydroxide/carbonate conversion capacity. Its core revenue is lithium chemicals, so profitability tracks the lithium price cycle, with reported earnings booming in the 2021-2022 spike and compressing as prices fell. It also has a smaller battery business, making it slightly less of a pure-play than 天齐. Roster-confirmed: graph node 002460.SZ subindustry_tag=lithium_salt.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002460.SZ); config/commodity-stock-map.yaml (lithium_carbonate, exposure 1.0)"
    },
    {
      "source": "COMM:LITHIUM_CARBONATE",
      "target": "301358.SZ",
      "target_name": "湖南裕能",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Genuinely two-sided. Lithium carbonate is by far the single largest input cost for LFP cathode. (a) When pricing power / cost-plus tolling contracts hold and inventory is matched, lithium moves are largely passed through to cell-maker customers, so margin is roughly neutral and the company can even book inventory GAINS on a fast rise — a transient +1. (b) When lithium prices FALL sharply (the 2023-2024 case), LFP cathode makers eat inventory write-downs and price down their output faster than cheap lithium reaches COGS — a painful −1. So the curator should pin direction by regime: rising-with-passthrough vs falling-with-destocking. Note: this is LFP, so NO nickel/cobalt exposure — lithium carbonate is the relevant commodity, not lithium hydroxide or sulfate.",
      "strength": 0.85,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Largest LFP cathode (磷酸铁锂) maker in China. Lithium carbonate is the dominant bill-of-materials line for LFP cathode; revenue and reported margin are heavily distorted by lithium price swings and inventory timing. revenue_share nulled: lithium's COGS share for LFP cathode swings violently with the lithium price (>50% at the 2022 peak, far less after the 2023-2024 collapse), so a fixed figure overstates precision. Verified: graph node 301358 = subindustry cathode, '磷酸铁锂正极 leader'.",
      "evidence": "湖南裕能 is the leading LFP cathode active-material supplier (main customers 宁德时代 and 比亚迪). For LFP cathode, lithium carbonate is the largest single raw-material cost — industry commentary commonly cites lithium as well over half of LFP cathode material cost at high lithium prices, falling sharply after the 2023-2024 price collapse. LFP uses iron phosphate and lithium carbonate only — no nickel or cobalt. Roster-confirmed: graph node 301358.SZ subindustry_tag=cathode (磷酸铁锂正极 leader).",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 301358.SZ)"
    },
    {
      "source": "COMM:LITHIUM_CARBONATE",
      "target": "688005.SH",
      "target_name": "容百科技",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Two-sided cost exposure. Lithium (here largely lithium hydroxide/carbonate, plus nickel/cobalt for ternary) is a major COGS line for NCM cathode. (a) Under cost-plus/tolling pricing with matched inventory, lithium moves pass through → near-neutral to transient +1 (inventory gains on a rise). (b) On a sharp lithium decline, ternary cathode makers take inventory losses and margin compression → −1. Curator pins by regime and by how much of the contract book is true cost-pass-through tolling. Unlike the LFP name, 容百 ALSO carries nickel/cobalt exposure (see the separate NICKEL and COBALT edges for this same code), so lithium is one of several commodity drivers, not the sole one — slightly lower strength than the pure-LFP case.",
      "strength": 0.72,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Leading ternary (NCM/high-nickel) cathode maker. Lithium hydroxide/carbonate is a major raw-material cost alongside nickel and cobalt; margins and inventory marks are sensitive to the lithium cycle but exposure is shared with Ni/Co. Verified: graph node 688005 = subindustry cathode, '三元正极 leader'. This code legitimately appears under three commodities (LITHIUM_CARBONATE / NICKEL / COBALT) — distinct edges, not duplicates.",
      "evidence": "容百科技 is China's leading high-nickel ternary cathode producer. Ternary cathode bill-of-materials is dominated by lithium (carbonate/hydroxide), nickel sulfate and cobalt sulfate; lithium is one of the top cost lines. Because the commodity basket is split across Li/Ni/Co, lithium is material but not the sole driver — no precise COGS share asserted because it varies with both metal prices and product mix (high-Ni vs mid-Ni). Roster-confirmed: graph node 688005.SH subindustry_tag=cathode.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688005.SH)"
    },
    {
      "source": "COMM:LITHIUM_CARBONATE",
      "target": "300073.SZ",
      "target_name": "当升科技",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Same two-sided structure as the other ternary cathode maker: lithium (hydroxide/carbonate) is a major COGS line shared with nickel/cobalt. (a) Cost-plus pass-through + matched inventory → neutral/transient +1 on a rise. (b) Sharp lithium decline → inventory write-downs and margin squeeze → −1. Curator pins by price regime and contract structure. Lithium is material but co-exists with Ni/Co exposure (and a nickel-free LFP segment), so it is not the single dominant commodity the way it is for an LFP-only cathode maker.",
      "strength": 0.7,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Ternary (NCM) cathode maker with significant export/overseas customer base. Lithium hydroxide/carbonate is a major input cost alongside nickel and cobalt; sensitive to lithium cycle and inventory timing. Verified: graph node 300073 = subindustry cathode, '正极 (三元 + 磷酸铁锂)'. This code also appears under NICKEL and COBALT — distinct edges.",
      "evidence": "当升科技 is a major Chinese ternary cathode active-material supplier with a notable international customer mix. As with all NCM cathode producers, lithium compounds are among the largest raw-material costs together with nickel and cobalt salts. The exact lithium COGS share varies with metal prices and product mix, so no fixed percentage is asserted. Roster-confirmed: graph node 300073.SZ subindustry_tag=cathode (三元 + 磷酸铁锂).",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300073.SZ)"
    },
    {
      "source": "COMM:LITHIUM_CARBONATE",
      "target": "300750.SZ",
      "target_name": "宁德时代",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Two-sided, and the polarity hinges on contractual pass-through. Lithium (carbonate, via cathode) is the single largest material cost embedded in a battery cell. (a) CATL runs metal-price linked pricing clauses with many large customers (lithium-carbonate-indexed pricing, e.g. the 锂矿返利/metal-linkage mechanisms), so it can pass much of the lithium move through to OEMs → cost rises are largely neutralized, and falling lithium can even EXPAND unit margin if ASPs lag the input drop (transient +1 on a decline). (b) Where pass-through is incomplete or lithium spikes faster than repricing, margin compresses and inventory can be marked down → −1. So unusually for a downstream name, the curator may find that FALLING lithium is net positive for CATL margins — direction is genuinely regime- and contract-dependent, which is exactly why the sign must stay ±. (NB the graph's SIGN INVERSION REGISTRY pre-notes 碳酸锂↑ => −1 电芯; that is the naive cost leg, which the pass-through mechanism can override — leave ± for the curator.)",
      "strength": 0.75,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "World's largest battery cell/pack maker. Lithium (through cathode) is the largest single material cost in a cell, but strong metal-price-linked customer contracts mute and can even invert the naive cost sign. Hop is via cathode but exposure is direct and very material. Verified: graph node 300750 = subindustry battery_cell, 'margin COMPRESSES when 碳酸锂 spikes (cost)'. Also carries a COPPER edge (copper-foil) — distinct.",
      "evidence": "宁德时代 is the global leader in lithium-ion battery cells and packs. Cathode (where lithium carbonate sits) is the most expensive cell material, so lithium is CATL's largest indirect raw-material exposure. CATL is widely reported to use metal-price-linked pricing and rebate mechanisms with major customers, which transmit lithium-price moves to OEMs; this is why its battery gross margin held up and in some periods improved even as lithium prices fell sharply in 2023-2024. Mechanism asserted, not a precise COGS percentage. Roster-confirmed: graph node 300750.SZ subindustry_tag=battery_cell.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300750.SZ)"
    },
    {
      "source": "COMM:LITHIUM_CARBONATE",
      "target": "300014.SZ",
      "target_name": "亿纬锂能",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Two-sided cell-maker exposure: lithium (via cathode) is the largest material cost. (a) To the extent power/storage cell pricing is metal-linked or repriced quickly, lithium moves pass to customers → neutral to transient +1 on a decline (margin recovery as cheap lithium reaches COGS). (b) When lithium spikes faster than cell ASPs or pass-through is weak (it has less pricing power than CATL), margin compresses and inventory marks bite → −1. Curator pins by regime and by 亿纬's weaker contractual leverage vs the market leader.",
      "strength": 0.65,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Major power and energy-storage cell maker. Lithium-through-cathode is the largest material cost; pass-through pricing power is real but weaker than the market leader, so margin sensitivity to the lithium cycle is somewhat higher. Verified: graph node 300014 = subindustry battery_cell. Also carries a COPPER edge — distinct.",
      "evidence": "亿纬锂能 is a top-tier Chinese battery cell producer across consumer, power and energy-storage segments. As with any lithium-ion cell maker, the cathode (lithium-bearing) is the dominant material cost, so the lithium price cycle and inventory timing materially affect cost and reported margin. It generally commands less customer pricing power than 宁德时代, so it absorbs more of the lithium swing. Mechanism asserted, no fabricated COGS figure. Roster-confirmed: graph node 300014.SZ subindustry_tag=battery_cell.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300014.SZ)"
    },
    {
      "source": "COMM:LITHIUM_CARBONATE",
      "target": "002074.SZ",
      "target_name": "国轩高科",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Two-sided, and especially lithium-carbonate-centric because 国轩 is LFP-heavy (LFP cells use lithium carbonate, not hydroxide, and have NO nickel/cobalt). (a) With pass-through/repricing, lithium moves transmit to customers → neutral/transient +1 on a falling-lithium regime as cheaper carbonate reaches COGS. (b) On a sharp rise with incomplete pass-through, margin compresses → −1; on a sharp fall it can take inventory losses on high-cost lithium and cathode stock. Curator pins by regime; note the LFP mix makes lithium carbonate the cleanest single commodity driver for this name.",
      "strength": 0.65,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "LFP-focused power and storage cell maker. Lithium carbonate (through LFP cathode) is the dominant material cost; no nickel/cobalt exposure. Margin and inventory marks track the lithium-carbonate cycle. Verified: graph node 002074 = subindustry battery_cell, '电芯 (磷酸铁锂-heavy)'. Also carries a COPPER edge — distinct.",
      "evidence": "国轩高科 is a major Chinese battery maker with a strong LFP product weighting (power and increasingly energy storage). LFP cells embed lithium carbonate via the cathode as the largest material cost and carry no nickel or cobalt, so lithium carbonate is the cleanest commodity driver of its unit economics. Mechanism asserted; COGS share left null because it swings with the lithium price. Roster-confirmed: graph node 002074.SZ subindustry_tag=battery_cell (磷酸铁锂-heavy).",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002074.SZ)"
    },
    {
      "source": "COMM:LITHIUM_CARBONATE",
      "target": "688063.SH",
      "target_name": "派能科技",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Two-sided storage-cell exposure, LFP-based (lithium carbonate, no Ni/Co). (a) Falling lithium lowers cell BOM cost and, if system ASPs lag, can support margin → transient +1; pass-through to its residential/commercial storage customers neutralizes part of the move. (b) Rising lithium or being caught long high-cost inventory during the 2023-2024 destock → −1 (派能 was notably hit by inventory/overstock dynamics in the storage channel). Curator pins by regime; somewhat lower strength because 派能 sells integrated storage SYSTEMS, so the cell/lithium cost is one layer beneath system-level and channel-inventory dynamics.",
      "strength": 0.55,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Residential/C&I energy-storage cell and system maker, LFP chemistry. Lithium carbonate (via LFP cathode) is a major cell cost; exposure is real but diluted by system-level integration and storage-channel inventory cycles. Verified: graph node 688063 = subindustry energy_storage_cell, '户储 pure-play'. Also carries a COPPER edge — distinct.",
      "evidence": "派能科技 is a leading independent residential energy-storage battery/system supplier using LFP chemistry. Its cells embed lithium carbonate via the LFP cathode as a major cost. Because it sells integrated storage systems and was exposed to the 2023-2024 storage-channel inventory glut, the lithium commodity effect is mediated by system pricing and destocking. Mechanism asserted; no fabricated figures. Roster-confirmed: graph node 688063.SH subindustry_tag=energy_storage_cell.",
      "confidence": "medium",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688063.SH)"
    },
    {
      "source": "COMM:LITHIUM_CARBONATE",
      "target": "002407.SZ",
      "target_name": "多氟多",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Two-sided. Lithium carbonate is a direct feedstock for lithium hexafluorophosphate (LiPF6, 六氟磷酸锂) — the lithium atom in LiPF6 comes from lithium carbonate. (a) When LiPF6 pricing tracks lithium feedstock and demand is firm, cost rises pass through → neutral/+1, and 多氟多 can book gains on a lithium/LiPF6 price spike (it earned outsized profits during the 2021-2022 LiPF6 boom). (b) When lithium and LiPF6 prices collapse with overcapacity (2023-2024), it suffers both lower ASPs and inventory losses → −1. Curator pins by LiPF6 price regime; lithium carbonate is a real but partial input (fluorine chemistry/HF and phosphorus also matter), and the dominant earnings swing is the LiPF6 SPREAD rather than lithium-carbonate cost in isolation, so it is material but not the sole driver. NB this is the lithium-FEEDSTOCK-cost view of 多氟多; the separate LIPF6 edge for the same code is the producer-REVENUE view — both are kept deliberately.",
      "strength": 0.55,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Major LiPF6 (六氟磷酸锂) producer. Lithium carbonate is a direct chemical feedstock for LiPF6; profitability tracks the LiPF6 cycle, which is itself partly driven by lithium-carbonate cost. Exposure shared with fluorine/HF chemistry; the LiPF6 spread, not lithium cost alone, is the primary lever. Verified: graph node 002407 = subindustry lithium_hexafluorophosphate (6F), SW2 化学制品 801034.SW.",
      "evidence": "多氟多 is one of China's largest producers of lithium hexafluorophosphate (LiPF6), the key lithium salt in electrolyte. LiPF6 synthesis consumes lithium carbonate (along with HF/fluorine chemistry), so lithium-carbonate cost feeds directly into its product cost, while its selling price is the LiPF6 price. It posted very large profits during the 2021-2022 LiPF6 price spike and then saw earnings fall sharply as LiPF6 prices collapsed on overcapacity. Mechanism well established; no precise COGS share asserted. Roster-confirmed: graph node 002407.SZ subindustry_tag=lithium_hexafluorophosphate.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002407.SZ)"
    },
    {
      "source": "COMM:LITHIUM_CARBONATE",
      "target": "002709.SZ",
      "target_name": "天赐材料",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Two-sided, mediated by its integrated LiPF6 position and weaker on a lithium-carbonate-SPECIFIC basis than the other names. 天赐 makes its own LiPF6, which consumes lithium carbonate; lithium-carbonate cost therefore flows into its electrolyte COGS, but two hops removed (lithium → LiPF6 → electrolyte) and LiPF6 is only a slice of electrolyte cost while lithium carbonate is only a slice of LiPF6 cost. (a) During the LiPF6 shortage/price boom its self-supply was a huge margin tailwind → +1; cost rises in lithium were more than offset by LiPF6 ASP. (b) When LiPF6/electrolyte prices collapsed (2023-2024) its self-made-LiPF6 advantage compressed and it carried high-cost lithium/LiPF6 inventory → −1. Curator pins by the electrolyte/LiPF6 price regime; the dominant swing factor is the electrolyte/LiPF6 spread, NOT lithium carbonate alone — strength trimmed accordingly. NB distinct from the LIPF6 edge for the same code, which captures the integrated-producer 6F view.",
      "strength": 0.4,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Integrated electrolyte leader that self-produces LiPF6. Lithium carbonate is a feedstock for its in-house LiPF6, so it has real but indirect (two-hop) lithium exposure that is the smallest and most diluted in this set; the dominant swing factor is the electrolyte/LiPF6 spread rather than lithium-carbonate cost. Strength downgraded from 0.5 to 0.4 to reflect that lithium-carbonate-specific materiality is modest. Verified: graph node 002709 = subindustry electrolyte, 'integrated into 6F'. Same code also appears under LIPF6 — distinct edges.",
      "evidence": "天赐材料 is China's largest electrolyte maker and is vertically integrated into LiPF6 (it produces its own lithium salt), which was a major competitive advantage during the 2021-2022 LiPF6 shortage. Because LiPF6 is made from lithium carbonate, lithium-carbonate cost feeds its electrolyte COGS; however LiPF6 is only part of electrolyte cost and lithium carbonate only part of LiPF6 cost (HF/fluorine chemistry dominates), so earnings are driven far more by the electrolyte/LiPF6 spread than by lithium carbonate in isolation. Mechanism established; no fabricated figure. Roster-confirmed: graph node 002709.SZ subindustry_tag=electrolyte.",
      "confidence": "medium",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002709.SZ)"
    },
    {
      "source": "COMM:POLYSILICON",
      "target": "688303.SH",
      "target_name": "大全能源",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "PROPOSED +1 (producer-revenue): polysilicon price IS Daquan's selling price — it is a near-pure-play poly producer, so poly price moves are revenue moves and (given a large fixed/cash-cost base) flow even more strongly to margin/profit. No offsetting downstream-cost leg. Curator should pin +1.",
      "strength": 0.95,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Pure-play polysilicon producer; poly is effectively ~100% of revenue. Highest-purity exposure on the roster. Profit is highly geared to poly price given the fixed/cash-cost base, so price→earnings sensitivity is amplified vs revenue alone. Verified: graph node 688303 = subindustry polysilicon, '硅料 pure-play'.",
      "evidence": "Daquan Energy (大全能源) is one of China's largest dedicated polysilicon producers and is essentially a single-product company; sales are overwhelmingly polysilicon. Pure-play status is uncontested. No exact revenue-share cited to avoid fabricated precision. Roster-confirmed: graph node 688303.SH subindustry_tag=polysilicon.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688303.SH)"
    },
    {
      "source": "COMM:POLYSILICON",
      "target": "600438.SH",
      "target_name": "通威股份",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "PROPOSED net +1 but INTEGRATED/AMBIGUOUS — curator must weigh: (a) +1 producer-revenue leg dominates — Tongwei is the world's largest polysilicon producer and poly is a major revenue/profit line; rising poly price lifts the poly segment. (b) −1 partial internal-cost offset — its large captive solar-cell capacity (TW Solar) CONSUMES poly, so a higher poly price raises its own cell-segment input cost, partially hedging the gain. Net exposure historically positive because merchant-poly economics swamp the captive-cell drag, but integration mutes sensitivity vs a pure-play. Curator likely pins +1 with reduced magnitude.",
      "strength": 0.85,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "World's largest polysilicon producer AND a top solar-cell maker (integrated); also has a 饲料 segment. Poly is a dominant earnings driver; the captive cell business is a partial internal hedge — net long poly price but less geared than a pure-play. The integration is the key nuance to encode. Verified: graph node 600438 = subindustry polysilicon, 'DIVERSIFIED (硅料 + 电池 + 饲料)'.",
      "evidence": "Tongwei (通威) is consistently ranked the largest global polysilicon producer by capacity and is simultaneously a leading solar-cell manufacturer (TW Solar / 通威太阳能). The dual role is why its poly-price sensitivity is net positive but partly self-hedged. Roster-confirmed: graph node 600438.SH subindustry_tag=polysilicon (diversified).",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 600438.SH)"
    },
    {
      "source": "COMM:POLYSILICON",
      "target": "601012.SH",
      "target_name": "隆基绿能",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "PROPOSED −1 (downstream-cost, absent full pass-through): LONGi is a wafer+module maker that consumes polysilicon as its primary feedstock. Higher poly price raises wafer/module COGS; if ASPs do not pass through fully (the usual case in a competitive, oversupplied module market), margin compresses → −1. Conditional +1 only where LONGi holds low-cost poly inventory/contracts into a rising-price environment and can widen spread, but the durable sign is −1. Curator pins −1. (NB the graph node flags 隆基 sits on BOTH sides of the 硅料-price inversion via its own 硅片 margin — a second-order nuance the curator may weigh.)",
      "strength": 0.8,
      "revenue_share": 0.35,
      "hop_class": 1,
      "materiality_note": "Polysilicon is the dominant non-glass raw-material cost in the wafer/module stack. Silicon's share of module cost is highly cyclical — roughly 30-50%+ at the wafer/cell stage depending on the poly-price cycle (peaked in the 2021-22 shortage, collapsed 2023-24). revenue_share is an order-of-magnitude COGS fraction, not a precise figure. Verified: graph node 601012 = subindustry pv_module, '硅片+组件 integrated'.",
      "evidence": "LONGi (隆基绿能) is the world's largest monocrystalline wafer maker and a top module producer; polysilicon is the feedstock for its wafers. Silicon material being the single largest non-glass input cost in the wafer→module chain is uncontested. COGS share given as a range to avoid a fabricated point estimate. Roster-confirmed: graph node 601012.SH subindustry_tag=pv_module.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 601012.SH)"
    },
    {
      "source": "COMM:POLYSILICON",
      "target": "002459.SZ",
      "target_name": "晶澳科技",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "PROPOSED −1 (downstream-cost, absent full pass-through): JA Solar is a vertically-integrated module maker for whom polysilicon (directly and via wafers) is the dominant non-glass COGS. Rising poly price raises module cost; without full ASP pass-through margin compresses → −1. Conditional +1 only on favorable poly-inventory timing in a rising market. Durable sign −1; curator pins −1.",
      "strength": 0.78,
      "revenue_share": 0.35,
      "hop_class": 1,
      "materiality_note": "Integrated module maker; poly is the dominant non-glass module COGS. Same cyclical 30-50%+ silicon-cost band as the rest of the module group. revenue_share is an order-of-magnitude estimate. Verified: graph node 002459 = subindustry pv_module, '组件 leader'.",
      "evidence": "JA Solar (晶澳科技) is a top-tier integrated PV module manufacturer (wafer/cell/module); polysilicon is the foundational feedstock. Module-maker poly cost exposure is well-established industry structure. Roster-confirmed: graph node 002459.SZ subindustry_tag=pv_module.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002459.SZ)"
    },
    {
      "source": "COMM:POLYSILICON",
      "target": "688599.SH",
      "target_name": "天合光能",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "PROPOSED −1 (downstream-cost, absent full pass-through): Trina Solar is a module maker consuming polysilicon (directly and embedded in wafers/cells). Higher poly price raises COGS; absent full ASP pass-through, margin compresses → −1. Conditional +1 only on favorable inventory/contract timing. Durable sign −1; curator pins −1.",
      "strength": 0.78,
      "revenue_share": 0.35,
      "hop_class": 1,
      "materiality_note": "Top-tier integrated module maker; poly is the dominant non-glass module COGS, same cyclical 30-50%+ band. revenue_share is an order-of-magnitude estimate. Verified: graph node 688599 = subindustry pv_module, '组件 leader (科创板 ±20%)'.",
      "evidence": "Trina Solar (天合光能) is a leading global PV module manufacturer; polysilicon is its core feedstock via the wafer/cell stack. Standard, well-established module-chain cost exposure. Roster-confirmed: graph node 688599.SH subindustry_tag=pv_module.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688599.SH)"
    },
    {
      "source": "COMM:POLYSILICON",
      "target": "688223.SH",
      "target_name": "晶科能源",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "PROPOSED −1 (downstream-cost, absent full pass-through): JinkoSolar is a module maker consuming polysilicon. Higher poly price raises module COGS; without full ASP pass-through margin compresses → −1. Conditional +1 only on favorable poly-inventory timing in a rising market. Durable sign −1; curator pins −1.",
      "strength": 0.78,
      "revenue_share": 0.35,
      "hop_class": 1,
      "materiality_note": "Top-tier integrated module maker; poly is the dominant non-glass module COGS, same cyclical 30-50%+ band. revenue_share is an order-of-magnitude estimate. Verified: graph node 688223 = subindustry pv_module, '组件 leader (科创板 ±20%)'.",
      "evidence": "JinkoSolar (晶科能源) is a leading global PV module manufacturer with vertically-integrated wafer/cell/module operations; polysilicon is the foundational feedstock. Well-established industry structure. Roster-confirmed: graph node 688223.SH subindustry_tag=pv_module.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688223.SH)"
    },
    {
      "source": "COMM:POLYSILICON",
      "target": "002865.SZ",
      "target_name": "钧达股份",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "PROPOSED −1 (downstream-cost, absent full pass-through), ONE STEP REMOVED: Jinko Junda is a dedicated solar-cell maker — it buys WAFERS (which already embed polysilicon) rather than poly directly, so the exposure is one transformation step removed but still material (silicon cost dominates the wafer it purchases). Higher poly price raises wafer cost → raises cell COGS; absent pass-through to cell ASP, margin compresses → −1. Weaker/less direct than a poly buyer. Curator pins −1 with reduced magnitude. NOTE: exposure is genuinely wafer-mediated (effectively hop ~1.5); treat the hop_class=1 tag as a directness flag, not a literal direct-purchase claim.",
      "strength": 0.55,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Pure-play solar-CELL maker (does not make poly). Poly exposure is transmitted via the price of purchased wafers, where silicon is the dominant cost — real and material but one step removed and buffered by the cell processing margin. Strength trimmed 0.62→0.55 to reflect the indirection (wafer-mediated, plus partial cost pass-through in wafer contracts). revenue_share left null — poly is not a directly-purchased line item for a cell maker. Verified: graph node 002865 = subindustry solar_cell, 'TOPCon 电池片 pure-play'.",
      "evidence": "Junda (钧达股份) is a specialist solar-cell manufacturer that purchases silicon wafers as its main input; polysilicon is the dominant cost embedded in those wafers. Cell-maker poly exposure being wafer-mediated is standard PV-chain structure. Roster-confirmed: graph node 002865.SZ subindustry_tag=solar_cell.",
      "confidence": "medium",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002865.SZ)"
    },
    {
      "source": "COMM:POLYSILICON",
      "target": "600732.SH",
      "target_name": "爱旭股份",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "PROPOSED −1 (downstream-cost, absent full pass-through), ONE STEP REMOVED: Aiko is a dedicated solar-cell maker (incl. ABC/back-contact cells) that buys WAFERS embedding polysilicon rather than poly directly. Higher poly price raises wafer cost → raises cell COGS; without pass-through to cell ASP, margin compresses → −1. Exposure is one transformation step removed and buffered by cell margin. Curator pins −1 with reduced magnitude. NOTE: genuinely wafer-mediated (effectively hop ~1.5); hop_class=1 is a directness flag, not a direct-purchase claim.",
      "strength": 0.55,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Pure-play solar-CELL maker (does not make poly). Poly exposure transmitted via purchased-wafer prices, where silicon is the dominant cost — real and material but indirect and buffered by the cell processing margin. Strength trimmed 0.62→0.55 to reflect the wafer-mediation and partial pass-through. revenue_share left null — poly is not a directly-purchased line item for a cell maker. Verified: graph node 600732 = subindustry solar_cell, '电池片 — BC (ABC/xBC) franchise'.",
      "evidence": "Aiko Solar (爱旭股份) is a specialist solar-cell manufacturer purchasing silicon wafers as its primary input; polysilicon is the dominant embedded cost in those wafers. Standard wafer-mediated cell-maker exposure. Roster-confirmed: graph node 600732.SH subindustry_tag=solar_cell.",
      "confidence": "medium",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 600732.SH)"
    },
    {
      "source": "COMM:NICKEL",
      "target": "688005.SH",
      "target_name": "容百科技",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Curator to pin. 容百 is a ternary-cathode BUYER of nickel (not a producer), so the natural pin is -1 for 容百 absent full pass-through: nickel (delivered as nickel sulfate -> NCM/NCA precursor) is the single largest metal-cost component in high-nickel cathode, so rising nickel compresses gross margin in the window before price is passed through. Counter-direction (+1) applies only under metal-linked / cost-plus '金属价+加工费'-style pricing, where higher nickel mechanically inflates pass-through revenue and produces inventory gains in a rising market; A-share ternary cathode contracts commonly carry PARTIAL metal-price linkage, which dampens but rarely fully neutralizes the cost shock, so the lag/regime determines which polarity dominates. Curator decides given the prevailing pass-through regime.",
      "strength": 0.78,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "容百 is a pure-play high-nickel ternary (NCM/NCA) cathode leader; high-nickel chemistries (NCM8-series/NCA) are its core product, making nickel its most-exposed single metal input via the nickel-sulfate -> 前驱体 -> cathode BOM path. High strength (0.78) reflects pure-play status. revenue_share left null deliberately: exact nickel COGS fraction NOT fabricated. Verified: KB graph-new_energy-v0.1.json node 688005 = subindustry 'cathode', note '三元正极 leader'. (Distinct from roster's 301358 湖南裕能 LFP, which has NO nickel.) Residual caveat the curator should weigh: partial cost-plus pass-through and 容百's gradual mix diversification (LMFP/钠电/Mn-rich exploration) can dilute sensitivity at the margin, but core revenue remains high-nickel ternary.",
      "evidence": "容百科技 (688005) is the leading A-share high-nickel ternary (NCM/NCA) cathode producer; ternary cathode is made from ternary precursor (前驱体) whose dominant metal input is nickel delivered as nickel sulfate (硫酸镍). High-nickel chemistries by definition maximize nickel content, so nickel price is the primary metal-cost swing factor for this product line. KB graph-new_energy-v0.1.json node 688005 describes it as '三元正极 leader' (subindustry_tag cathode), confirming the type. Exact COGS fraction not asserted to avoid fabricating a figure.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688005.SH)"
    },
    {
      "source": "COMM:NICKEL",
      "target": "300073.SZ",
      "target_name": "当升科技",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Curator to pin. 当升 is a ternary-cathode BUYER of nickel, so the natural pin is -1 for 当升 absent full pass-through: nickel sulfate flows through ternary precursor into its NCM/NCA cathode and is a major metal-cost component, compressing margin on a price spike before contractual pass-through catches up. (+1) applies only under metal-linked/cost-plus pricing where rising nickel lifts pass-through revenue and inventory value. Materiality qualifier vs 容百: 当升's product mix includes 磷酸铁锂 (LFP), which contains NO nickel, so a portion of output is unexposed and its BLENDED nickel sensitivity is diluted relative to a pure-play ternary maker. Curator pins dominant polarity given pass-through regime and the ternary share of mix.",
      "strength": 0.62,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "当升 produces ternary (三元) cathode, giving a direct nickel-sulfate-via-precursor exposure on the same BOM path as 容百. KB node note flags it also makes 磷酸铁锂 (LFP), which is nickel-free, so overall nickel sensitivity is material but PARTIAL/diluted — hence a correctly lower strength (0.62) than pure-play 容百 (0.78). revenue_share null: precise nickel COGS fraction not fabricated, and is blended down by the LFP portion of mix. Verified: KB graph-new_energy-v0.1.json node 300073 = subindustry 'cathode', note '正极 (三元 + 磷酸铁锂)' — confirms BOTH the real ternary/nickel exposure AND the nickel-free LFP dilution.",
      "evidence": "当升科技 (300073) is an A-share cathode maker whose product line includes ternary (NCM/NCA) cathode, which consumes nickel sulfate via ternary precursor. KB graph-new_energy-v0.1.json node 300073 explicitly notes scope as '正极 (三元 + 磷酸铁锂)', confirming a real ternary/nickel exposure AND a nickel-free LFP segment that dilutes blended sensitivity. Exact COGS share not asserted to avoid fabrication.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300073.SH)"
    },
    {
      "source": "COMM:COBALT",
      "target": "688005.SH",
      "target_name": "容百科技",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Conditional polarity for the high-nickel NCM-cathode maker; 容百 is a cathode BUYER of cobalt (via 硫酸钴 precursor), NOT a cobalt seller, so the lithium-miner-style +1 'price IS revenue' logic does NOT apply. (a) COST-channel, -1: a cobalt price rise lifts ternary-cathode COGS and compresses 容百's unit margin TO THE EXTENT the move is NOT recovered from customers. (b) PASS-THROUGH / margin-neutral, ~0 net: China ternary-cathode commercial terms are predominantly metal-price-linked cost-plus (金属价格联动 + 加工费), so most of the cobalt move flows straight to the downstream customer and the processing fee (加工费) is the true steady-state margin driver -> net P&L sensitivity is muted. (c) INVENTORY-revaluation, ±: a sharp cobalt move can mark up low-cost metal/precursor inventory on a rising tape (+) or force a write-down on a falling tape (-), independent of steady-state pass-through. Curator pins which channel dominates for the studied horizon.",
      "strength": 0.5,
      "revenue_share": 0.25,
      "hop_class": 1,
      "materiality_note": "Cobalt is a genuine BOM line for NCM cathode but secondary to nickel and lithium by cost, and 容百 specializes in HIGH-nickel chemistry (NCM811 / 9-series) where the cobalt fraction is at the LOWER end of the honest ~15-35% of cathode-metals-cost range. revenue_share 0.25 is a sell-side-grade COGS-fraction ESTIMATE (not disclosed) and approximate. Net equity sensitivity is materially dampened by cost-plus 加工费 pass-through -> strength held at mid (0.5), not high. Consistent with the house P11 commodity-stock-map.yaml, which lists ONLY cobalt MINERS (华友钴业/寒锐钴业/洛阳钼业/格林美) under `cobalt` (not cathode makers) precisely because the cathode-maker net price-sensitivity is muted; this raw_material edge is the complementary BOM-cost view, honestly down-weighted.",
      "evidence": "Cobalt is the 'C' in NCM (nickel-cobalt-manganese) ternary cathodes; cobalt sulfate (硫酸钴) is the standard cobalt-bearing precursor input. 容百科技 is a leading Chinese high-nickel NCM cathode maker (chain graph node: 三元正极 leader, SW2021 电池 801737.SW). Chinese ternary-cathode commercial terms are widely structured as metal-price-linked cost-plus processing-fee (加工费) contracts, so raw-metal moves are largely passed downstream; exact per-name pass-through ratio and cobalt COGS share are not publicly disclosed.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688005.SH); config/commodity-stock-map.yaml (cobalt: miners-only list 华友/寒锐/洛阳钼业/格林美)"
    },
    {
      "source": "COMM:COBALT",
      "target": "300073.SZ",
      "target_name": "当升科技",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Same conditional structure as 容百, but 当升's net cobalt intensity is DILUTED by a meaningful LFP (磷酸铁锂) segment that contains NO cobalt. 当升 is a cathode BUYER of cobalt, not a seller -> no +1 'price-IS-revenue' leg. (a) COST-channel, -1: higher cobalt raises COGS on 当升's TERNARY (NCM/NCA) line and squeezes unit margin only to the extent not recovered from customers; the LFP line is unaffected. (b) PASS-THROUGH / margin-neutral, ~0 net: 当升 sells ternary under metal-price-linked cost-plus terms (加工费 is the margin), so the bulk of a cobalt move transmits to the buyer and steady-state P&L sensitivity is small. (c) INVENTORY-revaluation, ±: sharp cobalt moves drive one-off inventory gains (rising) or write-downs (falling) on the ternary-precursor stock. Curator pins the dominant channel.",
      "strength": 0.4,
      "revenue_share": 0.18,
      "hop_class": 1,
      "materiality_note": "FIXED DOWN from candidate's 0.5/0.25. 当升 is NOT a pure-ternary maker: the roster and house chain-graph node both flag a 三元 + 磷酸铁锂 (LFP) product mix, and the LFP segment has ZERO cobalt. Group-level cobalt COGS share and net sensitivity are therefore lower than for pure-ternary 容百, so strength 0.4 and revenue_share ~0.18 (group-blended COGS-fraction estimate, sell-side-grade, not disclosed). Cobalt remains secondary to nickel/lithium even within the ternary line. Net sensitivity further dampened by cost-plus pass-through.",
      "evidence": "当升科技 is a major Chinese ternary (NCM/NCA) cathode producer that ALSO makes LFP cathode (roster sub: cathode (ternary/NCM); house chain-graph node 300073.SH notes '正极 (三元 + 磷酸铁锂)'). Cobalt (via 硫酸钴) is an intrinsic input to its nickel-cobalt-manganese line but absent from its LFP line. Like the rest of the Chinese ternary-cathode segment its customer contracts are broadly metal-price-linked cost-plus (加工费) structures, passing most raw-metal moves downstream. Exact per-name pass-through and cobalt COGS share are not publicly disclosed.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300073.SH: '正极 (三元 + 磷酸铁锂)')"
    },
    {
      "source": "COMM:LIPF6",
      "target": "002407.SZ",
      "target_name": "多氟多",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "PRODUCER-REVENUE leg. Propose +1 for 多氟多: LiPF6 (六氟磷酸锂, 6F) is one of its flagship products, so the 6F market price IS its selling price / revenue line — a 6F price spike lifts revenue and margin (and the 2021-22 6F super-cycle drove its earnings; the post-2022 collapse compressed them). This is the cleanest producer-side +1 in the LiPF6 chain. NOTE the curator should weigh that 多氟多 is DIVERSIFIED (also 电子级氢氟酸/电子化学品, 锂电池, 新材料), so 6F is a material but not whole-name driver — a +1 on the 6F line is real yet partial. The human curator pins the sign; this is a proposal, not a pin.",
      "strength": 0.7,
      "revenue_share": null,
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002407.SZ)",
      "hop_class": 1,
      "materiality_note": "002407 多氟多 is a (the) leading domestic LiPF6 producer; 6F is a flagship revenue line, NOT a cost. Producer-side exposure: 6F price = its ASP. Diversified across 氟化工/电子化学品/锂电, so 6F is material-but-partial to the consolidated name. SW2 classified 化学制品 801034.SW (氟化工), not 电池 (confirmed in graph node 002407). revenue_share=null — no segment % cited (avoid fabrication); honestly a meaningful minority-to-substantial fraction depending on 6F price regime. VERIFIED: no type error — this is correctly the producer-revenue leg, not a cost leg; complementary to the LITHIUM_CARBONATE feedstock-cost edge for the same code.",
      "evidence": "Well-known A-share supply-chain fact: 多氟多 (002407) is one of China's largest lithium hexafluorophosphate (六氟磷酸锂 / 6F) producers; LiPF6 is a named product line and its earnings were highly geared to the 2021-2022 6F price super-cycle (6F spot rose from ~10万元/吨 to a 2022 peak well above 50万元/吨, then collapsed below ~10万元/吨 by 2023-24). Exact segment revenue % not cited here to avoid fabricating a figure. Roster-confirmed: graph node 002407.SZ subindustry_tag=lithium_hexafluorophosphate.",
      "confidence": "high"
    },
    {
      "source": "COMM:LIPF6",
      "target": "002709.SZ",
      "target_name": "天赐材料",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "INTEGRATED-PRODUCER leg — basis differs MATERIALLY from a pure electrolyte buyer (this is the chain's key distinction). 天赐 is the electrolyte leader but is BACK-INTEGRATED into 6F (large captive solid + liquid LiPF6 capacity), so the LiPF6 market price is largely an INTERNAL TRANSFER, not a pure external cost. Propose treating this NOT as a clean cost-side −1: when 6F price rises, 天赐 captures producer-side margin on its self-supplied 6F that offsets the higher electrolyte input cost (a natural hedge / vertical-integration moat). So the net sign is ambiguous and closer to producer-like-than-cost-taker — leaning mildly + or roughly neutral on a 6F spike, the OPPOSITE of a pure buyer's −1. The curator should explicitly pin this differently from 新宙邦's cost-taker −1; that contrast is the whole point of carrying both edges. Sign stays ± pending curator pin.",
      "strength": 0.55,
      "revenue_share": null,
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002709.SZ)",
      "hop_class": 1,
      "materiality_note": "002709 天赐材料 is the 电解液 leader AND integrated into 6F (liquid LiPF6 self-supply). LiPF6 is the dominant cost component of electrolyte, BUT because 天赐 makes its own, the external-price exposure is materially BLUNTED vs a buyer — vertical integration converts most of the 6F cost line into an internal transfer + producer margin. Basis is hedged / producer-leaning, NOT cost-taker −1. This is exactly why it must be encoded distinctly from 新宙邦. revenue_share=null (electrolyte BOM share known qualitatively, captive offset not cited as a hard %). VERIFIED against graph node 002709 which states '电解液 leader, integrated into 6F (六氟磷酸锂) — partial overlap with 多氟多.' Same code also appears under LITHIUM_CARBONATE (feedstock-cost two-hop view) — distinct edges.",
      "evidence": "Well-known A-share supply-chain fact: 天赐材料 (002709) is the domestic electrolyte market leader and is notably vertically integrated into lithium hexafluorophosphate — it pioneered large-scale LIQUID LiPF6 self-supply, giving it among the highest 6F self-sufficiency in the industry. The existing graph node note already flags '电解液 leader, integrated into 6F (六氟磷酸锂) — partial overlap with 多氟多.' This integration is the textbook reason its 6F exposure is structurally different from a pure electrolyte buyer.",
      "confidence": "high"
    },
    {
      "source": "COMM:LIPF6",
      "target": "300037.SZ",
      "target_name": "新宙邦",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "COST-TAKER leg — the clean downstream-cost case. Propose −1 for 新宙邦 ABSENT FULL PASS-THROUGH: it is an electrolyte maker that primarily BUYS LiPF6 (lower 6F self-supply than the integrated 天赐), so 6F is a genuine external raw-material cost. LiPF6 is the single largest cost component of electrolyte (commonly cited at roughly ~40-60% of electrolyte material cost, varying strongly with the 6F price regime — higher share when 6F spikes), so a 6F price spike compresses electrolyte gross margin to the extent it cannot be passed to battery-cell customers; a 6F price fall RELIEVES cost (margin tailwind) — i.e. −1 to the input price. The pass-through caveat is load-bearing: if electrolyte ASP fully indexes to 6F (common in long-term cell contracts), the sign attenuates toward 0; in a price war with weak pass-through the −1 bites. Contrast with 天赐: same chain position, OPPOSITE net basis because 新宙邦 lacks the captive-6F hedge. Curator pins the sign.",
      "strength": 0.55,
      "revenue_share": 0.5,
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300037.SZ)",
      "hop_class": 1,
      "materiality_note": "300037 新宙邦 is an electrolyte maker that mainly PURCHASES LiPF6 (not integrated like 天赐), so 6F is a real external COGS input — the largest single material cost of electrolyte. revenue_share≈0.5 is an HONEST RANGE-MIDPOINT for LiPF6 as a fraction of ELECTROLYTE-SEGMENT material COST (commonly ~40-60%, regime-dependent), NOT a fraction of total company revenue/COGS — 新宙邦 also has 氟化工/电容化学品/半导体化学品 segments diluting the whole-name 6F-COGS share BELOW this electrolyte-only figure (graph node 300037 confirms 新宙邦 carries 氟化工/电容化学品). strength=0.55 (below the 0.5 electrolyte-segment COGS share would imply at full concentration) appropriately reflects that whole-name dilution. Cost-taker −1 absent pass-through; attenuates if ASP indexes to 6F. VERIFIED: no type error — correct cost leg for a 6F buyer, sign genuinely opposite to 天赐's hedged basis. Roster-confirmed: graph node 300037 = subindustry electrolyte.",
      "evidence": "Well-known electrolyte BOM fact: lithium hexafluorophosphate (LiPF6 / 6F) is the highest-value and largest single cost component of lithium-ion battery electrolyte — industry-cited at roughly 40-60% of electrolyte material cost, rising as a share when 6F prices spike (e.g. 2021-22). 新宙邦 (300037) is a leading electrolyte maker with materially LOWER 6F self-supply than the integrated 天赐, so it is structurally a 6F price-taker on the cost side. Exact pass-through and self-supply ratios vary by year/contract; share given as an honest range, not a pinned figure.",
      "confidence": "high"
    },
    {
      "source": "COMM:NEEDLE_COKE",
      "target": "603659.SH",
      "target_name": "璞泰来",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "璞泰来 is a coke BUYER (artificial-graphite anode maker), not a coke producer — no producer-revenue leg exists for this roster name. Dominant polarity is the COST side: −1 for 璞泰来 when needle/petroleum coke prices rise absent full pass-through, because coke is the principal carbon precursor for artificial graphite anodes (industry-cited at roughly one-third to one-half of anode MATERIAL cost, with graphitization electricity the other major cost bucket). Sign flips to +1 only on successful cost pass-through to cell customers (CATL/BYD etc.), which is sticky and lagged on long-term supply contracts. Net: a gross-margin-compression channel, not a revenue channel.",
      "strength": 0.65,
      "revenue_share": 0.4,
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 603659.SH)",
      "hop_class": 1,
      "materiality_note": "FIXED: anode/负极 materials is 璞泰来's DOMINANT but not sole segment — it also has separator coating/base-film, lithium-ion coating materials, and automation-equipment businesses, so the original 'near pure-play' framing is slightly overstated. Coke is the primary raw material for its graphite anodes; the secondary in-segment driver is graphitization power, so coke alone is not 100% of anode COGS. revenue_share=0.4 is an HONEST mid-point of coke's share of anode MATERIAL cost — treat as a ~30-50% range, not a precise figure. strength trimmed 0.70→0.65 to reflect modest non-anode dilution while keeping it the highest-exposure roster name to this commodity. Verified: graph node 603659 = subindustry anode, '负极 leader'.",
      "evidence": "Artificial graphite anodes (the dominant anode chemistry for Chinese cells) are produced from needle coke or petroleum coke as the carbon precursor, followed by graphitization; coke is widely recognized as the principal raw-material input to graphite anodes, with graphitization electricity the other major cost. 璞泰来 is one of China's largest dedicated graphite-anode producers, with anode materials its largest revenue segment. Roster-confirmed: graph node 603659.SH subindustry_tag=anode.",
      "confidence": "high"
    },
    {
      "source": "COMM:NEEDLE_COKE",
      "target": "600884.SH",
      "target_name": "杉杉股份",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Same cost-side logic as the anode peer: 杉杉 is a coke BUYER, not a producer, so no producer-revenue leg. −1 for 杉杉's anode segment when coke prices rise absent pass-through (coke is the primary precursor for its graphite anodes); +1 only on successful, lagged cost pass-through to cell customers. KEY DIFFERENCE vs 璞泰来: 杉杉 is DIVERSIFIED — it also runs a large LCD polarizer-film (偏光片) business with ZERO coke exposure — so consolidated/full-name sensitivity to coke is materially diluted and a coke move must NOT be read as a full-company signal.",
      "strength": 0.45,
      "revenue_share": null,
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 600884.SH)",
      "hop_class": 1,
      "materiality_note": "杉杉股份's anode (负极) business has the same direct coke dependence as 璞泰来, but at the consolidated/full-name level exposure is diluted by its sizeable non-battery polarizer-film segment. strength held at 0.45 (vs 璞泰来's 0.65) to reflect that dilution. revenue_share left null because coke's share of TOTAL company COGS is not estimable given the multi-segment mix — within the anode segment alone it is comparable to the ~30-50% precursor range, but no whole-company figure is asserted. Verified: graph node 600884 = subindustry anode, '负极 + 偏光片 — DIVERSIFIED'.",
      "evidence": "杉杉股份 operates a major graphite-anode (负极) business that, like all artificial-graphite anode makers, uses needle/petroleum coke as its primary carbon precursor; the company also has a large LCD polarizer-film segment unrelated to batteries, making it a diversified name where anode-input shocks transmit only partially to the consolidated result. Roster-confirmed: graph node 600884.SH subindustry_tag=anode (diversified, 偏光片 flagged).",
      "confidence": "high"
    },
    {
      "source": "COMM:SODA_ASH",
      "target": "601865.SH",
      "target_name": "福莱特",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Conditional, for the curator to pin. 福莱特 is a PV-glass BUYER of soda ash, not a producer, so only the cost-side leg exists: PROPOSE −1 for 福莱特 when soda-ash prices rise absent full pass-through (soda ash is the principal NON-energy raw material in the 光伏玻璃 melt, so a price spike compresses gross margin), and symmetric +1 (margin tailwind) when soda ash falls. The pass-through condition is the gate: PV-glass ASP is set on its OWN duopoly capacity/demand cycle (with 信义光能 HK, tracked weekly), so cost relief/burden reaches the P&L only to the extent the glass cycle is loose/tight enough to (not) pass it through — when glass is tight and pricing power is high, cost moves are largely passed through and the margin sensitivity attenuates; when glass is loose/oversupplied, the buyer eats it and the −/+ sign bites hardest. There is NO producer-revenue (+1) leg here because no roster name produces soda ash. Curator pins the sign and the regime weighting.",
      "strength": 0.5,
      "revenue_share": 0.2,
      "hop_class": 1,
      "materiality_note": "Moderate, margin-channel (NOT revenue). Soda ash is a direct, genuine batch input to 光伏玻璃 (real glass chemistry: silica + soda ash + carbonate flux), and is the single largest NON-energy raw material in the glass melt. As a near-pure-play PV-glass leader, 福莱特's gross margin is genuinely sensitive to soda-ash price swings. But the effect is second-order to (a) the PV-glass price cycle itself and (b) natural-gas/energy cost (typically the single largest cost line), so materiality is moderate, not dominant. Corrected vs candidate: trimmed revenue_share 0.25->0.20 and strength 0.55->0.50 — the candidate's 0.25 sat at the optimistic top of the honest range and mixed the raw-material-cost denominator with the COGS denominator; soda ash is closer to ~15-25% of TOTAL manufacturing cost (COGS), mid ~0.20, not 0.25.",
      "evidence": "Well-established industry fact: the PV-glass (光伏玻璃) furnace batch is dominated by 石英砂 (silica/quartz sand) and 纯碱 (soda ash), melted with natural gas; soda ash is the principal non-energy raw material and the standard glass-making flux that lowers silica's melting point. Sell-side/industry cost decompositions commonly place soda ash at roughly 20-35% of PV-glass RAW-MATERIAL cost or ~15-25% of TOTAL manufacturing cost — given as an honest range (exact share varies with energy mix, quartz cost, and the soda-ash price level), NOT a pinned figure. 福莱特 (601865.SH) is a dedicated PV-glass leader (duopoly with 信义光能 HK), so this commodity flows straight into COGS. Corroborated by the project's own new-energy graph (graph-new_energy-v0.1.json), which tags 601865 subindustry_tag='pv_glass' / '光伏玻璃 leader … 组件 BOM; own price cycle (price-weekly tracked)', and by config/commodity-stock-map.yaml CONTENT GAP §F, which explicitly recognizes 纯碱/soda ash and 玻璃 as deferred commodity classes.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 601865.SH); config/commodity-stock-map.yaml (CONTENT GAP §F: 纯碱/玻璃 deferred)"
    },
    {
      "source": "COMM:EVA_POE_RESIN",
      "target": "603806.SH",
      "target_name": "福斯特",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "福斯特 is a downstream CONSUMER of EVA/POE resin (粒子), not a producer, so the cost-side polarity dominates: −1 for 福斯特 when resin prices rise AND pass-through to film ASP is incomplete/lagged (resin is the overwhelming-majority COGS of encapsulant film, so a margin squeeze is the default short-horizon read). The +1 leg applies only conditionally: if 福斯特 fully or over-passes resin cost into film price (it is the >50%-share film leader with pricing power and largely cost-plus contracts that re-price on a lag), rising resin can be margin-neutral or even widen nominal spread, and falling resin can compress ASP faster than COGS. Net: margin/timing-driven, predominantly an inverse cost exposure with pass-through completeness/lag the swing factor — curator to pin direction.",
      "strength": 0.85,
      "revenue_share": 0.75,
      "hop_class": 1,
      "materiality_note": "EVA/POE resin (粒子) is the single dominant raw material in solar encapsulant film and by far the largest component of 福斯特's COGS. Cited resin-share-of-film-COGS spans a wide band — Western trade sources put the EVA portion at ~60-70% of production cost, while CN annual-report-based sources put total direct material (EVA+POE) near ~85-90%; 0.75 is a defensible mid-band estimate. Film margins are highly sensitive to the resin price cycle and to the lag between resin moves and film ASP re-pricing; this is the textbook pass-through margin node of the PV auxiliary-materials chain. POE in particular is import/oligopoly-constrained (三井化学/LG化学/陶氏), amplifying input-cost and margin volatility. Empirically validated: 2023 EVA price swings of ~±40% directly compressed film-maker profits and 福斯特 net profit fell ~29% in 2024 despite >50% share. Verified: graph node 603806 = subindustry encapsulant_film, 'EVA/POE 树脂 price pass-through'.",
      "evidence": "福斯特 is the dominant global solar encapsulant film maker (光伏胶膜 leader, >50% global share). Encapsulant film is manufactured from EVA and POE resin pellets, which constitute the overwhelming majority of film bill-of-materials cost — sources range from ~60-70% (EVA portion, Western trade research) to ~85-90% (total direct material incl. POE, CN annual-report sources); honest band, exact share varies by EVA-vs-POE mix and period. POE resin is supply-tight and largely imported from a small oligopoly of petrochemical producers (三井化学/LG化学/陶氏), making 福斯特's input cost and gross margin closely tracked against the resin price cycle. Internal chain graph (graph-new_energy-v0.1.json) independently encodes 603806.SH subindustry_tag=encapsulant_film with note 'EVA/POE 树脂 price pass-through'.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 603806.SH)"
    },
    {
      "source": "COMM:COPPER",
      "target": "300750.SZ",
      "target_name": "宁德时代",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "For the cell maker, copper is a COST input via copper foil (anode current collector), so the conditional polarity is −1 on margin when copper rises absent pass-through; copper foil is ~8-10% of cell cost, a modest single-digit COGS line. Copper-foil converters (嘉元/诺德) price on a processing-fee + LME-copper pass-through basis, so the cell maker effectively bears most of the copper move; pass-through to OEM/auto customers is partial and lagged, so a sustained copper spike compresses margin in the gap before contracts reset, and the sign flips toward neutral once they reprice. Curator to pin direction.",
      "strength": 0.35,
      "revenue_share": 0.08,
      "hop_class": 1,
      "materiality_note": "Modest: copper foil ~8-10% of cell COGS — a minority cost line dwarfed by cathode/lithium. Largest cell maker so absolute copper tonnage is huge, but as a % of its diversified COGS it remains single-to-low-double digit. Strength trimmed from 0.4 to 0.35 so a sub-10% COGS input is not overweighted relative to the lithium/cathode story. Same code also carries the flagship LITHIUM_CARBONATE edge — distinct, complementary cost lines.",
      "evidence": "Copper foil serves as the anode current collector in Li-ion cells and is widely cited at ~10-13% of cell mass and ~8-10% of cell cost (industry references on lithium-battery copper foil). 嘉元科技 and 诺德股份 are well-known copper-foil suppliers into CATL, and copper-foil contracts are typically processing-fee + copper pass-through. Exact % varies by chemistry/format and copper price; the 8-10% is an honest industry range, not a firm figure. Roster-confirmed: graph node 300750.SH subindustry_tag=battery_cell.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300750.SZ)"
    },
    {
      "source": "COMM:COPPER",
      "target": "300014.SZ",
      "target_name": "亿纬锂能",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Same channel as CATL: copper foil is the anode current collector, a COST input → −1 on margin when copper rises absent full pass-through; copper foil ~8-10% of cell cost. Converters price processing-fee + copper pass-through, so the cell maker bears the copper move; pass-through to customers is partial/lagged and the sign neutralizes once contracts reprice. Curator pins direction.",
      "strength": 0.38,
      "revenue_share": 0.08,
      "hop_class": 1,
      "materiality_note": "Modest single-digit COGS fraction via copper foil. Consumer + power + storage cell mix; copper foil exposure applies across all Li-ion formats. Minority cost line relative to lithium/cathode. Same code also carries the LITHIUM_CARBONATE edge — distinct.",
      "evidence": "亿纬锂能 is a major Li-ion cell maker (power, consumer, storage); all its Li-ion cells use copper foil as the anode current collector, the ~8-10%-of-cost industry range. Honest range, not a firm per-company figure. Roster-confirmed: graph node 300014.SZ subindustry_tag=battery_cell.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300014.SZ)"
    },
    {
      "source": "COMM:COPPER",
      "target": "002074.SZ",
      "target_name": "国轩高科",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Copper foil as anode current collector is a COST input → −1 on margin when copper rises absent pass-through; ~8-10% of cell cost. 国轩 is LFP-heavy; copper-foil intensity is largely chemistry-independent (the collector is copper regardless of cathode chemistry), so exposure is similar to peers. Partial/lagged pass-through to auto/storage customers neutralizes the sign over a contract cycle. Curator pins direction.",
      "strength": 0.38,
      "revenue_share": 0.08,
      "hop_class": 1,
      "materiality_note": "Modest. LFP focus does NOT reduce copper-foil exposure (the anode collector is copper regardless of cathode chemistry — correctly avoids a chemistry type-error). Minority cost line vs LFP cathode + lithium carbonate. Same code also carries the LITHIUM_CARBONATE edge — distinct.",
      "evidence": "国轩高科 is a major (LFP-leaning) cell maker; copper foil is the universal anode current collector in Li-ion cells at the ~8-10%-of-cost industry range. Range is honest, not a firm figure. Roster-confirmed: graph node 002074.SZ subindustry_tag=battery_cell.",
      "confidence": "high",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 002074.SZ)"
    },
    {
      "source": "COMM:COPPER",
      "target": "688063.SH",
      "target_name": "派能科技",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "派能 makes its own storage Li-ion cells, which use copper foil as the anode current collector → COST input, −1 on margin when copper rises absent pass-through; ~8-10% of cell cost. As a system integrator too, copper also enters via internal wiring/busbars, marginally. Pass-through to residential-storage customers is slow (channel-priced), so margin sensitivity exists in the gap. Curator pins direction.",
      "strength": 0.32,
      "revenue_share": 0.07,
      "hop_class": 1,
      "materiality_note": "Modest and slightly lower-confidence than the three big cell makers: 派能 is a storage-cell + system maker, so copper foil applies to its in-house cells but a portion of revenue is system-level where copper is a smaller fraction. Minority cost line. Same code also carries the LITHIUM_CARBONATE edge — distinct.",
      "evidence": "派能科技 manufactures lithium iron phosphate storage cells in-house; like all Li-ion cells these use copper foil anode current collectors (~8-10% of cell cost industry range). Honest range. Lower strength reflects its mixed cell/system business vs pure cell makers. Roster-confirmed: graph node 688063.SH subindustry_tag=energy_storage_cell.",
      "confidence": "medium",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688063.SH)"
    },
    {
      "source": "COMM:COPPER",
      "target": "300274.SZ",
      "target_name": "阳光电源",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Copper enters inverters via magnetics windings (transformers/inductors/chokes), DC/AC busbars and internal wiring → COST input, so −1 on margin when copper rises absent pass-through. Copper is a real but modest BOM line (semiconductors/IGBT, magnetic cores, capacitors dominate). 阳光 spans string + central + storage PCS, the larger units carry more copper magnetics/busbar. Pass-through via project pricing is partial; sign neutralizes on order repricing. Curator pins direction.",
      "strength": 0.3,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Modest. Copper is a minority of inverter BOM (power semis + magnetic cores + capacitors larger). Central/large inverters and storage PCS carry more copper (busbars, transformer windings) than string units, slightly raising 阳光's exposure within the modest band. No reliable public single % — left null (correct discipline, not fabricated). Verified: graph node 300274 = subindustry inverter, '逆变器 + 储能PCS + 电站EPC'.",
      "evidence": "Solar inverters use copper extensively in inductor/transformer windings and busbars (copper chosen for low resistivity/cost); busbar conductors are near-universally copper. 阳光电源 is the largest A-share inverter/PCS maker. No trustworthy public copper-COGS % exists per company, so revenue_share is null rather than fabricated. Roster-confirmed: graph node 300274.SZ subindustry_tag=inverter.",
      "confidence": "medium",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300274.SZ)"
    },
    {
      "source": "COMM:COPPER",
      "target": "300763.SZ",
      "target_name": "锦浪科技",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "String-inverter maker: copper in inductor/transformer windings, chokes and internal busbars/wiring → COST input, −1 on margin when copper rises absent pass-through. Modest BOM share (power semis + magnetic cores dominate). Distributor/project pricing gives partial, lagged pass-through; sign neutralizes on repricing. Curator pins direction.",
      "strength": 0.27,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Modest, slightly below 阳光: 锦浪 is string/residential + some storage, so per-unit copper magnetics smaller than central inverters. Minority BOM line. No reliable public % — null. Verified: graph node 300763 = subindustry inverter, '组串逆变器 pure-play'.",
      "evidence": "String solar inverters contain copper-wound inductors/transformers and copper busbars (copper standard for conductors due to conductivity/cost). 锦浪科技 is a leading string-inverter exporter. No credible public copper-COGS % per company; revenue_share left null. Roster-confirmed: graph node 300763.SZ subindustry_tag=inverter.",
      "confidence": "medium",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 300763.SZ)"
    },
    {
      "source": "COMM:COPPER",
      "target": "688390.SH",
      "target_name": "固德威",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "String + hybrid/storage inverter maker: copper in winding magnetics, chokes, busbars and wiring → COST input, −1 on margin when copper rises absent pass-through. Hybrid/storage units add a bit more copper magnetics. Modest BOM share; partial lagged pass-through neutralizes sign over repricing. Curator pins direction.",
      "strength": 0.27,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Modest. Hybrid/storage inverter mix gives slightly more copper-wound magnetics than pure string, but still a minority BOM line behind power semis and magnetic cores. No reliable public % — null. Verified: graph node 688390 = subindustry inverter, '逆变器/储能逆变器'.",
      "evidence": "固德威 makes string and hybrid/storage inverters, which use copper-wound inductors/transformers and copper busbars (copper standard for conductors). No credible public copper-COGS % per company; revenue_share null rather than fabricated. Roster-confirmed: graph node 688390.SH subindustry_tag=inverter.",
      "confidence": "medium",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688390.SH)"
    },
    {
      "source": "COMM:COPPER",
      "target": "605117.SH",
      "target_name": "德业股份",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Storage/hybrid + string inverter maker: copper in transformer/inductor windings, chokes, busbars and wiring → COST input, −1 on margin when copper rises absent pass-through. Storage/hybrid inverters carry meaningful copper magnetics. Modest BOM share; partial lagged pass-through neutralizes sign on repricing. Note 德业 also has a non-inverter (dehumidifier/heat-exchanger) segment with its own copper-tube exposure, reinforcing aggregate copper sensitivity. Curator pins direction.",
      "strength": 0.3,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Modest, comparable to 阳光 within the band: storage/hybrid inverter copper magnetics PLUS a heat-exchange/appliance segment that uses copper tubing, so aggregate copper exposure is a touch broader than pure-inverter peers. Still a minority of total COGS. No reliable public % — null. Verified: graph node 605117 = subindustry inverter, '储能逆变器 + 微逆; HEAVILY EXPORT-levered'.",
      "evidence": "德业股份 is a leading storage/hybrid inverter maker (and also makes heat-exchangers/dehumidifiers using copper tube). Storage inverters use copper-wound magnetics and busbars. No credible public copper-COGS % per company; revenue_share null. Roster-confirmed: graph node 605117.SH subindustry_tag=inverter.",
      "confidence": "medium",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 605117.SH)"
    },
    {
      "source": "COMM:COPPER",
      "target": "688032.SH",
      "target_name": "禾迈股份",
      "edge_type": "raw_material",
      "transmission_sign": "±",
      "proposed_sign_basis": "Microinverter maker: isolated topologies use small copper-wound transformers/inductors → COST input, −1 on margin when copper rises absent pass-through. Per-unit copper is small; microinverter BOM is dominated by control ICs, power semis and PCB. Minor share; partial lagged pass-through neutralizes sign. Curator pins direction.",
      "strength": 0.18,
      "revenue_share": null,
      "hop_class": 1,
      "materiality_note": "Minor — lowest of the inverter set and sits at the materiality floor: microinverters use small copper magnetics but are semiconductor/IC-heavy, so copper is a small BOM fraction. Kept because the channel is genuinely real and the strength is honestly de-rated to minor rather than overstated. No reliable public % — null. Verified: graph node 688032 = subindustry microinverter, '微逆 (microinverter) leader'.",
      "evidence": "Microinverters use isolated transformer topologies (e.g. flyback) with copper windings, but the dominant cost is semiconductors/control electronics. 禾迈股份 is a leading microinverter maker. Copper exposure is genuinely minor; revenue_share null, low strength reflects honest low materiality. Roster-confirmed: graph node 688032.SH subindustry_tag=microinverter.",
      "confidence": "medium",
      "source_ref": "data/operator-feeds/industry-chain/graph-new_energy-v0.1.json (node 688032.SH)"
    }
  ]
}
```
