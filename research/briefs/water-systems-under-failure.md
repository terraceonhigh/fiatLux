# Water Systems Under Failure

### Pressure loss, emergency isolation, and what a truck cannot replace

*Research memo, companion in register to `research/briefs/prepper-beekeeping.md`. Real-world facts only — not tied to any fictional setting's numbers.*

---

## I. Positive pressure is not a convenience, it is the treatment barrier

The thing worth understanding first is that a distribution network's pressure is not primarily about getting water uphill. It is the last barrier against contamination, and it works by direction of flow.

A buried main leaks continuously — that is normal, and utilities budget for it as non-revenue water. As long as internal pressure exceeds external, every one of those defects pushes treated water *out* into the soil. The moment internal pressure falls below the surrounding groundwater head, the same defects run backwards and draw soil water, and whatever is in it, *in*. Nothing about the pipe changes. Only the sign of the gradient.

This is why pressure loss is treated as a contamination event rather than an inconvenience. In US practice the operative threshold is a **minimum 20 psi (roughly 1.4 bar) residual pressure** in the distribution system, with normal service typically 40–80 psi; dropping below the 20 psi floor is a standard trigger for a boil-water advisory, independent of whether any sample has yet come back positive. The advisory is issued on the *loss of the barrier*, not on evidence of harm, because the sampling lag is longer than the exposure.

Two consequences that matter for any scene set during a pressure event:

**Depressurisation is retroactive.** Once the gradient has reversed anywhere in the network, you cannot know what came in or where, and restoring pressure does not undo it — it distributes it. Recovery from a pressure event therefore means flushing and sampling across the affected zone, not simply reopening a valve. The work after the emergency is longer than the emergency.

**Losing pressure means losing fire suppression.** The same 20 psi residual is specified under *fire flow* conditions, because hydrants draw enormous volumes and drag system pressure down when they open. A depressurised network cannot fight a fire, and a network fighting a fire is depressurising itself. These two failure modes are coupled and a system in one is vulnerable to the other.

---

## II. Isolating a network you have not been maintaining

Sectioning a distribution system means closing specific isolation valves. This is where deferred maintenance collects, because valves are the component that spends decades doing nothing and is then asked to work once, immediately, under load.

**Valves seize, and the failure is silent until you need them.** Buried gate valves corrode, accumulate tuberculation and debris around the seat, and lose their stems. AWWA practice therefore treats **valve exercising** — deliberately operating every valve on a scheduled cycle — as core preventive maintenance rather than an optional programme, precisely because an unexercised valve gives no indication of its condition. Utility surveys of poorly maintained systems routinely find a meaningful fraction of valves inoperable, partially operable, or simply unlocatable; a system that has let the programme lapse does not know which of its valves will turn, and finds out one at a time during an emergency. Valve *records* degrade in parallel: a valve nobody can find is functionally a valve that does not exist.

**Closing fast is its own hazard.** Rapidly stopping a moving column of water converts its momentum into a pressure surge — water hammer — governed by the Joukowsky relation, where the surge magnitude scales with the fluid's acoustic wave speed and the change in velocity. In a rigid buried main the wave speed is on the order of 1,000 m/s, so quite modest velocity changes produce surges of many bar, and the surge propagates through the network reflecting off closed ends and branches. Old pipe with reduced wall thickness fails at joints and at fittings under exactly this loading.

The operational consequence is a genuine bind: an emergency isolation must be performed **slowly**, by hand, while the thing you are racing is a falling pressure gradient. Closing the valve too quickly can burst the network you closed it to protect, and can do so somewhere you were not watching. Utilities manage this with surge analysis, slow-closing valves, air vessels and surge tanks; a crew improvising at a valve box has only the handwheel and their judgement.

**A related trap: draining is easy, refilling is not.** Recharging a large depressurised network entrains air, and trapped air pockets at high points both throttle capacity and, when they move, cause their own surges. Controlled refill is slow, requires air release valves to actually function, and is the phase where crews are most tempted to hurry.

---

## III. Hauling arithmetic: what a truck can and cannot replace

The arithmetic here is unforgiving and worth having exactly, because it decides what is and is not possible.

Water is dense and incompressible: **1 m³ = 1,000 litres = 1 tonne.** Hauling capacity is therefore governed by vehicle mass limits, not tank volume, and every load is near the axle limit by definition.

- A purpose-built highway water tanker runs roughly 20,000–30,000 L — that is 20–30 tonnes of payload, which requires a heavy tractor unit and a road that will take it.
- Agricultural water tenders and small municipal trucks are more typically **5,000–10,000 L**, i.e. 5–10 tonnes.
- Potable hauling additionally requires a tank dedicated to or certified for potable service, a sanitary fill point, and disinfection of the tank and hoses between uses. A tanker that has carried anything else is a cross-connection with wheels (see Section V).

Against that, **human drinking and sanitary demand is small and truckable.** Emergency planning figures in the range of 15 litres per person per day for basic survival needs, rising through 50 L/person/day for a reasonable domestic standard, mean that a single 10,000 L load covers hundreds of people for a day at survival rations. Trucking drinking water to a population is difficult logistics but it is arithmetically possible.

**Irrigation demand is not truckable, and the gap is orders of magnitude.** See Section IV for the derivation; the summary is that a single hectare of actively growing crop in summer wants roughly 50 tonnes of water per day, which is five to ten full loads *per hectare, per day, indefinitely*. Trucks can keep high-value stock alive. They cannot irrigate a field, and no amount of dispatch discipline changes that.

This asymmetry is the operational heart of any horticultural water emergency: the same fleet that comfortably keeps people drinking cannot keep a crop growing, and the people running it will know that from the first day while being asked to try anyway.

---

## IV. Irrigation demand, and the triage it forces

**The demand figure.** Crop water use is estimated as reference evapotranspiration (ET₀) scaled by a crop coefficient: ETc = ET₀ × Kc. The canonical method and coefficient tables are Allen, Pereira, Raes & Smith, *Crop evapotranspiration: Guidelines for computing crop water requirements* (FAO Irrigation and Drainage Paper 56, 1998), which remains the standard reference. In a temperate summer, ET₀ commonly runs 4–6 mm/day, and mid-season Kc for vegetable crops sits near 1.0–1.15, giving actively growing crops **roughly 5–7 mm/day**.

Converted: 5 mm over one hectare (10,000 m²) is 0.005 m × 10,000 m² = **50 m³ = 50 tonnes per hectare per day.**

Protected cropping is higher per unit area, not lower, because the canopy is denser and continuously productive. Greenhouse tomato guidance commonly cites **2–4 litres per plant per day at peak**, and at typical densities near 2.5 plants/m² that is 5–10 L/m²/day — the equivalent of 5–10 mm/day, sustained, with no rainfall contribution at all.

**What the irrigation method does to the requirement.** Application efficiency varies enough to matter under scarcity: surface and furrow irrigation is conventionally cited around 50–70%, sprinkler systems 70–85%, and drip/micro-irrigation 90–95%. Converting to drip under scarcity is therefore not merely a pressure accommodation but a real reduction in volume required for the same delivered water.

**Pressure requirements cut the same way.** Impact and rotor sprinklers generally need on the order of 2–4 bar to distribute properly and fail badly — poor pattern, drift, dry sectors — below that. Drip emitters typically operate around 0.7–1.4 bar, and purpose-designed low-head gravity drip tape functions on a few metres of head, i.e. a fraction of a bar. **Under a pressure emergency, drip continues working when sprinklers have already stopped being irrigation and become expensive mist.** Hand-laying drip line is the technically correct response to low pressure, and it is slow, unglamorous, entirely manual work.

**The triage order.** Horticultural triage under water scarcity follows replaceability rather than value, and the ordering is fairly consistent across extension guidance:

1. **Perennial and mother stock** — irreplaceable within a season. Years of accumulated growth, and the genetic source for everything propagated from it.
2. **Seed crops** — next season's entire capacity is contingent on them.
3. **Transplants already established** — the labour and the growing time are already sunk.
4. **Field annuals** — replantable next cycle. Expendable, in the specific sense that losing them costs a harvest and not a capability.

Two things follow that are worth noting because they are counterintuitive. First, **the most defensible allocation is also the most inequitable-looking one**: saving perennial stock while a field crop dies is correct, and it looks exactly like protecting the favoured. Second, **mature medicinal perennials sit at the top of that list on merit** — they represent multiple seasons of growth and are the least substitutable material in a pharmacopeia — so a competent triage decision and a corrupt one can produce the identical work order, and no one afterwards can distinguish them from the outcome.

---

## V. Cross-connection: the failure mode that ends the network

This is the section that matters most, because it is the one where the emergency response is more dangerous than the emergency.

A **cross-connection** is any link between potable and non-potable water. Under normal positive pressure it may do nothing. Under **backpressure** (the non-potable side at higher pressure) or **backsiphonage** (the potable side depressurised), it reverses and injects. A pressure-loss event converts every existing cross-connection in the system into an active one simultaneously, which is why depressurisation and contamination are the same event described twice.

The historical cases are unambiguous and worth knowing by name:

- **Chicago, 1933.** Amoebic dysentery at the Century of Progress International Exposition, traced to cross-connections between potable supply and sewage in hotel plumbing: on the order of 1,400 cases and approximately 98 deaths. This outbreak is the standard originating citation for modern cross-connection control programmes.
- **Milwaukee, 1993.** A *Cryptosporidium* outbreak affecting an estimated 403,000 people — the largest documented waterborne disease outbreak in US history — following degraded performance at a filtration plant. The significant technical point is that **_Cryptosporidium_ oocysts are highly resistant to chlorine** at practical contact times, so a chlorinated but inadequately filtered supply is not protected against them. Chlorine residual is not a universal backstop.
- **Walkerton, Ontario, 2000.** *E. coli* O157:H7 and *Campylobacter* in a municipal well supply: 7 deaths and roughly 2,300 illnesses in a town of about 5,000. The proximate cause was contamination reaching a vulnerable well, but the inquiry's findings centred on chlorination and monitoring practice — operators falsifying records and failing to maintain adequate residual. It is the canonical case for *institutional* rather than technical failure of a water system, and the reason Ontario's regulatory regime was rebuilt afterwards.

**Why this bears directly on emergency improvisation.** The specific move that a works crew under pressure is most likely to reach for — tying an available non-potable source into existing distribution piping to get irrigation water moving — is precisely the mechanism of Chicago 1933, executed deliberately. Temporary piping laid in haste, unlabelled, connected with whatever fittings are to hand, on a network whose pressure is already abnormal, is the textbook configuration. And it survives the emergency: temporary connections become permanent because nobody documents them and the crew that made them disperses.

Cross-connection control practice exists as a discipline for this reason, and its core provisions are all administrative rather than clever: physical separation, air gaps and backflow preventers at every interface, **distinct and unambiguous marking of non-potable lines**, and a maintained inventory of every connection that exists. All four fail the same way — through undocumented urgency.

**On irrigating with non-potable water.** It is legitimate and widely practised, with conditions. The reference framework is the WHO *Guidelines for the Safe Use of Wastewater, Excreta and Greywater* (2006, four volumes), which scales required water quality to crop type and irrigation method: crops eaten raw demand far higher quality than those cooked or processed, and **drip application below the canopy reduces pathogen contact with the edible portion compared with overhead sprinkling.** Medicinal material intended for topical application on broken skin belongs at the cautious end of that spectrum. So non-potable substitution for irrigation is the right answer during scarcity, and it comes with a labelling-and-discipline burden that a crew improvising at speed is least equipped to carry.

---

## VI. Is there a hard cap?

Following the structure of the beekeeping memo: is there a component of a water system that a competent post-industrial economy simply cannot reproduce, where the whole enterprise caps out once a stockpile is gone?

Yes, and it is narrower and more specific than one might expect: **it is the ultraviolet lamp.**

Work through the barriers:

**Filtration survives indefinitely.** Slow sand filtration is a mid-nineteenth-century technology — mandated in London by the Metropolis Water Act 1852 — and it requires sand, gravel, a basin, and labour to scrape and re-lay the schmutzdecke. It is effective against protozoan parasites including *Cryptosporidium*, because removal is physical rather than chemical. Its cost is **land and time**: filtration rates run roughly 0.1–0.3 m/h, against 5–15 m/h for rapid gravity sand filtration, so equivalent throughput needs something on the order of thirty to a hundred times the filter area. A city-scale slow sand installation is measured in hectares. That is a real and permanent constraint, but it is a constraint on *area*, which does not run out the way a consumable does.

**Chlorination survives.** Chlor-alkali chemistry is nineteenth-century: chlorine from the electrolysis of brine, and bleaching powder (calcium hypochlorite) by passing chlorine over slaked lime, an industrial process from the early 1800s. Salt, lime and electricity are all locally producible. On-site electrochlorination of brine is the modern version of the same idea, and its consumable is the coated electrode rather than the chemical. Disinfection by chlorine is therefore sustainable at an 1880s technological floor, and this is the barrier a long-horizon system should be built around.

**Ultraviolet disinfection does not survive.** A UV reactor needs low-pressure mercury or mercury-amalgam lamps, fused-quartz sleeves transparent at 254 nm, electronic ballasts, and calibrated UV intensity sensors. Every one of those is a product of an industrial supply chain — quartz working, mercury dosing, semiconductor electronics — and none is reproducible in a workshop economy. Lamps additionally age out on a duty cycle measured in thousands of hours whether or not they are damaged, so a stockpile depletes on a schedule regardless of care.

This produces a specific and slightly cruel finding. **UV is the barrier a modern utility adds precisely to handle chlorine-resistant protozoa, and it is the barrier that cannot outlive industrial supply.** A system that has come to rely on UV in place of large-footprint filtration has traded a land cost for a consumable cost — an excellent trade while the supply chain exists and a fatal one afterwards. The recovery path is backwards: rebuild filtration area, and accept that it is slow and occupies ground that could have grown something.

If a single sentence is wanted: **there is no mineral floor under water treatment, but the disinfection barrier that industrial modernity chose is the one that cannot be re-made, and going back means paying in hectares what was formerly paid in lamps.**

A second, non-material near-cap worth naming plainly, on the Walkerton pattern: **a water system's real limiting component is a maintained institution.** Valve exercising, cross-connection inventories, residual monitoring and honest record-keeping are all cheap in materials and expensive in sustained attention, and every one of them fails invisibly. A network can be materially sound and functionally unsafe because the programme that knew where the valves were has stopped existing.

---

## Confidence notes

- **Solid, standard engineering practice, verifiable in primary references:** the role of positive pressure in preventing intrusion and the 20 psi minimum residual as a boil-advisory trigger (US practice; AWWA and EPA guidance); water hammer and the Joukowsky relation, with acoustic wave speeds around 1,000 m/s in rigid buried pipe; valve exercising as core AWWA-recommended preventive maintenance; backflow via backpressure and backsiphonage as the cross-connection mechanism; cross-connection control provisions (separation, air gaps, backflow prevention, marking, inventory).
- **Solid, directly citable sources:** Allen, Pereira, Raes & Smith, FAO Irrigation and Drainage Paper 56 (1998) for ET₀/Kc methodology and coefficients; WHO *Guidelines for the Safe Use of Wastewater, Excreta and Greywater* (2006, 4 vols) for crop-and-method-scaled water quality; Metropolis Water Act 1852 for the mandating of sand filtration in London.
- **Documented outbreaks, figures widely reported and consistent across sources:** Chicago 1933 Century of Progress amoebic dysentery, ~1,400 cases / ~98 deaths; Milwaukee 1993 *Cryptosporidium*, ~403,000 affected; Walkerton 2000, 7 deaths / ~2,300 ill in a town of ~5,000, with the O'Connor inquiry locating cause in operational and institutional failure. Chlorine resistance of *Cryptosporidium* oocysts and their susceptibility to UV are both well established.
- **Well-supported but range-dependent, not precise:** tanker capacities (5,000–10,000 L small, 20,000–30,000 L highway); emergency per-capita demand figures (15 L/day survival, ~50 L/day domestic) which vary by agency and standard; irrigation application efficiencies (surface 50–70%, sprinkler 70–85%, drip 90–95%); operating pressures for sprinklers (2–4 bar) and drip (0.7–1.4 bar, less for low-head tape); slow sand filtration rates (0.1–0.3 m/h) against rapid sand (5–15 m/h); greenhouse tomato use at 2–4 L/plant/day. All of these are real published ranges rather than single values, and the derived "50 tonnes per hectare per day" follows from the midpoint of the ET range — it is the right order of magnitude, not a figure to quote to two significant digits.
- **Deliberately not quantified:** the fraction of valves found inoperable in neglected systems. Figures circulate but vary enormously with system age, soil, valve type and survey method, and I could not tie a defensible number to a specific study. The qualitative claim — that lapsed exercising programmes produce unknown valve condition, discovered during emergencies — is not in dispute.
- **Genuinely a judgment call in this memo:** naming the UV lamp as water treatment's hard cap, and framing the filtration-versus-UV choice as trading hectares for consumables. No source frames it that way; it is a synthesis from the reproducibility of each barrier's inputs against the *Cryptosporidium* chlorine-resistance literature. The individual technical claims are solid; the conclusion drawn from assembling them is mine.
