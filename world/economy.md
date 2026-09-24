# Economy

## Scope

This file owns currency, prices, wages, rationing, exchange, property, debt,
gifts, requisitions, and seasonal scarcity.

## Established in the manuscript

- `TEXT` The university prints its own banknotes. The front shows three
  signatures — the University President, the Dean of Economics, and the
  Director of Food Services — under a dogwood-and-mahonia seal.
  (`manuscript/08-hyperbolic.md:227`)
- `TEXT` Notes come in tens and fives. The five-dollar note carries a red
  rose-engine pattern at centre-left. (`manuscript/08-hyperbolic.md:227`;
  `manuscript/13-glean.md:125`)
- `TEXT` University bylaw lets the Senate approve new dies for the rose
  pattern only one at a time. (`manuscript/13-glean.md:125`)
- `TEXT` Note paper is hemp and pulped old books. The hemp makes it tough; the
  book pulp makes it cheap enough to print. (`manuscript/13-glean.md:127`)
- `TEXT` Two potato samosas and a sausage roll cost fifteen dollars at a campus
  bakery. (`manuscript/08-hyperbolic.md:225`)
- `TEXT` A day labourer earns fifteen dollars a day. His household spends it on
  two loaves and three onions for supper. (`manuscript/13-glean.md:121`,
  `:137`)
- `TEXT` Barter and gift payment run alongside cash. Mead, honey, sausage, and
  jam pay for goods and favours. "Two vials of poppy" is the price the
  hardware store sets for a pair of rubber gloves.
  (`manuscript/01-continuity-test.md:15`, `:159`)
- `TEXT` The university hands out seed and assigns oxen to towns.
  (`manuscript/10-wild-oats.md:131`, `:191`)
- `TEXT` A langar serves free breakfast. A message board there carries job
  postings. (`manuscript/13-glean.md:9-11`)
- `TEXT` University staff on official duty carry a chit and a metal seal.
  (`manuscript/10-wild-oats.md:131`)

Chits are credentials, not currency. See `institutions.md` for what they mean
and how towns read them.

## Terrace decisions

- `TERRACE` Collie's bakery order is retconned from $25 to $15, paid with a ten
  and a five. Reason: an ordinary bakery margin, and a regular quick lunch for
  Collie. (2026-09-23)
- `TERRACE` The dollar is backed by a caloric amount of staple crops. Bread is
  the one product redeemed at the highest volume, not the backing itself.
  (2026-09-23)
- `TERRACE` Five dollars is principally backed by the Standard Loaf: $5 is one
  Standard Loaf. The loaf's price is fixed by the currency's definition, not by
  competition. (2026-09-23)
- `TERRACE` Redemption is in bulk only. Individuals do not redeem notes at a
  window. (2026-09-23)
- `TERRACE` The system is honest. The reserve is not secretly fractional.
  (2026-09-23)
- `TERRACE` Groups pool to reach the bulk minimum. Religious institutions and
  pooling carry this, not patronage. (2026-09-23)
- `TERRACE` Pooling takes three common forms: public offices, religious
  institutions, and private enterprise. Each acts as a spoke of the
  university's monetary system and spreads the currency outward.
  (2026-09-23)
- `TERRACE` The currency symbol is a plain dollar sign, `$`. (2026-09-23)
- `TERRACE` Note serial numbers are in hexadecimal, for a modern feel.
  (2026-09-23; base64 was considered and dropped.)
- `TERRACE` Towns have local redemption points. Who runs a given one — a
  public office, a religious institution, or a private business — varies.
  (2026-09-23)

## Quantities and assumptions

`MODEL` One dollar redeems 1,000 kcal of staple at wholesale.

`MODEL` The Standard Loaf is the headline peg; the wholesale staple rates are
set beneath it so a bakery can make the loaf at $5. Flour for one loaf
redeems at $2, and fuel, labour, and margin make up the rest. A bakery that
cannot cover those costs at $5 short-weights the loaf or lobbies for a rate
change.

`MODEL` Each redeemable staple has its own rate, set near market ratios
rather than by pure calorie count. The Dean of Economics revises the rates once
a year, after harvest. Pure calorie parity would let holders drain the most
valued staple.

`MODEL` The reserve holds grain and dried pulses only. Potatoes do not store
long enough to back notes. They can be a harvest-season redemption product.

`MODEL` Price and cost ladder:

| Item | Price | Notes |
|---|---:|---|
| Standard Loaf, 1 kg dough | $5 | About 2,000 kcal |
| Flour for one loaf, at redemption | $2 | About 580 g |
| Fuel, labour, minor ingredients, margin per loaf | $3 | Open market |
| Storage onion, winter | $1.50 | Not a redeemable staple |
| Potato samosa | $4 | Retail, not pegged |
| Sausage roll | $7 | Retail, not pegged |
| Unskilled day wage | $15 | `TEXT` |

`MODEL` The retail loaf costs about 2.5 times its wholesale calories. The
labourer's $15 buys about 4,000 kcal at retail and would buy 15,000 kcal at
wholesale. That gap is the cost of not redeeming in bulk.

`MODEL` The minimum redemption is one sack, about 25 kg of wheat or $85.

`MODEL` A campus core of 20,000 holding about 2.5 months of calories in notes
needs about 3.5 billion kcal in reserve: roughly 1,000 tonnes of grain, or
$3.5 million in circulation.

## The reserve

`MODEL` Every note is backed by graded grain and pulses in store. No note is
issued without grain behind it.

`MODEL` Seed comes from a separate seed bank, not from the currency reserve.
Bred seed, such as the landrace Nadia distributes
(`manuscript/10-wild-oats.md:189`), was never food stock.

`MODEL` Towns repay seed loans in grain, with published interest, at harvest.
The interest grain enters the reserve. The Senate issues new notes against it
once a year, after the harvest is counted.

`MODEL` The University Press prints a monthly reserve statement: grain held,
notes in circulation, and seed loans outstanding.

`MODEL` If a harvest fails, the Senate may suspend redemption. The suspension
clause is public and names a resumption date and an issue cap.

`MODEL` A grading bureau inspects grain before it enters the reserve.

## Pooling

`TERRACE` Pools and redemption points run through three kinds of operator.
Each is a spoke of the university's monetary system: it gathers notes or
grain in bulk, redeems at the hub, and carries the currency further out.

| Operator | Examples | What it adds |
|---|---|---|
| Public office | A town office holding the town's granary account | Political control of redemption |
| Religious institution | Gurdwara, parish | Storage, kitchen, membership, trust |
| Private enterprise | Licensed exchange house, merchant counter | A fee for convenience; reach where no office or congregation exists |

`MODEL` Mixed arrangements are common. A town office may hold the account
while a licensed merchant runs the counter. An employer that runs redemption
for its own workers — a cannery, for example — risks the company-store
problem, because it controls both the wage and what the wage is worth.

`MODEL` Any group with a registered signatory can redeem in bulk. Registration
needs no sponsor.

`MODEL` Religious institutions are the main pooling infrastructure. They
provide what poor households lack: safe storage, a kitchen or oven, a
signatory, and a standing membership.

- The gurdwara pools donations and redeems in bulk. This is how the langar
  feeds people for free (`manuscript/13-glean.md:9`).
- A Catholic parish runs pools for its members. The Rosary couple in Glean
  belongs to one (`manuscript/13-glean.md:23-29`).

`MODEL` Rotating savings groups let households without savings join a pool.
Each member pays in weekly, and one member takes the pot each round.

`MODEL` Other pools form around crews, fraternities such as the Epsilons
(`manuscript/06-isolation.md:131`), shared houses, and neighbourhoods.

`MODEL` Poor pools redeem oats and dried peas more than wheat. Porridge and
pottage need a pot and a fire, not a mill and an oven.

`MODEL` Glean already shows both halves: breakfast at the langar is pooled
wholesale calories, and supper is retail bread bought with same-day cash.

## How towns acquire dollars

`MODEL` Weirwick's cannery is paid in dollars for fish and pays its workers in
dollars. Its need for university salt gives dollars value across the town.
The town's local redemption point keeps dollars near par despite the
three-day circuit.

`MODEL` The reserve works as a currency board in reverse. A town delivers
graded grain or pulses at the published staple rate and receives notes or a
credit on its granary account.

`MODEL` A town's granary account at the university is its bank balance. Towns
are bulk depositors, so they are also natural bulk redeemers.

`MODEL` University services — doctor tours, oxen, seed, fuses, medicine,
salt — carry dollar prices. A town can settle them by delivering grain into
its account. The university does not require payment in dollars; dealing in
dollars is simply the cheapest way to deal with it.

`MODEL` Dollars reach town markets through staff paid on tour
(`manuscript/01-continuity-test.md:41-49`) and through town merchants who sell
at the campus bazaar (`manuscript/11-mulberry.md:67`).

`MODEL` Barter persists where a town has little grain to deposit, such as a
fishing town like Weirwick, and far from redemption points
(`manuscript/01-continuity-test.md:15`).

`MODEL` The university does not levy a head tax or hut tax payable only in
dollars. A dean who knows the history of colonial currency taxes would choose
not to.

## Note security

`TEXT` Established features: the rose-engine pattern from Senate-controlled
dies, three facsimile signatures, the centred dogwood-and-mahonia seal, a
colour per denomination, and hemp and book-pulp paper.
(`manuscript/08-hyperbolic.md:227`; `manuscript/13-glean.md:125-127`)

`MODEL` The main counterfeiting threat is salvaged scanners, photocopiers,
and inkjet printers. Features built into the paper and the printing process
defeat them best, and the university controls both.

`MODEL` Proposed features:

| Feature | How it is made | Why it fits |
|---|---|---|
| Watermark | Shaped mould at the university paper mill | Cannot be copied; checked against light |
| Coloured hemp fibres | Dyed red and blue fibres mixed into the pulp | Uses existing hemp; cannot be printed |
| Intaglio printing | Ink pressed from engraved plates; the rose-engine die is the master | Raised ink can be checked by touch, including by people who cannot read |
| Serial numbers | Numbering machine; one unique serial per note | Serial ranges in circulation appear in the monthly reserve statement |
| Microprinting | Tiny engraved lettering worked into the rose pattern | Copiers blur it |
| Embedded thread | Dyed silk or hemp thread laid into the forming sheet | A second paper-level feature |
| Redemption promise | Printed line promising bulk redemption through Food Services | Puts the backing on the note |

`MODEL` Holograms and colour-shifting ink are out of reach; they need
industrial production.

`MODEL` Hexadecimal serials need numbering wheels with 16 positions, 0–9 and
A–F, instead of the usual 10. The machine shop can cut them.

`MODEL` Redemption doubles as inspection. Notes return through bakeries and
pools to Food Services, where worn and counterfeit notes are caught and
retired. Bakers become the front line of detection.

`MODEL` The Senate's die control extends to plates made from each die, with a
log of spoiled sheets destroyed.

## Dependencies

- Grain and pulse harvests from the breadbasket and townships.
- Grading, storage, and pest control for the reserve.
- The University Press, for notes, the Standard Loaf specification, and the
  reserve statement.
- Fuel and labour for bakeries, both priced on the open market.

## Failure modes

- `MODEL` A bad harvest shrinks the reserve and forces a public suspension or
  a smaller note issue.
- `MODEL` Fuel is the uncontrolled bakery input. Dear firewood squeezes the
  fixed $5 loaf. Bakers may short-weight loaves or lobby for a rate change.
- `MODEL` Graders can be bribed to accept wet or infested grain.
- `MODEL` Staple rates drift from market ratios between annual revisions.
- `MODEL` Households living day to day cannot save toward a pool without a
  rotating group.

## Substitutes and adaptations

- `TEXT` Barter in honey, mead, sausage, jam, and poppy vials where notes are
  scarce or no redemption point is near.

## Open questions

- `OPEN` How the two payment systems (university banknotes, barter/gift
  goods) trade against each other. No fixed exchange rate appears in the text
  yet.
- `OPEN` The Dean of Economics's training. Terrace suggested the Chicago
  School; a model analysis weighed Chicago price theory against mainstream
  central banking, MMT, and Ostrom-style institutionalism.
- `OPEN` What Food Services pays towns for grain, and in what.
- `OPEN` Whether note paper glows under ultraviolet light. Pulp from books made
  before about 1950 lacks optical brighteners; later pulp glows. This decides
  which way a UV test works.
- `OPEN` Where Weirwick's salmon fits: calories, but not a redeemable staple.
  The university buys it from operating funds, not new issue.

## Sources

Precedents named during design (2026-09-23). These came from model memory and
have not been checked against primary sources. Verify before relying on them.

- Benjamin Graham, commodity-reserve currency (*Storage and Stability*, 1937).
- F. A. Hayek, "A Commodity Reserve Currency" (1943).
- Milton Friedman, "Commodity-Reserve Currency" (1951).
- The Chicago Plan for full-reserve banking (1933); Benes and Kumhof, "The
  Chicago Plan Revisited" (IMF, 2012).
- Bank Charter Act 1844: weekly Bank of England returns; suspensions in 1847,
  1857, and 1866.
- Chicago Board of Trade grain grading (1850s); Illinois Warehouse Act (1871);
  *Munn v. Illinois* (1877).
- Assize of Bread and Ale (England, 13th to 19th century).
- Wang Anshi's Green Sprouts seed loans (11th-century China).
- Rentenmark stabilisation (Germany, 1923).
- Rochdale Society of Equitable Pioneers (1844); rotating savings and credit
  associations.
- West African Currency Board (1912), sterling-backed colonial currency.
- British colonial hut and poll taxes: Sierra Leone Hut Tax War (1898),
  Bambatha rebellion (1906).
- Roman provincial tribute in coin; Vindolanda tablets on frontier spending.
- Han salt and iron monopoly, *Discourses on Salt and Iron* (81 BC); the
  British Indian salt tax and the Salt March (1930).
- Spanish silver dollars and chop marks in China; the Maria Theresa thaler.
- Commutation of labour services in medieval England; Mughal *zabt*
  assessment; Tokugawa rice taxation in *koku*.
