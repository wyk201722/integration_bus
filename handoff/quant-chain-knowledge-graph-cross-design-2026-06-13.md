# CROSS-MODULE DESIGN PROPOSAL — Chain Knowledge-Graph boundary (quant ↔ KB)

- **Status**: PROPOSAL — cross-design checkpoint. **NO code or contract committed by either side.** This is a bus handoff for the **KB peer to review**. Quant proposes the boundary; quant does NOT commit the KB's half.
- **Date**: 2026-06-13
- **Author**: architect (stock-quant)
- **Scope class**: cross-repo boundary contract → requires (a) KB-peer agreement on their half AND (b) a quant-side ADR + quant-strategist sign-off before any build.
- **Discipline**: follows the ADR-0069 / ADR-0070 **validate-first + firewall** template verbatim (a prettier graph does NOT bypass the R2 gate).
- **Recommended quant ADR (deferred)**: next free number after this freeze (`docs/adrs/` currently ends at ADR-0070; ADR-0071/0072 are intraday) — drafted only post-agreement.
- **Arbitration**: the integration-bus **orchestrator owns `goal.md`**; any duty-split dispute or sequencing conflict is resolved there, not in either repo unilaterally.

---

## BLUF (read this first)

Today the industry-chain graph is a set of **static, file-versioned JSON scopes** (`data/operator-feeds/industry-chain/graph-*.json`) loaded **read-only** by `p10_industry_chain.py` via `symbol_to_scope`. It already has theme/demand entity nodes, an edge vocab `{customer, supplier, capex_driver, competitor}`, node types `{upstream, midstream, downstream, foreign_customer}`, materiality fields (`strength` 0-1, `revenue_share`, `hop_class`), and file-level versioning (`version`, `graph_date`) plus the ADR-0058 re-resolution discriminator.

The operator wants this to become a **signed, full-scoped, bitemporally-versioned knowledge graph** that news events flow *through* to reach a quant gate/decision — with **viz + human curation** and a **decision-flow trace view**. The natural home for the *storage + viz + curation + bitemporal versioning* is the **KB** (reobsidian is already bitemporal and has `kg-extractor/kg-store/kg-retriever/kg-validator/wikilink`). The natural home for the *runtime propagation + validation + firewall* is **quant**.

**The genuinely-new piece of the shared contract** is a **transmission SIGN (polarity) field** on edges, plus **commodity / raw-material nodes** that do not exist yet. Today the edge vocab is purely *relational* (`customer`/`supplier`/`competitor`/`capex_driver`) and the sign-flip for a `competitor` edge is handled **ad-hoc** — see `graph-v0.1.json` edge notes: *"Inverted-sign handled by R-layer per ADR-0009"*, *"competitor inversion ... Sign-flip handled by R-layer"*. That is exactly the failure mode the operator flagged: **a backwards sign is loss-making.** Polarity must become a **first-class, curated, signed field**, not a buried R-layer convention — so "copper price up = +miner / −downstream-cost" is *representable in the graph*, not inferred at runtime.

**Three hard constraints frame this whole proposal:**

1. **Validate-first + firewall (verbatim ADR-0069/0070).** Propagated news enters R2 as a **counted PRESENCE leg at ZERO directional weight** until a *pre-registered, cohort-relative, horizon-validated* study passes. The graph getting richer/prettier/KB-backed does **NOT** lift the firewall. `is_r2_weight_eligible(scope)` stays fail-closed (ADR-0065).
2. **KB-durability is a HARD PREREQUISITE.** The KB daemon **crashed twice on 2026-06-12** and runs out of `C:\Users\...\Temp\`. Making quant's chain graph *hard-depend* on a KB read-API that lives in a temp dir is a **durability risk**. We propose a **durable, repo-side, versioned EXPORT** as the decoupling fallback so quant is **never hard-down if the KB is** (§8).
3. **Free/local sources only; no advice-path contract change in this design.** §4.0 `Signal` contract stays UNTOUCHED; the graph carries semantics in graph fields, not in new `Signal` fields (same as ADR-0063/0065/0069).

**Recommendation:** agree **Phase 0 only** now — the *shared schema* (signed edge + commodity nodes + bitemporal fields + read-API shape) **and** the durable-export decision. Defer the extractor, the viz/decision-flow build, and the validation study to later phases, each its own gate.

---

## 1. The operator's four requirements — addressed explicitly

### Requirement 1 — complete, full-scoped, DIRECTIONAL (signed) graph, but quality-over-coverage + phased

- **Signed:** introduce a first-class `transmission_sign ∈ {+1, −1, ±, 0}` on every edge (§6.2). This is the load-bearing new field. `competitor` edges (today sign-flipped ad-hoc in notes) become explicit `−1`; a raw-material cost pass-through becomes explicit (`copper↑` → `+1` miner, `−1` downstream-cost). `±` = genuinely sign-ambiguous (e.g. a bank rate cut: volume tailwind vs 净息差 compression — already flagged ambiguous in the ADR-0063 handoff §7.5); `±` edges are **never auto-propagated with a sign** — they are presence-only until a curator pins the sign.
- **Full-scoped but phased:** quality-over-coverage is non-negotiable — **a backwards sign is loss-making.** We do NOT boil the ocean. Phase the scope rollout (§7): start with the scopes that already have curated graphs (`ai_compute`, `construction_infra`, `new_energy`, `consumer_demand`, `mil_defense`, `humanoid_robotics`) and add **commodity nodes** (copper/盘/锂/steel) only where a real pass-through edge is curated and source-cited. **Coverage grows behind sign-quality, never ahead of it.** The honest precedent: 0/N feedable signals across 7 validate-first negatives — coverage that isn't sign-correct AND horizon-validated is worthless.
- **Either peer may extract.** The point is graph **quality**, not who runs the extractor (§3 duty-split leaves extraction as a KB-owned engine that quant can also feed candidate edges into for curation — the *curation gate* is what protects quality, not the extractor's location).

### Requirement 2 — sources → what each builds (source-to-artifact map)

| Source (FREE) | Builds | Bitemporal field it sets | Cadence |
|---|---|---|---|
| **研报 (analyst reports / 产业链深度)** | chain **STRUCTURE** — nodes + edges + edge_type + transmission_sign (analysts literally draw 产业链 maps) | `valid_from` (when the link began), `recorded_at` (when curated) | irregular; the structural backbone |
| **定期报告 (年报/季报, 定期报告)** | **materiality** — `revenue_share`, `strength`, customer-concentration disclosures (primary-disclosure upgrade of sell-side estimates) | refreshes `revenue_share` with a new `observed_at`; can `valid_to`-close a stale link | quarterly |
| **news / 电报 (M13 capture, 快讯)** | the **EVENTS that flow THROUGH the graph at runtime** — NOT graph structure. A news item → entity match → signed-edge propagation → evidence leg | none (events are not graph edges; they reference edges) | daily / intraday |
| **policy docs (SASAC/国常会/CSRC)** | **policy → theme-node** edges + **interval timing** (a policy is valid over an interval, not a point) | `valid_from`/`valid_to` = the policy's effective interval (ADR-0063 dual-date `knowledge_date`) | irregular |

Key separation (matches the signal-horizon-separation memory): **研报/定期报告/policy build the GRAPH (slow, structural, valid over intervals); news/电报 are the EVENTS that traverse it (fast, point-in-time).** Conflating them is the M10 Telegram trap (echo, not structure).

### Requirement 3 — visualization + human curation + DECISION-FLOW view

- reobsidian **already has** graph viz + wikilink + human curation (viewer v2 whole-graph, `1c154f0`). The KB owns the viz + the human-revision UI for the graph-as-KG (a curated edge is a human firewall act, mirroring the M11 catalyst-review gate).
- **NEW: the decision-flow trace view** (§9 data contract) — given an input news item, render the chain: `news → matched entities → signed edges traversed → evidence leg produced → which quant gate/decision it impacted (and at what directional weight, including weight=0.0 when firewalled)`. This is the operator's **"every decision traced and interpreted"** principle made visible. The view is a KB-rendered surface fed by a quant-emitted **trace record** (quant owns producing the trace; KB owns rendering it). Critically, the trace must show **weight=0.0 / firewalled** legs honestly — a propagated news item that the firewall zeroed must appear in the trace as *"present, contributed 0.0, reason: scope R2-ineligible / study not passed"*, never silently dropped (this is the ADR-0064 honest-WHY-HOLD principle applied to propagation).

### Requirement 4 — dynamic graph → edge/entity-level TEMPORAL validity (bitemporal)

- We have **file-level** versioning (`version`, `graph_date`) + ADR-0058's re-resolution discriminator. The operator wants **edge/entity-level temporal validity** (a supplier link valid 2023→2025; a company *entering* a chain in 2024).
- **KB memory-store is ALREADY bitemporal** (`observed_at` / `recorded_at` / `valid_from` / `valid_to`). Storing the graph as KB KG entries gives edge/entity-level bitemporality **nearly free** — this is the strongest argument for KB-side storage. A supplier edge valid 2023-01→2025-06 is one KG entry with `valid_from=2023-01-01`, `valid_to=2025-06-30`; a company entering a chain is a node entry with `valid_from` set and `valid_to=null` (open). Replay at `as_of=D` selects edges where `valid_from ≤ D < valid_to` AND `recorded_at ≤ D` (GP8 no-look-ahead — a 2024-curated correction of a 2023 link must NOT be visible at a 2023 `as_of`).

---

## 2. Why this is a cross-module boundary (not a quant-only or KB-only change)

- It crosses the **signal contract → KB write path** boundary (the architect-invoked trigger): the graph becomes a KB-stored, KB-served artifact that quant consumes at runtime.
- It introduces a **new external dependency** for quant's runtime (a KB read-API where today there is a static JSON file).
- It needs an **ADR** (signed-edge + commodity-node schema is a load-bearing decision; sign errors are loss-making).
- It is **KB-contract-adjacent** — the graph-as-KG entry schema is *partly* owned by the KB side. Per the architect charter, **quant CONSUMES that contract and does not modify it**; the KB half is proposed here for the KB peer's review, routed through this `handoff/`.

---

## 3. DUTY SPLIT — the core of this doc

| Concern | **KB owns (PROPOSED — for KB-peer review)** | **Quant owns (we commit)** | **SHARED CONTRACT (both must agree; §6/§8/§9)** |
|---|---|---|---|
| Graph **storage** | First-class **bitemporal KG entries** (node entries + signed-edge entries) in memory-store, with `observed_at/recorded_at/valid_from/valid_to` | — | The **entity schema + signed-edge schema + bitemporal fields** (§6) |
| **Entity extraction** | The extraction engine (`kg-extractor`) over 研报/定期报告/policy; emits candidate nodes+edges | MAY feed candidate edges for curation; does NOT own the engine | The candidate-edge shape the curation gate ingests (= §6 schema, `review:pending`) |
| **Curation / revision UI + VIZ** | reobsidian viz + wikilink + human-revision surface; a curated edge is a **human firewall act** (M11-style review gate) | — | What a "curated/approved" edge looks like (`review:approved`, `transmission_sign` pinned, source-cited) |
| **Serving to quant** | A **read API** returning the graph at an `as_of` (bitemporal slice) | Read-only **CONSUME** of that API (same posture P10 has today vs static JSON) | The **read-API shape** (§8) — request `(scope?, as_of)`, response = nodes+signed-edges valid at `as_of` |
| **Decision-flow VIEW** | Renders the trace surface | **Produces** the trace record (news→entity→edge→evidence→gate→weight) | The **decision-flow trace data contract** (§9) |
| **Runtime propagation** | — | The news→entity→**SIGNED-propagation**→evidence logic (extends today's P10 cascade with explicit polarity) | — (quant-internal) |
| **Validation study** | — | The **pre-registered cohort-relative horizon VALIDATION** (ADR-0069/0070 template; feasible-fill IC; stop-if-weak) | The PASS bar is quant-strategist's; KB is informed |
| **Firewall** | — | `is_r2_weight_eligible(scope)` fail-closed; propagated news = **presence-only at 0.0** until a study passes | — (quant-internal; the firewall is NOT delegable to a KB read) |
| **Durable fallback** | Move `KB_DATA_DIR` off Temp; address crash stability | A **durable repo-side versioned EXPORT** so quant degrades gracefully on KB-down | The **export format** = the same §6 schema, file-materialized (§8) |

**Non-negotiable boundary invariant:** the **firewall lives on the quant side and is never satisfied by anything the KB serves.** The KB can serve a beautiful, fully-signed, human-curated graph; the propagated evidence still enters R2 at weight **0.0** until the quant-side, quant-strategist-gated, pre-registered study passes. A KB read can never set `is_r2_weight_eligible` true.

---

## 4. What stays UNTOUCHED (CONSUMES, does not modify)

- **§4.0 `Signal` contract / `signals/contract.py`** — UNTOUCHED. No new Pydantic field. Graph semantics live in graph fields + existing free-form `Signal` tags (`scope:<scope>` per ADR-0065 wiring 2a), exactly as ADR-0063/0069. **No `architect-ack` against the signal contract is needed by this design.**
- **ADR-0057** N-scope loader / discovery / precedence / collision rule — the read-API and the export both preserve the *same* per-scope merge + last-wins precedence semantics.
- **ADR-0058** re-resolution idempotency discriminator — `graph_version` stays the GP2 key segment; the KB-served graph exposes a stable `graph_version` per `as_of` slice so catalyst re-resolution keeps replaying correctly.
- **ADR-0065** scope firewall (`_R2_ELIGIBLE_SCOPES` allowlist, `is_r2_weight_eligible` fail-closed) + AND-gated ratchet — INHERITED verbatim. A KB-backed graph does not weaken it.
- **ADR-0069/0070** validate-first + shadow-0.0 + feasible-fill IC + cohort-relative/beta-stripped horizon discipline — this design REUSES it, does not relax it.
- The existing **static JSON loader path** stays working — the KB read-API and the durable export are *additive*; on any KB miss quant falls back to the export, and on export miss to the last static JSON (triple-fallback, §8).

---

## 5. Honest finding — does a richer signed graph actually feed the R2 wall?

Stated up front, per the discipline: across **7 validate-first negatives** (P10-R2, style-rotation, R1/R5, 合同负债, M10 Telegram, and the GMV/Taiwan priors) the R2 evidence wall has **not** been feedable by any tested signal at the 14-20d horizon. A signed graph does not change that prior. What it *does* change:

- It makes **sign errors auditable and curated** instead of buried in R-layer convention (the operator's loss-making-backwards-sign concern).
- It gives the **decision-flow trace** (the "interpret every decision" principle) a real data backbone.
- It lets a **commodity pass-through** edge (copper/锂/steel → miner/downstream) be *represented* — a class of edge that literally cannot exist today.

But the **alpha question is still open and still gated.** The most likely outcome remains another validated negative; the one under-tested shape worth a clean shot is a **multi-hop signed propagation** (a real raw-material shock → downstream-cost edge → margin → re-rate) at the *correct* horizon, cohort-relative + beta-stripped. **Do not oversell.** The graph is infrastructure for honesty + traceability first; an alpha source only if-and-when a pre-registered study passes.

---

## 6. SHARED CONTRACT — the data model (concrete fields)

> This is the piece both peers must agree before anything is built. Quant proposes it; the KB peer owns the KG-entry mapping and may counter-propose field names/types. Field *semantics* (especially `transmission_sign`) are the load-bearing part.

### 6.1 Entity (node) schema — extends today's node, adds commodity nodes

```jsonc
{
  "code": "300308.SZ",            // canonical id; A-share NNNNNN.XX | foreign ticker | COMMODITY code
  "name": "中际旭创",
  "country": "CN",
  "node_type": "midstream",       // EXISTING {upstream,midstream,downstream,foreign_customer}
                                  // + NEW "commodity" (raw-material / price node, e.g. COPPER, LITHIUM)
                                  // + NEW "theme"     (policy/demand theme node, e.g. INFRA, BAIJIU — already informal)
  "industry_sw2": "801101.SW",    // null for commodity/theme/foreign
  "subindustry_tag": "optical_module",
  "notes": "...",                 // free-form provenance
  // --- NEW bitemporal fields (KB-native; null/open allowed) ---
  "valid_from": "2023-01-01",     // when the entity ENTERED the chain (null = always)
  "valid_to": null,               // when it EXITED (null = still valid)
  "observed_at": "2026-06-13",    // when this fact was observed in a source
  "recorded_at": "2026-06-13"     // when curated into the KB (GP8 look-ahead anchor)
}
```

New `node_type=commodity` example: `{"code":"COPPER","name":"铜价","node_type":"commodity","unit":"CNY/t","source_ref":"上海有色 free spot","subindustry_tag":"base_metal"}`.

### 6.2 SIGNED edge schema — the genuinely-new piece

```jsonc
{
  "source": "COPPER",
  "target": "601899.SH",          // 紫金矿业 (miner)
  "edge_type": "raw_material",     // EXISTING {customer,supplier,capex_driver,competitor}
                                  // + NEW "raw_material" (commodity → consumer/producer)
                                  // + NEW "policy_driver"(theme/policy → beneficiary)
  // --- THE LOAD-BEARING NEW FIELD ---
  "transmission_sign": 1,         // +1 same-direction | -1 inverse | 0 none | "±" sign-ambiguous
                                  //   COPPER↑ → miner revenue ↑  => +1
                                  //   COPPER↑ → downstream cost ↑ => -1 (on the downstream edge)
                                  //   competitor capacity↑ → target pricing ↓ => -1 (was ad-hoc "R-layer")
                                  //   bank rate cut => "±" (volume vs 净息差) — NEVER auto-propagated signed
  "sign_basis": "research:中信 有色2026; 紫金 80% 收入铜",  // WHY this sign — curated, source-cited (audit)
  // --- EXISTING materiality (unchanged semantics) ---
  "strength": 0.8,                // 0-1 transmission strength
  "revenue_share": 0.8,           // primary-disclosure materiality; null = sell-side estimate
  "hop_class": 1,
  "notes": "...",
  // --- NEW bitemporal validity ---
  "valid_from": "2023-06-01",     // supplier link began
  "valid_to": "2025-06-30",       // supplier link ended (null = still valid)
  "observed_at": "2026-06-13",
  "recorded_at": "2026-06-13",
  // --- curation / firewall ---
  "review": "approved"            // {pending,approved,rejected} — a curated (approved) edge is a human firewall act
}
```

**`transmission_sign` rules (must be pinned by quant-strategist in the ADR, not here):**
- `+1` / `−1` are the only signs that may EVER propagate a directional contribution — and only when the owning scope is `is_r2_weight_eligible` (otherwise presence-only at 0.0).
- `±` (sign-ambiguous) edges are **presence-only**, never directional, until a curator splits them into a signed edge with evidence. Rate-cuts, dual-exposure names (东山精密: Apple FPC + AI-server PCB), and `competitor` edges with capacity-vs-spillover ambiguity all start `±`.
- `0` = structural relationship with no price/fundamental transmission (rare; documentation-only).
- A `transmission_sign` change is a **curated, source-cited, reviewed edit** — never a runtime inference. This is the operator's "backwards sign is loss-making" guardrail made structural.

### 6.3 Bitemporal versioning (replaces file-level-only)

- File-level `version`/`graph_date` REMAIN at the export level (the export is a point-in-time snapshot). Edge/entity-level `valid_from/valid_to/observed_at/recorded_at` are the NEW granularity, KB-native.
- **Replay rule (GP8):** an edge is visible at `as_of=D` iff `valid_from ≤ D < (valid_to or +inf)` **AND** `recorded_at ≤ D`. The second clause is the no-look-ahead guard: a correction curated in 2025 must not retroactively appear in a 2023 replay.
- `graph_version` (ADR-0058 GP2 key segment) = a stable content-hash of the *as_of-resolved slice* (so a re-resolution against the same bitemporal state replays to the same key; a curated change produces a new key — exactly ADR-0058's semantics, now at edge granularity).

---

## 7. PHASE PLAN (each phase its own gate; Phase 0 is all we ask agreement for now)

- **Phase 0 (THIS doc) — agree the shared schema + the durable-export decision.** Output: KB-peer agreement on §6 (signed edge + commodity nodes + bitemporal fields) and §8 (read-API + export), recorded as a frozen contract in this `handoff/`. **Blocking gate for everything below.** No build.
- **Phase 1 — durable export + read-only consume.** Quant: a durable, repo-side, versioned export materialized from the agreed schema (initially from the existing static graphs, signed-edge-annotated by curation); quant reads export-first, KB-API-second, static-JSON-third. KB: move `KB_DATA_DIR` off Temp + stability fix (HARD PREREQUISITE, §8) before the KB-API leg is trusted. Gate: export round-trips to today's loader byte-faithfully; firewall non-regression.
- **Phase 2 — extraction engine + curation gate.** KB: `kg-extractor` over 研报/定期报告/policy → candidate signed edges → human-review (`review:pending`). Quant: may feed candidate edges. Gate: a curated edge is source-cited + sign-pinned; `±` never auto-signed.
- **Phase 3 — viz + decision-flow trace view.** KB renders §9 trace. Quant emits the trace record. Gate: weight=0.0 / firewalled legs shown honestly.
- **Phase 4 — validation study (the alpha question).** Quant + quant-strategist: pre-registered cohort-relative, beta-stripped, feasible-fill IC at the *correct* horizon (commodity pass-through likely a margin→re-rate multi-quarter shape, NOT 14-20d). Stop-if-weak. Even a PASS ships shadow-0.0; graduation needs the ADR-0065 double-gate. **This is the only phase that can ever lift the firewall, and only for a specific scope.**

---

## 8. KB-DURABILITY PREREQUISITE + EXPORT FALLBACK (flag prominently)

**HARD PREREQUISITE.** The KB daemon **crashed twice on 2026-06-12** and runs out of `C:\Users\...\Temp\`. A Temp-dir-backed store is liable to OS cleanup + is not a durable home for a load-bearing graph. **Making quant's chain graph hard-depend on the KB read-API is a durability risk until:**
1. `KB_DATA_DIR` is moved to a **durable path** (off `Temp\`), AND
2. the crash root-cause is addressed (stability).

Until both are met, the KB read-API is a **best-effort enrichment leg, not a hard dependency.**

**Decoupling — durable repo-side versioned EXPORT (so quant is never hard-down if the KB is):**
- The KB (or a quant-run export job against the KB) periodically materializes the agreed §6 schema to a **durable, git-tracked** file under `data/operator-feeds/industry-chain/` (the same dir the loader already reads), e.g. `graph-<scope>-vX.Y.json` with the new signed/bitemporal fields. This is the **same schema as the read-API**, just file-materialized — one contract, two transports.
- **Quant read order (triple-fallback, GP4 graceful-degrade):** (1) durable export → (2) KB read-API (enrichment / freshest bitemporal slice) → (3) last-known static JSON. Quant **never crashes on KB-down**; it degrades to the export (which is as fresh as the last materialization) and surfaces the staleness honestly in the trace (§9).
- The export is also the **replay anchor**: a backtest at `as_of=D` reads the export slice resolved to `D`, so determinism (ADR-0021 byte-identical replay) does not depend on a live KB.

**Net:** the KB gives us bitemporality + viz + curation "nearly free"; the durable export gives us **durability + replay-determinism + decoupling**. We want both — the export is the safety floor, the KB-API is the enrichment ceiling.

---

## 9. DECISION-FLOW VIEW — data contract (quant emits, KB renders)

A **trace record** is emitted by quant whenever a news item is propagated through the graph (Phase 3). KB renders it as the decision-flow view. Concrete shape (quant-owned producer; KB-owned renderer — both must agree the fields):

```jsonc
{
  "trace_id": "...",
  "as_of": "2026-06-13",
  "input": { "kind": "news", "doc_id": "...", "headline": "...", "source": "m13_capture", "knowledge_date": "2026-06-13" },
  "matched_entities": [ { "code": "COPPER", "match_span": "铜价大涨", "confidence": 0.9 } ],
  "edges_traversed": [
    { "source": "COPPER", "target": "601899.SH", "edge_type": "raw_material",
      "transmission_sign": 1, "strength": 0.8, "hop_class": 1,
      "graph_version": "g<hash>", "valid_at_as_of": true }
  ],
  "evidence_legs": [
    { "symbol": "601899.SH", "agent_id": "p10_industry_chain", "scope": "new_energy",
      "presence_counted": true,
      "directional_weight": 0.0,          // HONEST: 0.0 because firewalled
      "weight_reason": "scope not in _R2_ELIGIBLE_SCOPES (ADR-0065); validation study not passed" }
  ],
  "gate_impact": [
    { "gate": "r2_valuation_paradigm", "symbol": "601899.SH",
      "effect": "presence_leg_counted_no_directional_tilt",
      "decision": "HOLD", "why": "weight=0.0 firewalled; ≥2-distinct-Pn not met" }
  ]
}
```

**Mandatory honesty property (ADR-0064 lineage):** every firewalled / weight-0.0 leg appears in the trace with its `weight_reason` — a propagated item that contributed nothing must be shown as *present-but-zeroed*, never dropped. This is what makes "every decision traced and interpreted" true rather than decorative.

---

## 10. OPEN QUESTIONS FOR THE KB PEER (things only the KB side can decide)

> Route answers back through this `handoff/`. The orchestrator arbitrates if we disagree on a duty-split line.

- **OQ-K1 (KG-entry mapping).** Can each **signed edge** and each **node** be stored as a first-class bitemporal KG entry in memory-store with `valid_from/valid_to/observed_at/recorded_at`, and does `kg-store` already model a typed, *directed, signed* edge — or is `transmission_sign` a new attribute on the KB side too? (It is new on the quant side.)
- **OQ-K2 (read-API shape).** Can the KB serve a **bitemporal slice** `get_chain_graph(scope?, as_of)` returning nodes + signed-edges valid at `as_of` (with `recorded_at ≤ as_of` enforced), and expose a stable `graph_version` content-hash per slice (ADR-0058 GP2 key segment)? What is the endpoint shape and auth (today: `X-API-Key`, `http://127.0.0.1:7733`)?
- **OQ-K3 (durability — the prerequisite).** What is the plan + timeline to move `KB_DATA_DIR` off `C:\Users\...\Temp\` to a durable path and address the 2026-06-12 double-crash? Until that lands, do you agree the **durable repo-side export is the contract of record** and the KB-API is enrichment-only?
- **OQ-K4 (export ownership).** Should the **export job** be KB-run (KB materializes to the repo dir) or quant-run (quant pulls the API and writes the export)? Quant prefers KB-run for freshness, but quant-run keeps quant self-sufficient when the KB is down — your call on which side owns the materializer.
- **OQ-K5 (extraction engine).** Does `kg-extractor` already extract *directed* chain edges from 研报/定期报告/policy text, or only co-occurrence/entity links? Can it emit candidates in the §6.2 shape with `transmission_sign` left `±` (curator-pins-the-sign) rather than guessing it?
- **OQ-K6 (curation = firewall act).** Do you agree a `transmission_sign` set/change and an edge `review:approved` are **human firewall acts** (M11-style), and that the daemon refuses to serve an `approved` signed edge that lacks a `sign_basis` citation (fail-closed, mirroring the ADR-0058/non-promotable daemon guards)?
- **OQ-K7 (decision-flow renderer).** Can reobsidian render the §9 trace record as a decision-flow view (news→entities→signed edges→evidence→gate), and does it agree to render **weight=0.0 / firewalled legs honestly** rather than hiding them?
- **OQ-K8 (commodity / theme nodes + wikilinks).** Do `node_type=commodity` and `node_type=theme` fit the KB's KG node model + wikilink/curation UI, and is there a free local source you'd want quant to wire for commodity price levels (we will NOT add paid endpoints — operator policy)?

---

## 11. Decision summary for the orchestrator

- **Asking for now:** KB-peer agreement on **Phase 0 only** — the §6 shared schema (signed edge + commodity nodes + bitemporal fields), the §8 read-API shape + durable-export decision, and answers to OQ-K1..K8. **No build authorized by this doc.**
- **Deferred behind two gates:** (a) this cross-design freeze + KB-peer agreement, AND (b) a quant-side ADR + quant-strategist sign-off on the sign / materiality / validation rules.
- **Firewall + free/local + no-Signal-contract-change:** all intact; this design changes none of them.
- **Arbitration:** the orchestrator owns `goal.md`; any duty-split or sequencing dispute is resolved there.

## STOP

**STOP: this is a PROPOSAL for the KB peer to review. No quant code, no quant ADR, no KB contract is committed by this document.** Phase 0 (schema + durable-export agreement) must freeze first; every later phase is its own gate. The firewall is not delegable to the KB — propagated news enters R2 at weight 0.0 until a pre-registered quant-strategist-gated study passes.
