from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

plt.style.use("default")

fig = plt.figure()
ax = fig.add_subplot(111)

step = 0.001

X = np.arange(5, 12 + step, step)

st = 50 / (1 + np.e ** -(X - 6))
vt = (50 * np.e ** (X - 6)) / ((np.e ** (X - 6) + 1) ** 2)

lw = 2

ax.plot(X, st, linewidth=lw, label='s(t)')
ax.plot(X, vt, linewidth=lw, label='v(t)')

# ax.axis('equal')
ax.grid(True, color='grey', linestyle='--')

rect = Polygon([(6.4, 35), (9.6, 35), (9.6, 50), (6.4, 50)], **{'alpha': 0.5, 'linewidth': 2, 'linestyle': '-'})
#ax.add_patch(rect)

handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles, labels, prop={'size': 20})

for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(17)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(17)

plt.show()
