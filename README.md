# Smart Parking Platform — Project Management Document

**Course:** CIS 4374 – Information Systems Project Management, University of Houston, Fall 2026
**Company:** $oftware ¢orp (fictitious software development studio)
**Project Manager:** Faiz Hajiani

This repository holds the living project document for the **Smart Parking Platform** — a web and mobile system that lets drivers locate, reserve, navigate to, and pay for garage parking in real time, and gives parking operators live occupancy, pricing, and revenue tools.

The document grows every week as the course covers a new project-management topic. Each weekly homework adds or refines a section, and the version number is bumped with every submission. Only the current version of the document is kept in the repository; earlier versions remain available in the Git history.

## Current document

| File | Version | Date | Contents |
|---|---|---|---|
| [`SmartParking_SRS_v6.0.docx`](SmartParking_SRS_v6.0.docx) | 6.0 | Oct 15, 2026 | Sections 1–15: vision and scope, market research, overall description, functional and non-functional requirements, use cases (Sections 1–7); Work Breakdown Structure, 369 story points (8); estimation and timeline (9); sprint backlog, board management and CI/CD (10); risk management (11); quality management (12); communication plan (13); resource and cost management, cost baseline $2,146,328 (14); references (15). |
| [`SmartParking_Gantt_v2.0.xlsx`](SmartParking_Gantt_v2.0.xlsx) | 2.0 | Sep 17, 2026 | Editable Gantt model from HW2 (assumptions → WBS → Gantt). Superseded for dates by the v6.0 Gantt chart in Section 9.4 / `figures/fig4_gantt_v6.png`. |
| [`SmartParking_Backlog_v3.0.csv`](SmartParking_Backlog_v3.0.csv) | 3.0 | Sep 24, 2026 | 84-card backlog behind the Jira board as of HW3. The v6.0 work items 8.3.3, 8.5.1 and 8.5.2 are added at Sprint 1 planning (see Section 10). |

## What changed in v6.0 (HW6, October 15, 2026)

Full review of every section after Lecture 7; no new chapters.

- Requirements FR-27 to FR-30 and use cases UC-19 to UC-23 added for WBS work that had no use case
- WBS work items 8.3.3, 8.5.1 and 8.5.2 added (total now 369 story points), with schedule rows; Gantt chart and WBS diagram redrawn (`figures/`)
- Sprint 1 capacity reconciled team by team; new Section 10.6 on source control, the CI/CD pipeline and board integration
- Risks T-6, F-5 and P-5 added and S-3 re-rated; new stakeholders in Section 4.2 and the communication plan
- Cost plan: DevOps engineer full-time from build start and a production-parity staging environment; cost baseline now $2,146,328; cashflow and RACI updated
- AI usage log: [`ai-usage/AI_Usage_Log_HW6.md`](ai-usage/AI_Usage_Log_HW6.md)

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-09-08 | HW1 – Project kickoff and SRS initiation |
| 2.0 | 2026-09-17 | HW2 – Work Breakdown Structure, estimation, draft timeline and Gantt chart |
| 3.0 | 2026-09-24 | HW3 – Sprint backlog, board conventions and Sprint 1 plan |
| 4.0 | 2026-10-01 | HW4 – Risk management (Section 11), quality management (Section 12), communication plan (Section 13) |
| 5.0 | 2026-10-08 | HW5 – Resource and cost management (Section 14): roles, bottom-up cost plan, reserves, cashflow, RACI |
| 6.0 | 2026-10-15 | HW6 – Full documentation update after Lecture 7 (see above) |

## Repository layout

```
/SmartParking_SRS_v6.0.docx      ← current project document (Word)
/SmartParking_Gantt_v2.0.xlsx    ← editable Gantt / schedule model (Excel, HW2)
/SmartParking_Backlog_v3.0.csv   ← backlog behind the Jira sprint board (HW3)
/figures/                        ← diagrams embedded in the document
    fig1_context.png               competitive placement map (v1.0)
    fig2_positioning.png           system context diagram (v1.0)
    fig3_wbs_tree.png              WBS levels 0–2 (v2.0)
    fig3_wbs_v6.png                WBS levels 0–2 (v6.0)        ← script: wbs_v6.py
    fig4_gantt_v2.png              draft Gantt chart (v2.0)
    fig4_gantt_v6.png              project timeline (v6.0)      ← script: gantt_v6.py
    fig5_sprint_board.png          Sprint 1 board (v3.0)
    fig6_product_backlog.png       full product backlog (v3.0)
/ai-usage/                       ← AI usage log, one file per homework
    AI_Usage_Log_HW2.md
    AI_Usage_Log_HW3.md
    AI_Usage_Log_HW6.md
/README.md                       ← this file
```

## Weekly deliverable checklist

1. Update the document for the week's topic and bump the version.
2. Commit and push.
3. Record a 1–2 minute stakeholder update video (Teams, camera on).
4. Submit the repo link and the MS Streams video link on Canvas by Thursday 11:59 PM.
