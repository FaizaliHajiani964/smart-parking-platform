import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import textwrap

DARK = '#1F3A5F'; MOD = '#2E6DA8'; L2F = '#E6EDF5'; L2E = '#B8C4D2'; LINE = '#555555'; TXT = '#1a1a1a'
mods = [
    ('1. Accounts, Authentication & Security', 50, [('1.1 Driver Accounts', 13, 4), ('1.2 Operator & Administrator Access Control', 15, 4), ('1.3 Fraud & Abuse Prevention', 11, 3), ('1.4 Data Protection & Audit', 11, 3)]),
    ('2. Availability, Map & Navigation', 33, [('2.1 Real-Time Availability Engine', 13, 3), ('2.2 Facility Search & Map', 15, 4), ('2.3 Navigation Hand-off', 5, 2)]),
    ('3. Reservations & Permits', 43, [('3.1 Reservation Engine', 21, 4), ('3.2 Active Session Management', 8, 2), ('3.3 Entry Credentials', 6, 2), ('3.4 Monthly Permits', 8, 2)]),
    ('4. Payments, Receipts & Finance', 37, [('4.1 Payment Processing', 16, 3), ('4.2 Receipts & History', 5, 2), ('4.3 Finance Tools', 16, 3)]),
    ('5. Operator Dashboard & Facility Management', 46, [('5.1 Facility Configuration', 12, 3), ('5.2 Pricing', 16, 3), ('5.3 Occupancy Monitoring', 8, 2), ('5.4 Reservation Management & Lane Assist', 10, 2)]),
    ('6. Reporting & Analytics', 19, [('6.1 Operator Reports', 14, 3), ('6.2 Open Data', 5, 1)]),
    ('7. Notifications', 12, [('7.1 Notification Service', 11, 3), ('7.2 Preferences', 1, 1)]),
    ('8. Hardware Integration & Platform Infrastructure', 77, [('8.1 Cloud Platform', 18, 3), ('8.2 Gate & LPR Integration', 18, 3), ('8.3 Facility Edge Service', 18, 3), ('8.4 Client Application Shells', 15, 3), ('8.5 Release & Delivery Automation', 8, 2)]),
    ('9. Quality Assurance & Release', 52, [('9.1 Test Infrastructure', 21, 3), ('9.2 Performance, Security & Usability Validation', 16, 3), ('9.3 Release Management', 15, 3)]),
]
NEW = {'8.3 Facility Edge Service', '8.5 Release & Delivery Automation'}

W, H = 13.2, 10.03
fig = plt.figure(figsize=(W, H), dpi=200)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

def box(x, y, w, h, fc, ec, text, color, bold, fs):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=0.5', fc=fc, ec=ec, lw=1))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', color=color, fontsize=fs,
            fontweight='bold' if bold else 'normal', linespacing=1.15)

# level 0
box(28, 93.2, 44, 5.4, DARK, DARK, 'Smart Parking Platform\n(Level 0 – project, 369 story points)', 'white', True, 11)
colw = 18.6; gap = 1.0; x0 = 0.9
L2h = 7.0; L2gap = 1.4
rows = [(mods[:5], 82.0), (mods[5:], 38.5)]
ax.plot([50, 50], [93.2, 90.5], color=LINE, lw=1)
ax.plot([x0 + colw / 2 - 9.45 + 9.45 - 9.45 + 0.0, 0], [0, 0], alpha=0)
# trunk
ax.plot([0.45, 0.45], [90.5, 48.5], color=LINE, lw=1)
for (ms, ytop) in rows:
    centers = [x0 + i * (colw + gap) + colw / 2 for i in range(len(ms))]
    ybar = ytop + 8.5 if ytop > 50 else ytop + 10.0
    ax.plot([0.45, centers[-1]], [ybar, ybar], color=LINE, lw=1)
    for i, (name, sp, l2s) in enumerate(ms):
        cx = centers[i]; x = cx - colw / 2
        ax.plot([cx, cx], [ybar, ytop + 6.2], color=LINE, lw=1)
        label = '\n'.join(textwrap.wrap(name, 26)) + f'\n({sp} SP)'
        box(x, ytop, colw, 6.2, MOD, MOD, label, 'white', True, 10)
        y = ytop - 1.0
        for (n, s, k) in l2s:
            y -= L2h
            bx = x + 2.6; bw = colw - 2.6
            ec = '#C0392B' if n in NEW else L2E
            box(bx, y, bw, L2h - 0.7, L2F, ec, '\n'.join(textwrap.wrap(n, 30)) + f'\n{s} SP · {k} item' + ('s' if k > 1 else ''),
                TXT, False, 8.4)
            ax.plot([x + 1.4, x + 1.4, bx], [y + L2h - 0.2, y + (L2h - 0.7) / 2, y + (L2h - 0.7) / 2], color='#7A8CA5', lw=0.9)
ax.text(99, 1.0, 'Red outline: deliverable added or changed in v6.0', ha='right', va='bottom', fontsize=8.5, color='#C0392B')
fig.savefig('fig3_wbs_v6.png', dpi=200)
print('ok')
