# i* SD and SR models

**Task:** 4.5 ([#152](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/152)), part d of 4.1 ([#142](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/142))
**Lead:** Hasaan Ahmad. **Reviewer:** Shamy.
**Status:** draft for review.

This folder holds the i* Strategic Dependency (SD) model and the Strategic Rationale (SR) model of the marketplace. This README records the tool, the notation, the rules for the files and the mapping between the i* models and the BPMN models. [model-content.md](model-content.md) lists every element, with its ID and its source.

The rules in this README follow the Week 12 lecture on i* (AlHaj Hassan, 2026) and the Week 12 lab sheet (UWE Bristol, 2026).

## 1. Files

| File | Content | State |
|---|---|---|
| `sd-model-draft.pistar.txt` | SD model, piStar source | Current. Converted from the OpenOME draft, with the review fixes of [#160](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/160) |
| `sr-model-draft.pistar.txt` | SR model, piStar source | Current. As above |
| `sd-model-draft.ood`, `sd-model-draft.png` | SD model, OpenOME source and export (Royden Dias) | First draft. Kept as history |
| `sr-model-draft.ood`, `sr-model-draft.png` | SR model, OpenOME source and export (Royden Dias) | First draft. Kept as history |
| `colour-key.png` | Colour of each element type | Current |
| [model-content.md](model-content.md) | Elements, IDs, sources, tensions and decisions | Current |

**Proposal (decision D1 in section 9):** use one current file for each model, and keep the drafts unchanged. The lab sheet asks the group to save revised versions and to keep the drafts. It also asks for an editable source and a readable image of each model (UWE Bristol, 2026).

| Model | Current source | Current export |
|---|---|---|
| SD | `istar-sd.pistar.txt` | `istar-sd.png` |
| SR | `istar-sr.pistar.txt` | `istar-sr.png` |

These are the output names of 4.1 (#142). [PR #161](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/161) adds a second copy of each model (`BRF-Network-&-Producer-refinement-SD.txt` and `-SR.txt`). If the group agrees D1, rename these two files to the names above before #161 merges. Do not use `&` in a file name, because it causes problems in shells and URLs.

## 2. Tool and file rules

| Item | Rule |
|---|---|
| Tool | piStar 2.1.0, online at <https://www.cin.ufpe.br/~jhcp/pistar/tool/>. The `tool` field of each model file records the version |
| Language | iStar 2.0 (Dalpiaz, Franch and Horkoff, 2016). Section 3 gives the differences from the notation of the lecture |
| File extension | `.txt`. Do **not** use `.json`. Camunda parses each `.json` file in `task1-bpmn/`, and the sync fails on a file that is not a Camunda file |
| One editor | One member edits a model file at a time (risk R3). Tell the group before you start and when you stop |
| Exports | Export a `.png` of each model after each change. Commit the source and the export together |

**How to edit a model:**

1. Open the tool and select **File > Load model**. Select the `.txt` file.
2. Make the change.
3. Select **File > Save model**. The browser downloads a new file.
4. Rename the downloaded file to the name in section 1, and replace the file in the repository.
5. Export the image, and replace the `.png` file.
6. Commit both files to the task branch.

## 3. Notation: lecture and iStar 2.0

The lecture uses the classic i* notation. piStar uses iStar 2.0. The lab sheet says that piStar "is not a direct substitute for the lecture notation". If a group uses piStar, the lab sheet tells it to "record the terminology and link differences rather than mixing notations" (UWE Bristol, 2026). This table records these differences.

| Lecture (classic i*) | iStar 2.0 in piStar | Rule in our models |
|---|---|---|
| Actor (circle) | Actor, Role or Agent | Role: Customer, the three segments, Producer, A06 and A07. Agent: BRF Network, Marketplace platform and the four services. Actor: E05 and E06 |
| Actor boundary, with the actor symbol on it | Actor boundary | piStar draws the actor symbol on the boundary, as the lab sheet requires |
| Hard goal (rounded capsule) | Goal | No difference |
| Softgoal (wavy outline) | Quality (cloud) | The diagrams show "Quality". The documents say "softgoal". The two words mean the same element |
| Task (hexagon) | Task | No difference |
| Resource (rectangle) | Resource | No difference |
| Dependency: depender, dependum, dependee | Dependency | No difference. The "D" points from the depender to the dependum, and from the dependum to the dependee |
| Task decomposition (bar at the parent task) | AND-refinement | iStar 2.0 also lets a goal have an AND-refinement. Give each AND-refinement two or more children (lab sheet, Task 3) |
| Means-end (arrow from the means to the end) | OR-refinement | Each child is an alternative means to the same end |
| Contribution: Make, Help, Hurt, Break | Contribution: make, help, hurt, break | A contribution goes only to a softgoal. Give a reason for each contribution in model-content.md |
| A resource that a task needs, inside the decomposition | Needed-by link | Use a needed-by link from the resource to the task |
| Not in the lecture | Qualification link | Links a softgoal to the goal, task or resource that it qualifies |
| Is-a | Is-a | A01, A02 and A03 are each is-a Customer |
| Is-part-of | Participates-in | A06 and A07 participate in the BRF Network |

**Rules of iStar 2.0 that piStar enforces:**

- A refined element or a contributed element cannot be a depender (Dalpiaz, Franch and Horkoff, 2016, p. 14). Thus seven dependencies in the SR model start at the actor. The "Conversion note" property of each of these dependums gives the original element.
- Do not mix AND-refinement and OR-refinement under one parent.
- Put each dependum outside the actor boundaries.

**Notation key:** the lab sheet asks for a notation key in each final diagram (UWE Bristol, 2026). `colour-key.png` gives the colours, but piStar does not add a key to an export. Add `colour-key.png` to each final export (decision D2).

## 4. Naming rules

| Element | Form | Example from our models |
|---|---|---|
| Goal | A state: noun and past participle | Order processed |
| Softgoal | A quality: adjective and noun, or noun | Secure payment, Low supplier admin |
| Task | An instruction: verb and object | Submit payment |
| Resource | An entity: noun phrase | Order confirmation |
| Actor | The name in [actors.md](../../requirements/strategic/actors.md) and in the strategic BPMN model | Producer, Payment service |
| Platform task that becomes a service task | Task name, then the planned job type in brackets | Check stock (`check-stock`) |

The job types follow section 4.4 of [functionalities.md](../../requirements/scope/functionalities.md). A statement that is not in the case study is an assumption. Mark it as an assumption in model-content.md, for example CU16 Quick delivery (lab sheet, Task 1).

## 5. Colours

| Element | Colour | Hex |
|---|---|---|
| Goal | Amber | `#FFE29A` |
| Softgoal (Quality) | Pink | `#F9C6D7` |
| Task | Blue | `#B9DCFA` |
| Resource | Lilac | `#D9CCF2` |
| Role | Green | `#C9F2CF` |
| Agent | Teal | `#A6E3DC` |
| Actor | Grey | `#E2E2E2` |

## 6. Mapping of the actors to the BPMN models

### 6.1 How to read the mapping

The i* models and the BPMN models answer different questions. The SD model shows who relies on whom. The SR model shows why an actor chooses an option. The BPMN model shows how the work progresses (AlHaj Hassan, 2026, slide 25). Thus the mapping is not one to one:

- **A dependency is not a message flow.** A dependency records reliance. It does not give the timing of a message (AlHaj Hassan, 2026, slide 12). Some dependencies have a related message flow, but many have none.
- **A means-end alternative is not an XOR gateway.** The BPMN model shows only the chosen means. The rejected means (CU03, PR03, MP14 and MP25) have no BPMN element.
- **A decomposition has no order.** An AND-refinement gives the required parts. The BPMN model gives their order (AlHaj Hassan, 2026, slide 21).
- **A lane is not automatically an actor.** The lab sheet states that "a BPMN lane does not automatically become an i* actor" (UWE Bristol, 2026). The five lanes of the BRF Network pool are functions (F01 to F05), not actors.

### 6.2 Actor mapping

| ID | i* actor | i* type | Strategic BPMN | Operational BPMN (planned, 5.1) | Same name |
|---|---|---|---|---|---|
| A01 to A03 | Customer | Role | Customer pool (collapsed) | The user tasks with Camunda Forms in FN1 and FN2 | Yes |
| A01 | Household customer | Role, is-a Customer | Customer pool (shared) | Not separate | No (note 1) |
| A02 | Community group buyer | Role, is-a Customer | Customer pool (shared) | Not separate | No (note 1) |
| A03 | Restaurant or café buyer | Role, is-a Customer | Customer pool (shared) | Not separate | No (note 1) |
| A04 | Producer | Role | Producer pool | Receives the new order notification of FN2 | Yes |
| A05 | BRF Network | Agent | BRF Network pool, with the lanes F01 to F05 | Owner of the business rules of FN1 and FN2 (S1, S3, S4) | Yes |
| A06 | Marketplace administrator | Role, participates-in BRF Network | Quality and traceability lane (F04) | Not in FN1 or FN2 (UC3) | No (note 2) |
| A07 | Authorised marketplace representative | Role, participates-in BRF Network | Quality and traceability lane (F04) | Not in FN1 or FN2 (UC3) | No (note 2) |
| SYS | Marketplace platform | Agent | The automated activities in the BRF Network lanes, for example Process order and Process payment | The service tasks and the job workers of FN1 and FN2. Later, the Task 2 services | No (note 3) |
| E01 | Payment service | Agent | Payment service pool (collapsed) | External participant, with message flows to `submit-payment` | Yes |
| E02 | Organic certification verification service | Agent | Organic certification verification service pool | Not in FN1 or FN2 | Yes |
| E03 | Notification service | Agent | Notification service pool | External participant, with message flows from `notify-producer` | Yes |
| E04 | Postcode distance service | Agent | Postcode distance service pool | Not in FN1 or FN2 | Yes |
| E05 | Data protection and financial services regulators | Actor | None | None | i* only (note 4) |
| E06 | Tax authority | Actor | None | None | i* only (note 4) |

**Notes:**

1. **A01 to A03.** The three segments do the same work in the order process ([actors.md](../../requirements/strategic/actors.md), section 2). Thus BPMN shows one Customer pool. Their needs are different (SD27 to SD29), so i* shows them as is-a specialisations (decision DI1).
2. **A06 and A07.** The lanes of the BRF Network are functions, not roles ([processes.md](../../requirements/strategic/processes.md), section 2). A06 and A07 do their work in the F04 lane (P08). They are outside UC2.
3. **Marketplace platform.** The strategic model shows the enterprise. At that level, the platform is part of the BRF Network, and its work is the automated activities in the lanes. i* shows the platform as a separate agent to show the socio-technical boundary (decision DI2).
4. **E05 and E06.** They take part in no process and exchange no message with the marketplace ([actors.md](../../requirements/strategic/actors.md), section 3). i* shows them because their dependencies set constraints on the design (NFR01, NFR08).

## 7. External participants (E01 to E06)

Each dependency gives the depender a capability. It also makes the depender vulnerable when the dependee does not deliver (AlHaj Hassan, 2026, slide 17). The "If it fails" column records this vulnerability. The last column shows how the models handle it.

| ID | Dependency (depender, dependum, dependee) | Supports | If it fails | How the models handle it | Status |
|---|---|---|---|---|---|
| E01 | SD22: Marketplace platform depends on Payment service for **Payment processed** (goal) | MP04 Payment processed | The platform cannot confirm the order, and the reserved stock stays held | FN2 decline path: `PAYMENT_DECLINED`, then retry or cancel (B11) | Required. Sandbox or mock only (NFR02) |
| E01 | SD23: Marketplace platform depends on Payment service for **Payment service availability** (softgoal) | MP28 Reliable checkout | No answer from the service | FN2 unavailable path: retries, then cancel and release the stock (MP24, B12, B17) | As above |
| E02 | SD25: Marketplace platform depends on Organic certification verification service for **Organic certification verified** (goal) | Trust in the listings (P02) | An organic claim stays unverified | "Listing not published" end event in the strategic model | Only if P02 stays (T3 in processes.md). Not in UC2 |
| E03 | SD24: Marketplace platform depends on Notification service for **Notifications delivered** (goal) | PR13 Enough time to prepare, through SD14 | A producer does not learn of a paid order and misses the 48-hour lead time (NFR07) | Multi-instance `notify-producer` (B16) and a stub (B23). The failure path is open (question R2 in section 8.5) | External (assumption Q3, decision DI5) |
| E04 | SD26: Marketplace platform depends on Postcode distance service for **Postcode distance** (resource) | NW12 Sustainability (P09) | The customer does not see the food miles | Not in FN1 or FN2. B09 is a Could story | External (assumption Q3) |
| E05 | SD31: Data protection and financial services regulators depend on BRF Network for **Regulations complied with** (goal) | NW09 Regulations complied with | The network does not comply with the regulations. Here the network is the dependee, so this is a commitment of the network (slide 24) | NFR01 and NFR03 (no card data), NFR08 (audit trail). #161 adds the task "Protect personal data and keep financial audit trail" | i* only |
| E06 | SD32: Tax authority depends on Producer for **Producer tax report** (resource) | PR14 Tax-ready accounts | The producer cannot report its tax | P07 settles each producer weekly with an audit trail (SD17, SD18) | i* only |

Each dependency has one depender, one dependum and one dependee. The SR model shows E01 and E03 as closed actors. E02, E04, E05 and E06 are only in the SD model (decision DI7).

## 8. Mapping of the SR tasks to the BPMN models

The table maps each task of the SR model. "Out of scope" means that the task is in the strategic model, but not in FN1 or FN2. Section 7.1 of model-content.md maps 17 of these tasks. This section maps all of them.

### 8.1 Customer

| ID | SR task | Strategic BPMN | Operational BPMN (planned) | Stories |
|---|---|---|---|---|
| CU02 | Buy through the marketplace | Customer pool: its messages to P03, P04 and P05 | FN1 and FN2, as seen by the customer | B01 to B17 |
| CU03 | Buy from farm shops and markets | None. The current practice, a rejected alternative (section 6.1) | None | None |
| CU05 | Check out the order | Order message to Process order (P04, Orders lane) | `process_order`: the customer user tasks | B02, B05 |
| CU07 | Review and confirm order | Order message to Process order | `process_order`: user task with a Camunda Form | B05 |
| CU08 | Amend unavailable items | Customer pool (O01, O02) | `process_order`: user task and a loop back to the stock check | B02 |
| CU09 | Pay for the order | Process payment (P05, Finance lane) | `process_payment`: the customer user tasks | B10, B11 |
| CU10 | Give sandbox payment reference | Customer pool, Payment request through Process payment | `process_payment`: user task with a Camunda Form | B10 |
| CU11 | Retry or cancel after decline | Customer pool (O03, O04) | `process_payment`: user task after `PAYMENT_DECLINED` | B11 |

### 8.2 Producer

| ID | SR task | Strategic BPMN | Operational BPMN (planned) | Stories |
|---|---|---|---|---|
| PR02 | Sell through the marketplace | Producer pool: Product listing and Fulfil order | None | None |
| PR03 | Sell by email, telephone and markets | None. The current practice, a rejected alternative | None | None |
| PR04 | List and update products | Product listing message to Manage products (P01, Product listing lane) | None. Out of scope (UC1) | None |
| PR05 | Keep stock levels accurate | Manage products (P01) | None. The stock data is an input of `check-stock` | B21, B24 |
| PR06 | Set delivery or collection arrangements | Manage products (P01). An input of Process order | None. The data is an input of `identify-producers` | B03, B04 |
| PR07 | Prepare and hand over orders | Fulfil order (P06, Producer pool) | None. Out of scope | None |
| PR10 | Accept 5% commission | None. An agreement, not an activity | None. Its effect is the commission calculation in FN2 | B13 |

### 8.3 BRF Network

| ID | SR task | Strategic BPMN | Operational BPMN (planned) | Stories |
|---|---|---|---|---|
| NW02 | Run the digital marketplace | BRF Network pool, all lanes | None | None |
| NW04 | Charge 5% commission on each order | Process payment (P05, Finance lane) | `process_payment`: the commission calculation, through SD19 | B13 |
| NW05 | Set business rules | None. The rules are inputs, not activities | The values of S1, S3 and S4 in FN1 and FN2 | B07, B12, B13 |
| NW06 | Settle producers weekly | Settle producer payments (P07, Finance lane) | None. Out of scope | None |
| NW07 | Handle quality incidents | Handle quality incident (P08, Quality and traceability lane) | None. Out of scope (UC3) | None |
| NW08 | Promote surplus offers, food miles and education | The three activities of the F05 lane | None. Out of scope | None |
| (#161) | Offer surplus produce | Offer surplus produce (P10, F05 lane) | None. Out of scope | None |
| (#161) | Report food miles | Report food miles (P09, F05 lane) | None. Out of scope | B09 |
| (#161) | Share educational content | Share educational content (P11, F05 lane) | None. Out of scope | None |
| (#161) | Protect personal data and keep financial audit trail | None. A constraint on all processes | No card data in Forms or variables (NFR03). A record of each payment attempt (NFR08) | B10, B13 |

The four tasks marked "(#161)" are in PR #161. They get IDs when model-content.md section 5.3 is updated.

### 8.4 Marketplace platform

| ID | SR task | Strategic BPMN | Operational BPMN (planned) | Stories |
|---|---|---|---|---|
| MP02 | Run automated checkout | Process order and Process payment | FN1 and FN2 | B01 to B17 |
| MP05 | Process order (`process_order`) | Process order (P04, Orders lane) | Process ID `process_order` | B01 to B08 |
| MP06 | Check stock (`check-stock`) | Process order | Service task `check-stock` | B01, B21 |
| MP07 | Ask customer to amend order | Process order (O01) | `process_order`: the path from the stock check to the amend user task | B02 |
| MP08 | Identify producers and arrangements (`identify-producers`) | Process order | Service task `identify-producers` | B03, B04 |
| MP09 | Get customer confirmation | Order message to Process order | `process_order`: the review user task | B05 |
| MP10 | Create and split marketplace order (`create-order`, `split-order`) | Process order | Service tasks `create-order` and `split-order` | B06 |
| MP13 | Reserve stock for a time limit | Process order | The reservation, with a timer boundary event on the review task | B07, B08 |
| MP14 | Check stock only at payment | None. A rejected alternative (TN3) | None | None |
| MP15 | Process payment (`process_payment`) | Process payment (P05, Finance lane) | Process ID `process_payment` | B10 to B17 |
| MP16 | Submit payment (`submit-payment`) | Payment request and Payment response with the Payment service pool | Service task `submit-payment` | B10, B20 |
| MP17 | Calculate producer amounts and 5% commission | Process payment | FEEL expressions in the output mappings | B13 |
| MP18 | Confirm order and update stock (`confirm-order`, `update-stock`) | Update stock (Product listing lane), Order confirmation message | Service tasks `confirm-order` and `update-stock` | B14, B15 |
| MP19 | Notify each producer (`notify-producer`) | Notify producers (Orders lane), New order notification request | Multi-instance service task `notify-producer` | B16, B23 |
| MP20 | Record every payment attempt | None | No element planned yet (question R3 in section 8.5) | NFR08 |
| MP22 | Let customer retry or cancel | "Payment successful?" gateway | Error boundary event `PAYMENT_DECLINED`, then the user task of CU11 | B11 |
| MP24 | Retry, then cancel and release stock | "Payment not completed" end event | Retry loop, then cancellation (`PAYMENT_SERVICE_UNAVAILABLE`) | B12, B17 |
| MP25 | End the process at once | None. A rejected alternative (UC2) | None | None |

**Summary:** the SR model has 39 tasks on main and 43 tasks with #161. FN1 or FN2 uses 24 of them. Twelve are in the strategic model only. Four are rejected alternatives. Three are agreements or constraints, not activities.

### 8.5 What the i* models add to the BPMN models

The strategic BPMN model shows the order of the work. The i* models add the reasons for the work, the responsibilities of each actor and the alternatives that the group did not choose. The lab sheet asks for candidate requirements or questions, each linked to an element or a dependency (UWE Bristol, 2026, Task 4). The lecture gives the kind of requirement that each element type suggests (AlHaj Hassan, 2026, slide 24).

| No. | i* element or dependency | Kind (slide 24) | Requirement or question | Related BPMN stage or evidence |
|---|---|---|---|---|
| R1 | MP22 Let customer retry or cancel, and CU11 Retry or cancel after decline | Task | **Gap.** No dependency connects these two tasks, in the draft or in #161. The platform cannot do MP22 without a decision from the customer. Add a task dependency "Retry or cancel after decline" from the platform to the Customer, as SD07 and SD08 do | FN2 decline path (B11, U9) |
| R2 | SD24 Notifications delivered (Marketplace platform on Notification service) | Dependency | What does FN2 do when a producer notification fails after a successful payment? The order is paid, so FN2 must not cancel it. NFR04 requires a modelled end | `notify-producer` (B16, B23) |
| R3 | MP20 Record every payment attempt, with a Make contribution to MP32 Auditability | Task | Which element records each attempt? No operational element is planned. NFR08 requires the reference, the status, the amounts and the time | `submit-payment` (5.4) |
| R4 | SD13 Delivery or collection arrangements (resource from the Producer) | Resource | Who owns the arrangement data, and where does the platform keep it? `identify-producers` needs it, but no process creates it (P01 does not list it) | Process order (B03, B04) |
| R5 | SD15 Adequate lead time (softgoal from the Producer) | Softgoal | The criterion is measurable: 48 hours (NFR07). What happens when an order cannot meet it? FN1 has no path for this case | `identify-producers` (B04) |
| R6 | CU16 Quick delivery (softgoal) | Softgoal | The case study does not state it. Keep it as a stated assumption for TN4, or remove it (question 2 in model-content.md) | None |

**One insight from the i* models:** the strategic model shows the unavailable payment service only as the "Payment not completed" end event. The SR model shows why FN2 retries: MP24 helps Reliable checkout but hurts Quick checkout (TN5). It also shows the rejected option MP25. Thus the retry limits (S3) are a trade-off between two softgoals, not only a technical setting.

## 9. Open decisions for the group

| No. | Decision | Proposal |
|---|---|---|
| D1 | Which file is the current version of each model? | One current file for each model, with the names in section 1. Keep the drafts unchanged |
| D2 | How does each final diagram show the notation key? | Add `colour-key.png` to each final export |
| D3 | Do the elements carry their IDs? | Add the ID of model-content.md (for example, CU07) as a property of each element in piStar |
| D4 | Add the missing dependency of R1? | Yes. It closes the gap in the decline path of FN2 |
| D5 | One regulator actor or two (E05)? | Question 3 in model-content.md. Keep one actor until the tutor answers |

The tutor has not answered Q1 (delivery) and Q3 (notification and postcode services) of [actors.md](../../requirements/strategic/actors.md). The answers can change E03, E04 and decisions DI4 and DI5.

## 10. References

AlHaj Hassan, S. (2026) *Goal-oriented requirements engineering using i\** [Lecture slides]. UFCFTR-30-3 Distributed and Enterprise Software Development, Week 12. UWE Bristol. Unpublished. Available on Blackboard.

Dalpiaz, F., Franch, X. and Horkoff, J. (2016) *iStar 2.0 language guide*. arXiv:1605.07767. Available from: <https://arxiv.org/abs/1605.07767> [Accessed 9 November 2026].

UWE Bristol (2026) *Week 12 goal oriented modelling with iStar* [Lab sheet]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished. Available on Blackboard.
