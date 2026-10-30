# Smart Parking Platform — Project Management Document

Course project for **CIS 4374 Information Systems Project Management**, University of Houston, Fall 2026 (Instructor: Dr. Otto Dobretsberger).
Fictitious studio: **$oftware ¢orp**. Client: Bayou City Parking Group (fictional). Project Manager: **Faiz Hajiani**.

The product is a web and mobile system that lets drivers find, reserve, navigate to and pay for garage parking in real time, and gives operators live occupancy, pricing and revenue tools across their facilities.

## Current version: 7.0 (October 29, 2026)

**`SmartParking_SRS_v7.0.docx`** — the single, continuous project document (80 pages, Sections 1–16). Superseded versions are removed from the repository; their history is in git.

| Section | Content |
|---|---|
| 1–3 | Introduction, vision and scope, market research *(finished)* |
| 4–7 | Overall description, 30 functional and 16 non-functional requirements, 23 use cases |
| 8–9 | Work breakdown structure (369 story points), estimation, milestones M0–M4, Gantt chart |
| 10 | Sprint backlog, Jira board, source control and CI/CD pipeline |
| 11–13 | Risk register (21 risks), quality management, communication plan |
| 14 | Resource and cost management — cost baseline **$2,146,328**, cashflow, RACI |
| **15** | **Stakeholder management, charters and team leadership** *(new in v7.0)* |
| 16 | References |

### What changed in v7.0 (HW7, Lecture 8 — Managing Teams and Stakeholders)
- **Section 15 added.** Power–interest assessment of 16 stakeholders (Table 15.1), the power–interest grid (Figure 7), engagement strategy by quadrant and an engagement plan for the key stakeholders.
- **Project charter** (Figure 8) and **team charter** (Figure 9) as one-page, signable documents, each with a text version in the document. Both are also in `figures/` as PNG and PDF.
- **Leadership approach and conflict-resolution plan** (15.6), including the lecture's "API fails before release" scenario applied to this project.
- Cross-references added in Sections 4.2 and 13; the Project Manager is now named consistently in Table 14.1; Lecture 8 added to the references, which moved to Section 16. No other section changed.

## Repository layout

```
SmartParking_SRS_v7.0.docx        main project document (always the latest version only)
SmartParking_Gantt_v2.0.xlsx      editable schedule model from HW2 (dates superseded by the v7.0 Gantt chart)
SmartParking_Backlog_v3.0.csv     84-card backlog behind the Jira board as of HW3
figures/                          diagrams embedded in the document and their generator scripts
  power_interest_grid_v7.png        Figure 7 — stakeholder power–interest grid
  project_charter_v7.png / .pdf     Figure 8 — project charter (one page)
  team_charter_v7.png / .pdf        Figure 9 — team charter (one page)
  gantt_v6.py, wbs_v6.py, ...       earlier figure scripts
ai-usage/                         one AI usage log per homework (AI_Usage_Log_HW1.md … HW7.md)
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
| **7.0** | **Oct 29, 2026** | **HW7** | **Stakeholder analysis (power–interest grid), project charter, team charter, leadership and conflict plan** |

## Weekly process
1. Update the document and bump the version (major for new sections, minor for incremental changes).
2. Regenerate any figures, commit and push; remove the superseded document version.
3. Record a 1–2 minute stakeholder update video in Teams (camera on; screen-share figures when the homework asks to show them).
4. Submit the repository link and the Microsoft Stream link on Canvas by Thursday 11:59 PM, with the AI usage log for the week in `ai-usage/`.
