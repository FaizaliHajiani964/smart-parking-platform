# Smart Parking Platform — Project Management Document

**Course:** CIS 4374 – Information Systems Project Management, University of Houston, Fall 2026
**Company:** $oftware ¢orp (fictitious software development studio)
**Project Manager:** Faiz Hajiani

This repository holds the living project document for the Smart Parking Platform — a web and mobile system that lets drivers locate, reserve, navigate to, and pay for garage parking in real time, and gives parking operators live occupancy, pricing, and revenue tools.

The document grows every week as the course covers a new project-management topic. Each weekly homework adds or refines a section, and the version number is bumped with every submission.

## Current document

| File | Version | Date | Contents |
|---|---|---|---|
| `SmartParking_SRS_v2.0.docx` | 2.0 | Sep 17, 2026 | Sections 1–7 (v1.0): vision & scope, market research, overall description, functional and non-functional requirements, 18 use cases. **New in v2.0:** Section 8 – three-level Work Breakdown Structure (9 modules, 29 deliverables, 79 work items, 356 story points); Section 9 – estimation approach, 5 milestones, dependency-driven draft schedule and Gantt chart (Sep 2026 – Apr 2027). |
| `SmartParking_Gantt_v2.0.xlsx` | 2.0 | Sep 17, 2026 | Editable Gantt chart. `Assumptions` sheet (days per story point, team sizes, cushion, holidays) → `WBS` sheet (story points per item) → `Gantt` sheet (durations, FS/SS predecessors, start/end formulas, weekly bars). Change a blue input cell and the whole timeline re-computes. |

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-09-08 | HW1 – Project Kickoff & SRS Initiation |
| 2.0 | 2026-09-17 | HW2 – Work Breakdown Structure, estimation, draft timeline and Gantt chart |

## Repository layout

```
/SmartParking_SRS_v2.0.docx     ← current project document (Word)
/SmartParking_Gantt_v2.0.xlsx   ← editable Gantt / schedule model (Excel)
/figures/                       ← diagrams embedded in the document
    fig1_context.png            ← competitive placement map (v1.0)
    fig2_positioning.png        ← system context diagram (v1.0)
    fig3_wbs_tree.png           ← WBS levels 0–2 (v2.0)
    fig4_gantt_v2.png           ← draft Gantt chart (v2.0)
/ai-usage/                      ← AI usage log, one file per homework
    AI_Usage_Log_HW2.md
/README.md                      ← this file
```

## Weekly deliverable checklist

1. Update the document for the week's topic and bump the version.
2. Commit and push.
3. Record a 1–2 minute stakeholder update video (Teams, camera on).
4. Submit the repo link and the MS Streams video link on Canvas by Thursday 11:59 PM.
