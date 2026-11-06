# Smart Parking Platform — Project Management Document

Course project for **CIS 4374 Information Systems Project Management**, University of Houston, Fall 2026 (Instructor: Dr. Otto Dobretsberger).
Fictitious studio: **$oftware ¢orp**. Client: Bayou City Parking Group (fictional). Project Manager: **Faiz Hajiani**.

The product is a web and mobile system that lets drivers find, reserve, navigate to and pay for garage parking in real time, and gives operators live occupancy, pricing and revenue tools across their facilities.

## Current version: 8.0 (November 5, 2026)

**`SmartParking_SRS_v8.0.docx`** — the single, continuous project document (90 pages, Sections 1–17). Superseded versions are removed from the repository; their history is in git.

| Section | Content |
|---|---|
| 1–3 | Introduction, vision and scope, market research *(finished)* |
| 4–7 | Overall description, 30 functional and 16 non-functional requirements, 23 use cases |
| 8–9 | Work breakdown structure (369 story points), estimation, milestones M0–M4, Gantt chart |
| 10 | Sprint backlog, Jira board, source control and CI/CD pipeline |
| 11–13 | Risk register (21 risks), quality management, communication plan |
| 14 | Resource and cost management — cost baseline **$2,146,328**, cashflow, RACI |
| 15 | Stakeholder management, charters and team leadership |
| **16** | **Project closure report (internal draft)** *(new in v8.0)* |
| 17 | References |

### What changed in v8.0 (HW8, Lecture 9 — Monitoring, Reporting and Project Closure)
- **Section 16 added: Project Closure Report (internal draft).** Executive summary and project snapshot (Table 16.1), objectives and deliverables with acceptance evidence (16.2), achievements and shortfalls (16.3), schedule and budget comparison with actuals to date plus a KPI dashboard and the **Sprint 1 burndown chart (Figure 10)** (16.4), lessons-learned register L-1 to L-11 (16.5), recommendations for future projects (16.6), the seven-step closure checklist, ethical-accountability statement and sign-off (16.7).
- Written deliberately as a draft at the end of Sprint 1: structure and measures fixed now, actuals filled to Nov 5, 2026, and items that depend on the final outcome marked "to be completed at M4".
- Cross-reference added in Section 13.4; Lecture 9 added to the references, which moved to Section 17. No other section changed.
- **`PostMortem_Google_Stadia_v1.0.docx`** — the HW8 post-mortem of a failed technology (Google Stadia, 2019–2023), a **separate document** as the homework requires; it is not part of the project document.

### What changed in v7.0 (HW7, Lecture 8 — Managing Teams and Stakeholders)
- Section 15 added: power–interest assessment of 16 stakeholders, the power–interest grid (Figure 7), engagement plan, project charter (Figure 8), team charter (Figure 9), leadership and conflict-resolution plan.

## Repository layout

```
SmartParking_SRS_v8.0.docx        main project document (always the latest version only)
PostMortem_Google_Stadia_v1.0.docx  HW8 post-mortem of a failed technology (separate document, as required)
SmartParking_Gantt_v2.0.xlsx      editable schedule model from HW2 (dates superseded by the v7.0 Gantt chart)
SmartParking_Backlog_v3.0.csv     84-card backlog behind the Jira board as of HW3
figures/                          diagrams embedded in the document and their generator scripts
  power_interest_grid_v7.png        Figure 7 — stakeholder power–interest grid
  project_charter_v7.png / .pdf     Figure 8 — project charter (one page)
  team_charter_v7.png / .pdf        Figure 9 — team charter (one page)
  sprint1_burndown_v8.png           Figure 10 — Sprint 1 burndown chart
  gantt_v6.py, wbs_v6.py, ...       earlier figure scripts
ai-usage/                         one AI usage log per homework (AI_Usage_Log_HW1.md … HW8.md)
```

## Version history

| Version | Date | Homework | Summary |
|---|---|---|---|
| 1.0 | Sep 8, 2026 | HW1 | Vision and scope, market research, requirements, 18 use cases |
| 2.0 | Sep 17, 2026 | HW2 | WBS, estimation, milestones, Gantt chart |
| 3.0 | Sep 24, 2026 | HW3 | Sprint backlog and Jira board, Sprint 1 commitment |
| 4.0 | Oct 1, 2026 | HW4 | Risk management, quality management, communication plan |
| 5.0 | Oct 8, 2026 | HW5 | Resource and cost management, RACI |
| 6.0 | Oct 15, 2026 | HW6 | Full review: FR-27–30, UC-19–23, CI/CD (10.6), new risks, cost baseline $2,146,328 |
| 7.0 | Oct 29, 2026 | HW7 | Stakeholder analysis (power–interest grid), project charter, team charter, leadership and conflict plan |
| **8.0** | **Nov 5, 2026** | **HW8** | **Project closure report (internal draft): KPI dashboard, Sprint 1 burndown, lessons learned, recommendations, closure checklist; separate Google Stadia post-mortem** |

## Weekly process
1. Update the document and bump the version (major for new sections, minor for incremental changes).
2. Regenerate any figures, commit and push; remove the superseded document version.
3. Record a 1–2 minute stakeholder update video in Teams (camera on; screen-share figures when the homework asks to show them).
4. Submit the repository link and the Microsoft Stream link on Canvas by Thursday 11:59 PM, with the AI usage log for the week in `ai-usage/`.
