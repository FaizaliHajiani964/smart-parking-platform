# AI Usage Log — HW2: Work Breakdown Structure and Draft Timeline

**Student:** Faiz Hajiani  **Course:** CIS 4374, Fall 2026  **Submission:** HW2, September 17, 2026  **Document version:** SmartParking_SRS_v2.0.docx

**Tool used:** Claude (Anthropic), desktop app, one working session on September 17, 2026.

## What I asked the AI to do

1. **Understand the lecture.** I uploaded my lecture notes and asked for the homework requirements and a full analysis of the material (WBS depth, deliverables vs. tasks, story points vs. function points vs. COCOMO, dependency types, milestones, cushions, interleaved testing, Mythical Man-Month).
2. **Plan the assignment.** I asked for a step-by-step breakdown of everything needed to finish HW2 (WBS, estimation assumptions, timeline, Gantt chart, document update, version bump, video, repo, Canvas).
3. **Support material.** A 1–2 minute script for the Teams update video, an updated README, and this log.

## My decisions and inputs

- Chose a realistic ~7-month schedule (kickoff to final delivery) rather than compressing everything into the semester, following the lecture's warning about overambitious timelines.
- Chose version 2.0 (major bump: two whole new sections), the Excel Gantt approach, and the one-file-per-homework AI log.
- Reviewed the WBS module list against my SRS scope (Section 2.5) and the parking-app components from the lecture (authentication, user/operator setup, monitoring, payment, reporting, dashboards, fraud prevention).
- Recorded the update video, committed and pushed the repository, and submitted on Canvas myself.

## What I verified or changed

- Checked that every branch of the WBS is exactly three levels deep and that Level 1/2 entries are deliverables, not tasks.
- Checked that the Excel dates match the Python-computed schedule (all 53 rows agree) and that the workbook has zero formula errors after recalculation.
- Confirmed the milestone count (5) and the 18% cushion are inside the lecture's guidance (≤5 milestones; 15–20% cushion for a team new to the domain).
- Read the generated sections and edited wording where needed before submission.

## Limitations I am aware of

- Story-point values and the 2-days-per-point conversion are assumptions, not measured velocity; they will be re-calibrated after the first sprints (noted in Section 9.5).
- The schedule has not been resource-levelled; Backend/API is assigned to 17 of 29 deliverables and some November bars assume full availability.
- Page numbers in the table of contents were computed from a LibreOffice rendering; Word may paginate slightly differently (right-click → Update Field fixes it).
