import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import datetime as dt

D = lambda s: dt.datetime.strptime(s, '%b %d %Y')
PURPLE = '#7E66B0'; NAVY = '#1F3A5F'; BLUE = '#2E6DA8'; GREEN = '#3E9C6E'; AMBER = '#E2A03A'; GREY = '#B5B5B5'; RED = '#C0392B'
rows = [
    ('P0.1', 'Requirements finalization (SRS v1.0 -> v6.0, use cases, NFRs)', 'Sep 8 2026', 'Oct 9 2026', 'p', '24 wd'),
    ('P0.2', 'Architecture, data model and UX design', 'Sep 21 2026', 'Oct 16 2026', 'p', '20 wd'),
    ('1', 'Accounts, Authentication & Security', 'Nov 4 2026', 'Dec 14 2026', 'm', ''),
    ('1.1', 'Driver Accounts', 'Nov 4 2026', 'Nov 16 2026', 'mvp', '13 SP · 9 wd'),
    ('1.2', 'Operator & Administrator Access Control', 'Nov 17 2026', 'Dec 2 2026', 'mvp', '15 SP · 10 wd'),
    ('1.3', 'Fraud & Abuse Prevention', 'Nov 30 2026', 'Dec 14 2026', 'beta', '11 SP · 11 wd'),
    ('1.4', 'Data Protection & Audit', 'Nov 17 2026', 'Dec 3 2026', 'beta', '11 SP · 11 wd'),
    ('2', 'Availability, Map & Navigation', 'Nov 20 2026', 'Dec 10 2026', 'm', ''),
    ('2.1', 'Real-Time Availability Engine', 'Nov 20 2026', 'Dec 4 2026', 'mvp', '13 SP · 9 wd'),
    ('2.2', 'Facility Search & Map', 'Nov 20 2026', 'Dec 3 2026', 'mvp', '15 SP · 8 wd'),
    ('2.3', 'Navigation Hand-off', 'Dec 4 2026', 'Dec 10 2026', 'mvp', '5 SP · 5 wd'),
    ('3', 'Reservations & Permits', 'Jan 5 2027', 'Feb 3 2027', 'm', ''),
    ('3.1', 'Reservation Engine', 'Jan 5 2027', 'Jan 20 2027', 'mvp', '21 SP · 11 wd'),
    ('3.2', 'Active Session Management', 'Jan 27 2027', 'Feb 3 2027', 'beta', '8 SP · 6 wd'),
    ('3.3', 'Entry Credentials', 'Jan 21 2027', 'Jan 26 2027', 'mvp', '6 SP · 4 wd'),
    ('3.4', 'Monthly Permits', 'Jan 21 2027', 'Jan 28 2027', 'beta', '8 SP · 6 wd'),
    ('4', 'Payments, Receipts & Finance', 'Nov 4 2026', 'Feb 10 2027', 'm', ''),
    ('4.1', 'Payment Processing', 'Nov 4 2026', 'Nov 25 2026', 'mvp', '16 SP · 16 wd'),
    ('4.2', 'Receipts & History', 'Jan 21 2027', 'Jan 26 2027', 'beta', '5 SP · 4 wd'),
    ('4.3', 'Finance Tools', 'Jan 27 2027', 'Feb 10 2027', 'beta', '16 SP · 11 wd'),
    ('5', 'Operator Dashboard & Facility Management', 'Dec 3 2026', 'Feb 4 2027', 'm', ''),
    ('5.1', 'Facility Configuration', 'Dec 3 2026', 'Dec 14 2026', 'mvp', '12 SP · 8 wd'),
    ('5.2', 'Pricing', 'Dec 15 2026', 'Jan 4 2027', 'mvp', '16 SP · 11 wd'),
    ('5.3', 'Occupancy Monitoring', 'Dec 15 2026', 'Dec 22 2026', 'beta', '8 SP · 6 wd'),
    ('5.4', 'Reservation Management & Lane Assist', 'Jan 27 2027', 'Feb 4 2027', 'beta', '10 SP · 7 wd'),
    ('6', 'Reporting & Analytics', 'Dec 7 2026', 'Feb 9 2027', 'm', ''),
    ('6.1', 'Operator Reports', 'Jan 27 2027', 'Feb 9 2027', 'beta', '14 SP · 10 wd'),
    ('6.2', 'Open Data', 'Dec 7 2026', 'Dec 11 2026', 'beta', '5 SP · 5 wd'),
    ('7', 'Notifications', 'Nov 4 2026', 'Nov 20 2026', 'm', ''),
    ('7.1', 'Notification Service', 'Nov 4 2026', 'Nov 18 2026', 'mvp', '11 SP · 11 wd'),
    ('7.2', 'Preferences', 'Nov 19 2026', 'Nov 20 2026', 'mvp', '1 SP · 2 wd'),
    ('8', 'Hardware Integration & Platform Infrastructure', 'Oct 19 2026', 'Dec 17 2026', 'm', ''),
    ('8.1', 'Cloud Platform', 'Oct 19 2026', 'Nov 3 2026', 'mvp', '18 SP · 12 wd'),
    ('8.2', 'Gate & LPR Integration', 'Nov 4 2026', 'Nov 19 2026', 'mvp', '18 SP · 12 wd'),
    ('8.3', 'Facility Edge Service (+8.3.3 in v6.0)', 'Nov 20 2026', 'Dec 17 2026', 'mvp', '18 SP · 18 wd'),
    ('8.4', 'Client Application Shells', 'Oct 19 2026', 'Oct 28 2026', 'mvp', '15 SP · 8 wd'),
    ('8.5', 'Release & Delivery Automation (new in v6.0)', 'Nov 4 2026', 'Nov 25 2026', 'mvp', '8 SP · 16 wd'),
    ('9', 'Quality Assurance & Release', 'Oct 19 2026', 'Mar 17 2027', 'm', ''),
    ('9.1', 'Test Infrastructure', 'Oct 19 2026', 'Nov 16 2026', 'mvp', '21 SP · 21 wd'),
    ('9.2', 'Performance, Security & Usability Validation', 'Jan 27 2027', 'Feb 10 2027', 'beta', '16 SP · 11 wd'),
    ('9.3', 'Release Management', 'Mar 4 2027', 'Mar 17 2027', 'mvp', '15 SP · 10 wd'),
    ('T1', 'MVP integration & end-to-end testing', 'Jan 27 2027', 'Feb 9 2027', 't', '10 wd'),
    ('C1', 'Schedule cushion – MVP (5 working days)', 'Feb 10 2027', 'Feb 17 2027', 'c', '5 wd'),
    ('T2', 'Beta regression, stress-test run and security sign-off', 'Feb 18 2027', 'Mar 3 2027', 't', '10 wd'),
    ('C2', 'Schedule cushion – Final (13 working days)', 'Mar 18 2027', 'Apr 5 2027', 'c', '13 wd'),
]
miles = [('Kickoff\nSep 8', 'Sep 8 2026', 0), ('Design approved\nOct 16', 'Oct 16 2026', 1), ('MVP acceptance\nFeb 17', 'Feb 17 2027', 0),
         ('Beta release\nMar 3', 'Mar 3 2027', 1), ('Final delivery\nApr 5', 'Apr 5 2027', 0)]
col = {'p': PURPLE, 'm': NAVY, 'mvp': BLUE, 'beta': GREEN, 't': AMBER, 'c': GREY}

fig = plt.figure(figsize=(15.5, 12.5), dpi=200)
ax = fig.add_axes([0.245, 0.03, 0.745, 0.865])
n = len(rows)
for i, (rid, name, s, e, k, lab) in enumerate(rows):
    y = n - i
    a = D(s); b = D(e) + dt.timedelta(days=1)
    h = 0.32 if k == 'm' else 0.62
    ax.barh(y, (b - a).days, left=a, height=h, color=col[k], edgecolor='white' if k != 'c' else '#888',
            hatch='//' if k == 'c' else None, lw=0.8)
    if k == 'mvp' and rid in ('8.3', '8.5'):
        ax.barh(y, (b - a).days, left=a, height=h, color='none', edgecolor=RED, lw=1.6)
    if lab:
        ax.text(b + dt.timedelta(days=2), y, lab, va='center', fontsize=7.6, color='#333')
    italic = k in ('p', 't', 'c')
    bold = k == 'm'
    ax.text(-0.325, y, rid, transform=ax.get_yaxis_transform(), va='center', ha='left', fontsize=8.6,
            fontweight='bold' if bold else 'normal', style='italic' if italic else 'normal', color=NAVY if bold else '#111')
    ax.text(-0.29 if not bold and not italic and '.' in rid else -0.29, y, ('     ' if (not bold and not italic) else '') + name,
            transform=ax.get_yaxis_transform(), va='center', ha='left', fontsize=8.6, fontweight='bold' if bold else 'normal',
            style='italic' if italic else 'normal', color=NAVY if bold else '#111')
top = n + 2.4
for label, dd, lvl in miles:
    x = D(dd) + dt.timedelta(hours=12)
    ax.axvline(x, color=RED, ls='--', lw=1, alpha=0.8)
    ax.plot([x], [n + 1.2], marker='D', color=RED, ms=9, clip_on=False)
    ax.text(x, n + 1.9 + 0.9 * lvl, label, ha='center', va='bottom', color=RED, fontsize=8.6, fontweight='bold')
ax.axvspan(D('Dec 24 2026'), D('Jan 4 2027'), color='#EFEBD5', alpha=0.8, zorder=0)
ax.text(D('Dec 29 2026'), 0.25, 'holidays', fontsize=7, color='#777', ha='center')
ax.set_ylim(0, n + 4.2)
ax.set_xlim(D('Sep 1 2026'), D('Apr 20 2027'))
ax.set_yticks([])
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=0))
ax.tick_params(axis='x', labelsize=8.6, top=True, labeltop=True)
ax.grid(axis='x', which='major', color='#AAA', lw=0.8)
ax.grid(axis='x', which='minor', color='#EEE', lw=0.6)
for s in ('left', 'right'):
    ax.spines[s].set_visible(False)
ax.set_axisbelow(True)
fig.suptitle('Smart Parking Platform – Project Timeline v6.0 (Sep 2026 – Apr 2027)\n'
             'Bars: WBS Level-2 deliverables · FS/SS dependencies drive start dates · 1 SP ≈ 2 blended developer-days',
             fontsize=11.5, y=0.985)
leg = [Patch(color=PURPLE, label='Requirements & design (Phase 0)'), Patch(color=NAVY, label='Module summary (Level 1)'),
       Patch(color=BLUE, label='MVP-scope deliverable (Level 2)'), Patch(color=GREEN, label='Beta-scope deliverable (Level 2)'),
       Patch(color=AMBER, label='Integration / end-to-end test window'), Patch(facecolor=GREY, edgecolor='#888', hatch='//', label='Schedule cushion (18%)'),
       Patch(facecolor='white', edgecolor=RED, lw=1.6, label='Added or changed in v6.0'),
       Line2D([0], [0], marker='D', color='w', markerfacecolor=RED, markersize=8, label='Milestone')]
ax.legend(handles=leg, loc='lower left', ncol=2, fontsize=8, framealpha=0.95)
fig.savefig('fig4_gantt_v6.png', dpi=200)
print('ok')
