# AI Usage Log: HW3, Sprint Backlog and Board Management

**Student:** Faiz Hajiani  **Course:** CIS 4374, Fall 2026  **Submission:** HW3, September 24, 2026  **Document version:** SmartParking_SRS_v3.0.docx

**Tool used:** Claude (Anthropic) desktop app for analysis and drafting.

## What I asked the AI to do

1. **Understand the lecture.** I uploaded my lecture notes and asked for a full analysis of the material (Agile versus Waterfall, the Scrum roles and ceremonies, board anatomy and columns, Scrum versus Kanban, velocity versus cycle time, and the Jira/Trello comparison) along with the homework requirements.
2. **Derive the backlog from my own WBS.** I asked it to read Section 8.3 of my v2.0 document and decompose those 79 Level-3 work items into board cards, rather than writing a new backlog from scratch, so that the board stays traceable to the plan I already submitted.
3. **Check the assignment minimums.** I asked for a programmatic count per category against the required minimums (login 5, UI 15, backend 15, reporting 10) rather than counting by hand.

## My decisions and inputs

- Chose **Jira** over Trello as the board tool, on the grounds that the story points, the three-way label taxonomy and the sprint container needed to be real fields rather than text in card titles. Wrote the justification in Section 10.1 myself.
- Chose to treat the board as the **Level-4 view of the WBS** rather than as a separate artefact, on the basis of the Class 3 point that the fourth level belongs in the PM tool and not in the WBS document. This decided the whole structure of the backlog.
- Set the Sprint 1 capacity assumption (six developers, ten working days, two developer-days per story point) and chose to commit **28 of 30 points** rather than filling the sprint, because the lecture was explicit that a first sprint with a new team carries estimation error.
- Chose the Sprint 1 contents, meaning the platform foundation plus the operator permission model, and the reasoning that operator-side work precedes driver-side work because there is no service to sell until a garage is onboarded.
- Chose to commission the unit-test coverage gate in Sprint 1 rather than later, following the lecture's point that testing interleaved between sprints beats testing as a final phase.
- Decided to defer the QA and release work items (WBS 9.1.2 through 9.3.3) to the Beta milestone rather than loading them onto the board now, and to note that decision in the document.
- Directed the board build through a written handoff rather than doing the clicking myself, but every decision the handoff encodes was mine: the tool, the field mapping, the sprint contents, the dates and the column structure. I created the Jira account and project, reviewed the finished board against the specification, and corrected the sprint dates from 20 to 31 October to 19 to 30 October so that the window contains ten working days and matches the capacity arithmetic in Section 10.4.
- Took the screenshots, recorded the update video, and submitted on Canvas myself.

## What I verified or changed

- Ran the category counts against the assignment minimums: login 10, UI 21, backend 40, reporting 13, total 84, each above its floor.
- Checked that every card names a real Level-3 parent from Section 8.3, and confirmed the backlog covers 71 of the 79 work items, with the eight omissions being the deferred QA and release items.
- Confirmed each of the UI, backend and reporting categories contains both operator-facing and driver-facing cards, since the assignment asks for both actors in each.
- Caught that the first pass double-counted story points where one work item split into a separate interface card and backend card, which made the backlog total exceed the WBS. Points are now divided between the two cards, and the backlog reconciles exactly: 309 points on the board plus 47 deferred equals the 356-point project total.
- Caught that the first draft of the Sprint 1 commitment came to 31 points against a 30-point capacity and removed a card to bring it to 28, rather than quietly raising the stated capacity to fit.
- Confirmed that inserting the new section pushes References from Section 10 to Section 11, and updated the heading and the table of contents accordingly.
- Read the generated section and edited the wording before submission.

## Limitations I am aware of

- The story points on the cards are inherited from the v2.0 estimates, which were relative assumptions rather than measured velocity. The Sprint 1 capacity figure of 30 points rests on the same unverified two-days-per-point conversion, so the sprint could be materially over- or under-committed. It will be re-based after the first two or three sprints.
- The cards are not assigned to named individuals. The project has no real team, so assignment would be invented detail; the board shows role-level ownership through the actor labels instead.
- The board reflects a single planned sprint. It has not been tested against the resource concentration flagged in Section 9.5, where backend work sits on a majority of the deliverables. That conflict is likely to surface once later sprints are laid out card by card.
