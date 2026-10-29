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

The video has an introduction and three sections. The sections follow the chain of the work: the analysis documents, then the strategic model that they produced, then the plan for the next work. Each member presents only the work that they did. The video aims for 9:15, so that it has a margin under 10:00.

Three rules apply to every part:

1. **Start with the evidence.** Open your task on the board and its pull request for 5 to 10 seconds. Point to the author and the reviewers. This shows the project management together with the work, as the announcement asks.
2. **In section 1, end each document with the element of the model that it produced.** For example: "These four services became the collapsed pools of the model." This shows the traceability from the analysis to the model.
3. **In section 2, give the reason for each change, not only the change.** The first-class band asks for "excellent justification". Use the decisions D1 to D7 in [interactions.md, section 8](../../requirements/strategic/interactions.md#8-decisions).

### 3.1 Overview

| Time | Section | Presenter | Content | Evidence |
|---|---|---|---|---|
| 0:00 to 0:30 | Introduction | All | Full name, student ID, and one line on your work | Cameras |
| 0:30 to 0:55 | 1. Documents | Hasaan | The case study and the chosen use case | 2.1 ([#78](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/78)) |
| 0:55 to 1:40 | 1. Documents | Royden | Actors, external services and interactions | 1.1 ([#99](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/99)), 1.3 ([#102](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/102)) |
| 1:40 to 2:20 | 1. Documents | Shamy | Functions and major processes | 1.2 ([#100](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/100)) |
| 2:20 to 2:55 | 1. Documents | Hasaan | The two functionalities | 2.2 ([#115](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/115)) |
| 2:55 to 4:10 | 2. Strategic model | Ishaq | The first version, and the Use Case 2 path from end to end | 1.4 ([#116](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/116)), sync of 27 Oct |
| 4:10 to 5:00 | 2. Strategic model | Shamy | The parallel split and the organic claim gateway | Commits 62f3b6c, 0535b94 and 85e016f |
| 5:00 to 5:50 | 2. Strategic model | Hasaan | The review changes and the message flows | Commit da8f209, 1.5 ([#145](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/145)) |
| 5:50 to 6:50 | 2. Strategic model | Royden | The call activities and the boundary to the operational models | 1.6 ([#156](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/156)), sync of 28 Oct |
| 6:50 to 7:30 | 3. Planning | Ishaq | The product backlog | 2.5 ([#148](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/148)) |
| 7:30 to 8:05 | 3. Planning | Shamy | The requirements, the traceability and the merge checks | 2.5 ([#148](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/148)), [#47](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/47) |
| 8:05 to 8:50 | 3. Planning | Hasaan | The board, the task allocation, the workflow and the stand-ups | Board, README, `standups.md` |
| 8:50 to 9:15 | 3. Planning | Royden | Sprint 2 and the questions for the module team | Board, Sprint 2 view |

Time for each member: Hasaan 2:35, Royden 2:10, Shamy 2:05 and Ishaq 1:55, plus the introduction. Section 2 has the most time, because the strategic model carries half of the marks. If the video runs long, shorten section 1. Do not shorten section 2.

### 3.2 Script

"Show" gives the screens in order. "Say" gives the points to make. Use your own words, but keep each point.

**Introduction (0:00 to 0:30), all.** Show: all cameras on. Say, in this order:

- Hasaan: full name, student ID. "I wrote the use case, the interactions and the two functionalities. I added the message flows, and I set up the repository and the board."
- Royden: full name, student ID. "I wrote the actors and the services. I added the call activities, and I revised the functionalities."
- Shamy: full name, student ID. "I wrote the processes and the functions. I added the parallel split and the organic claim gateway. I wrote the requirements and the traceability."
- Ishaq: full name, student ID. "I set up the Camunda project and drew the first strategic model. I wrote the stories of the backlog."

#### Section 1: documents

**Hasaan (0:30 to 0:55).** Show: task 2.1 and #78, then [use-case.md](../../requirements/scope/use-case.md), section "Reasons". Say:

- "The case study is a digital marketplace for the Bristol Regional Food Network. We chose Use Case 2: the multi-vendor order, checkout and payment."
- "It is the core business flow, and it connects the most parties: the customer, several producers, the network and a payment service. It also carries directly into Task 2."

**Royden (0:55 to 1:40).** Show: task 1.1 and #99, then [actors.md](../../requirements/strategic/actors.md). Then [interactions.md](../../requirements/strategic/interactions.md), section 3.1. Say:

- "Task 1.1 identifies who takes part. There are seven actors: three types of customer, the producer, the network and two roles in the network."
- "There are six external participants. Four are services: payment, organic certification, notification and postcode distance. Two are organisations: the regulators and the tax authority."
- "Task 1.3 lists the messages between them. Hasaan and I wrote it."
- "The four services became the collapsed pools of the model. The messages became its message flows."

**Shamy (1:40 to 2:20).** Show: task 1.2 and #100, then [processes.md](../../requirements/strategic/processes.md), sections 2, 3 and 5. Say:

- "Task 1.2 identifies the major processes and the functions that own them. I wrote the first draft and completed it with Ishaq."
- "The network has five functions. There are eleven major processes, and each one has one owner, a trigger and an outcome."
- "Section 5 maps each requirement of the case study to a process."
- "The five functions became the lanes of the network pool. The processes became the tasks in the lanes."

**Hasaan (2:20 to 2:55).** Show: task 2.2 and #115, then [functionalities.md](../../requirements/scope/functionalities.md), sections 3.2 and 4.2. Say:

- "From the eleven processes, we chose two functionalities: P04 Process order and P05 Process payment. Royden revised the document after the review."
- "Each one has its own trigger, owner and outcome. Each one covers the six points of the brief, as this table shows. The interface between them is the confirmed order (R06)."
- Give the response of the tutor at stand-up 3.
- "These two processes became the call activities of the model. Royden shows them in section 2."

#### Section 2: strategic model

**Ishaq (2:55 to 4:10).** Show: task 1.4 and #116, then the model in the Camunda Web Modeler. Zoom to fit, then zoom in on each area as you speak. Say:

- "I drew the first version of the strategic model in task 1.4, and I synced it from the Web Modeler. The reviews in this pull request improved it."
- "The network is one organisation, so it is one pool. Its five functions are the lanes, so the lanes show who is responsible."
- "The three customer types share one collapsed pool. The producer has a full pool, because it runs P06 Fulfil order. The four services are collapsed pools."
- Follow Use Case 2 from end to end: "The customer browses the catalogue. The order goes to Process order, then to Process payment. A gateway checks the result. On success, the stock update and the producer notification run. The producer receives its order and fulfils it."

**Shamy (4:10 to 5:00).** Show: the history of `task1-bpmn/strategic/strategic.bpmn` with your three commits. Then the model: the parallel gateways in the orders lane, and the organic claim gateway in the product listing lane. Say:

- "I reviewed the first version two times. After the review, I added the parallel split after a successful payment."
- "The stock update and the notification of the producers do not depend on each other. Thus they run at the same time."
- "I also linked P01 to P02 through an organic claim gateway (R01, R02). If a product claims organic status, the certification is checked. If the check fails, the listing is not published."

**Hasaan (5:00 to 5:50).** Show: commit da8f209, then task 1.5 and #145, then the message flows to the payment service and the notification service. Say:

- "I applied the review of the first version. Then, in task 1.5, I added the message flows from the message list of task 1.3."
- "Decision D1: the model shows one message for each business document between organisations. The review of 22 October removed the screen steps, so the model has 22 message flows."
- "D3: the notification service is a separate pool, because Use Case 3 needs the outcome of each notification recorded. D6: the model shows the payment request and the response, but not how the customer enters card details. D7: the data stores are not drawn."

**Royden (5:50 to 6:50).** Show: task 1.6 and #156, then the bot commit "Web Modeler - Git sync push - 1.0 (by Royden Dias)". Then the model: zoom in on Process order and Process payment. Say:

- "In task 1.6, I marked P04 and P05 as call activities, and I synced the model from the Web Modeler to GitHub."
- "Each call activity calls an operational process, `process_order` or `process_payment`. We build these processes in Sprint 2."
- "This is the boundary between the levels. The strategic model shows what the enterprise does and who is responsible. The operational models show how, with user tasks, service tasks and the exception paths."

#### Section 3: planning

**Ishaq (6:50 to 7:30).** Show: task 2.5 and #148, then [product-backlog.md](../../requirements/product-backlog.md), section 5 and story B10. Say:

- "Task 2.5 decomposes the two functionalities into a product backlog. I wrote the stories."
- "There are 24 stories: 19 functional stories and 5 enabler stories, with 78 story points in total."
- "Each story has the form 'As a role, I can do something, so that I get a benefit', with acceptance criteria in the Given, When, Then form. Each one has a MoSCoW priority, an estimate and a sprint."

**Shamy (7:30 to 8:05).** Show: [product-backlog.md](../../requirements/product-backlog.md), sections 3, 4 and 10.1, then the checks on one merged pull request. Say:

- "I wrote the requirements and the traceability. There are 20 functional and 13 non-functional requirements, in separate sections."
- "Section 10.1 traces each functionality from the case study, through the requirements and the model, to the stories and the Task 2 service."
- "I also changed the merge checks. They run on each merge into main, and they flag a merge with no approval or no linked task."

**Hasaan (8:05 to 8:50).** Show: the Task 1 board, Sprint 1 view, with one parent issue and its sub-issues. Then the README, section "How we work". Then [standups.md](standups.md). Say:

- "We planned Sprint 1 on this board. Each figure has one parent issue, with sub-issues for each member. Each task has owners, a priority, a week and an estimate."
- "Each task has a branch and a pull request. Another member must approve it before it merges into main. A ruleset on main enforces this."
- "After stand-up 3, we changed the allocation. In each task, one member drafts, another finalises and another reviews. The stand-up records show the work of each member each week."

**Royden (8:50 to 9:15).** Show: the Task 1 board, Sprint 2 view. Say:

- "Sprint 2 starts on Monday 2 November. It has the i* models, the operational models, the executable processes, and the update of the strategic model from this feedback."
- "We have two questions for the module team. Do you agree P04 and P05? Do you agree the settlement rule in decision D4? Thank you."

## 4. Before the submission

- [x] #84 (call activities for P04 and P05) is merged ([#156](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/156)), so that the model shows `process_order` and `process_payment` as call activities
- [ ] #85 (design decisions) is in progress. The video explains the decisions of [interactions.md, section 8](../../requirements/strategic/interactions.md#8-decisions)
- [x] #90 (product backlog) is merged ([#148](https://github.com/ssrhaso/UFCFTR-30-3-DESP/pull/148)). The Sprint 1 plan (#94) and the Sprint 2 plan (#91) are on the board
- [x] The stale `task1-bpmn/strategic/strategic-architecture.bpmn` template is not on `main`
- [ ] The ZIP files are in [submission/](submission/): `links.txt`, and the board screenshots in `board/`. The MP4 is not in the repository
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
