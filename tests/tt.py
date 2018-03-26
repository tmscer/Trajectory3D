from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import numpy as np


plt.style.use('default')

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot([4], [2], 'ko')

ax.plot([0, 4], [0, 0], 'r-', label='x', linewidth=3)
ax.plot([4, 4], [0, 2], 'b-', label='y', linewidth=3)


ax.plot([-5, 5], [0, 0], 'k-', linewidth=1)
ax.plot([0, 0], [-5, 5], 'k-', linewidth=1)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size': 20})

ax.grid()

ax.axis('equal')
plt.show()
