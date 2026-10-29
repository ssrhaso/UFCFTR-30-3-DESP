# Sprint 1 review plan

**Task:** [#93](https://github.com/ssrhaso/UFCFTR-30-3-DESP/issues/93), Criterion 3: progress and practice
**Review:** Thu 29 Oct 2026, 14:00. One ZIP file on Blackboard, with the video
**Status:** agreed for the video. Each part goes to the members who did that work in the commit history. The group can swap a part before the recording.

## 1. Format

The group submits the Sprint 1 Review as a video (option B of the Blackboard announcement of 22 Oct 2026). At stand-up 3 the group chose an in-class presentation (option A). On 29 Oct 2026 the group changed to a video.

The brief describes each sprint review as a live in-class demonstration (UWE Bristol, 2026c, p. 6). For Sprint 1, the module team also permits a video (UWE Bristol, 2026f). The rules for the video are:

- One MP4 file of 10 minutes or less.
- All four members take part. Each member has the camera and the microphone on, with clear audio and video.
- Each member gives their full name and student ID.
- The video shows the project management together with the work: the Kanban board, the task allocation, and how the group planned and tracked the sprint.
- Slides are optional. The group shows the repository and the board.
- The ZIP file holds the MP4, `links.txt` with the links to the repository and the board, the board screenshots and the PNG of the strategic model.
- The module team gives written feedback on Blackboard.

## 2. What the marks reward

| Criterion | Share | What the group shows |
|---|---|---|
| Strategic BPMN model | 50% | A coherent model of the enterprise, with justified design decisions |
| Business analysis, functional scope and sprint planning | 30% | The analysis of the case study, the two functionalities, the product backlog and the sprint plan, with responsibilities and priorities |
| Sprint progress, version control and professional practice | 20% | The repository history, the reviews, the task allocation, and the work of each member |

## 3. Running order

| Time | Show | Say | Criterion | Presenter |
|---|---|---|---|---|
| 0:00 to 0:30 | **Introductions.** Each member on camera | Full name and student ID | | All |
| 0:30 to 1:30 | **Context and scope.** `case_study/` and `requirements/scope/use-case.md` | The marketplace, Use Case 2, and why the group chose it: the core sales flow, the most parties, and the link to Task 2 | Analysis | Hasaan |
| 1:30 to 3:00 | **Analysis.** `requirements/strategic/actors.md`, `processes.md` and `interactions.md` | The actors and the external services (1.1). The 11 processes and the 5 functions (1.2). The messages and the relationships between the processes (1.3). How each item traces to the case study | Analysis | Royden, Shamy |
| 3:00 to 6:30 | **Strategic model.** `strategic.bpmn` in Camunda, with `strategic.png` as a backup | Follow Use Case 2 through the diagram along the messages M04 to M09. Explain the design decisions: one BRF Network pool with five functional lanes, and a shared collapsed pool for the three customer segments ([interactions.md, section 2](../../requirements/strategic/interactions.md#2-participants)). The external services are collapsed pools (D3). The producer is a full pool, because it runs P06 Fulfil order. One message for each business document (D1). The data stores are not drawn (D7). P04 and P05 are call activities, so the strategic model stays at enterprise level and the operational models of Sprint 2 give the detail | Strategic BPMN | Ishaq, Shamy, Royden |
| 6:30 to 7:30 | **Two functionalities.** `requirements/scope/functionalities.md` | P04 and P05, how they cover the six points of the brief, their interface (R06), and the response of the tutor at stand-up 3 | Analysis | Hasaan, Royden |
| 7:30 to 8:45 | **Backlog and plan.** `requirements/product-backlog.md`, and the Sprint 1 and Sprint 2 tasks on the board | The 24 stories (19 functional and 5 enablers, 78 points), their MoSCoW priorities and estimates, and the traceability to the requirements. The Sprint 2 tasks, with their owners, priorities, estimates and weeks | Planning | Ishaq, Shamy |
| 8:45 to 9:45 | **Practice.** GitHub: the merged pull requests and reviews, the three checks (BPMN lint, approvals, closes issue), the board and the stand-up records | The review rule (one approval). After stand-up 3 the group changed the allocation, so that every member works on every artefact: one member drafts, another finalises, and another reviews. The Camunda sync commits show the bot account `desp-camunda-sync`, and their message gives the member, for example "by Royden Dias" | Progress | Hasaan |
| 9:45 to 10:00 | **Next steps** | Sprint 2: the i\* models (4.1), the operational models (5.1), the executable processes (6.1), and the update of the strategic model from the feedback (7.1) | | Royden |

The strategic model carries half of the marks, so it has the most time. If the video runs long, cut the analysis section before the model.

## 4. Before the submission

- [x] #84 (call activities for P04 and P05) is merged ([#156](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/156)), so that the model shows `process_order` and `process_payment` as call activities
- [ ] #85 (design decisions) is in progress. The video explains the decisions of [interactions.md, section 8](../../requirements/strategic/interactions.md#8-decisions)
- [x] #90 (product backlog) is merged ([#148](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/148)). The Sprint 1 plan (#94) and the Sprint 2 plan (#91) are on the board
- [x] The stale `task1-bpmn/strategic/strategic-architecture.bpmn` template is not on `main`
- [ ] Every Sprint 1 output is on `main` by 14:00
- [ ] Each member has pulled `main`, and the video uses `main`, not a local branch
- [ ] The Camunda model, the PNG, the documents, the pull request list, the board and `standups.md` are open in tabs, in the order of section 3
- [ ] The group has rehearsed once with a timer
- [ ] The MP4 is 10 minutes or less, and each member is on camera with their full name and student ID
- [ ] The ZIP file is on Blackboard before 14:00
- [ ] The feedback of the tutor is recorded in `review.md` after the review ([sprints/README.md](../README.md))

## 5. Likely questions

- Why one network pool with lanes, and not one pool for each system?
- Why is the customer a collapsed pool?
- What is the difference between the strategic and the operational model, and where is the boundary?
- Why P04 and P05? Are they end-to-end enough, and what does the group do if the module team says no?
- What are the open questions (the delivery assumption, the notification and postcode services, and P02)?
- Who wrote this part? Explain it.

## 6. References

UWE Bristol (2026c) *Assessment Task 1 brief* [Assessment brief]. UFCFTR-30-3 Distributed and Enterprise Software Development. Unpublished.

UWE Bristol (2026f) *Sprint 1 Review submission* [Blackboard announcement]. UFCFTR-30-3 Distributed and Enterprise Software Development, 22 October. Unpublished.
