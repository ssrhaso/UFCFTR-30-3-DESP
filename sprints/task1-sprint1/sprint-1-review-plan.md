# Sprint 1 review plan

**Task:** [#93](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/93), Criterion 3: progress and practice
**Review:** Thu 29 Oct 2026, 14:01
**Status:** draft. The group decides who presents each part.

## 1. Format

The sources differ on the format of the review:

- The brief (UWE Bristol, 2026c, p. 7) says that each assessed sprint review is a live in-class demonstration, and that no recorded presentation is required. It also says that the module team may ask any member a question.
- The Week 7 lecture (slide 20) says that the review is a 10-minute demonstration, as a video or in person.

Confirm with the tutor if a recording is needed and where it goes. Prepare the review as a live demonstration of about 10 minutes. Each member must be able to explain every part.

## 2. What the marks reward

| Criterion | Share | What the group shows |
|---|---|---|
| Strategic BPMN model | 50% | A coherent model of the enterprise, with justified design decisions |
| Business analysis, functional scope and sprint planning | 30% | The analysis of the case study, the two functionalities, the product backlog and the sprint plan, with responsibilities and priorities |
| Sprint progress, version control and professional practice | 20% | The repository history, the reviews, the task allocation, and the work of each member |

## 3. Running order

| Time | Show | Say | Criterion | Presenter |
|---|---|---|---|---|
| 0:00 to 1:00 | **Context and scope.** `case_study/` and `requirements/scope/use-case.md` | The marketplace, Use Case 2, and why the group chose it: the core sales flow, the most parties, and the link to Task 2 | Analysis | TBC |
| 1:00 to 3:00 | **Analysis.** `requirements/strategic/actors.md` and `processes.md` | The actors and the external services, the 11 processes and the 5 functions, and how each traces to the case study | Analysis | TBC |
| 3:00 to 6:30 | **Strategic model.** `strategic.bpmn` in Camunda, with `strategic.png` as a backup | The pools and the lanes. Follow Use Case 2 through the diagram along the messages (M04 to M09). Show the call activities for P04 and P05. Explain two or three design decisions: why one network pool with lanes, why the customer and the external services are collapsed, and why the stock-amendment and retry messages stay out of the model (D1) | Strategic BPMN | TBC |
| 6:30 to 7:30 | **Two functionalities.** `requirements/scope/functionalities.md` | P04 and P05, how they cover the six points of the brief, their interface (R06), and the questions for the module team | Analysis | TBC |
| 7:30 to 8:45 | **Backlog and plan.** `requirements/product-backlog.md`, and the Sprint 1 and Sprint 2 plans | The 19 stories, their priorities and points, and what Sprint 2 builds | Planning | TBC |
| 8:45 to 9:45 | **Practice.** GitHub: the merged pull requests and reviews, the board, and the stand-up records | Who did what, the review rule (one approval), and the stand-ups | Progress | TBC |
| 9:45 to 10:00 | **Next steps** | i\* and the operational models in Sprint 2, and the open questions for the tutor | | TBC |

The strategic model carries half of the marks, so it has the most time. If the review runs long, cut the analysis section before the model.

## 4. Before the review

- [ ] #84 (call activities for P04 and P05) and #85 (design decisions) are merged, so that the model shows `process_order` and `process_payment` as call activities
- [ ] #90 (product backlog), #94 (Sprint 1 plan), #91 (Sprint 2 plan) and #93 (this plan and `review.md`) are merged
- [ ] Every Sprint 1 output is on `main` by 14:01
- [ ] Each member has pulled `main`, and the demonstration uses `main`, not a local branch
- [ ] The stale `task1-bpmn/strategic/strategic-architecture.bpmn` template is not in the demonstration folder
- [ ] The Camunda model, the PNG, the documents, the pull request list, the board and `standups.md` are open in tabs, in the order of section 3
- [ ] The group has rehearsed once with a timer
- [ ] The feedback of the tutor is recorded in `review.md` after the review

## 5. Likely questions

- Why one network pool with lanes, and not one pool for each system?
- Why is the customer a collapsed pool?
- What is the difference between the strategic and the operational model, and where is the boundary?
- Why P04 and P05? Are they end-to-end enough, and what does the group do if the module team says no?
- What are the open questions (the delivery assumption, the notification and postcode services, and P02)?
- Who wrote this part? Explain it.

## 6. References

UWE Bristol (2026c) *Assessment Task 1 brief* [Assessment brief]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished.
