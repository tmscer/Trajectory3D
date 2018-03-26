from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

plt.style.use("default")

fig = plt.figure()
ax = fig.add_subplot(111)

step = 0.001

X = np.arange(-10, 60 + step, step)
Y = 5 * np.sin(X) / X
#D = 3 * (X ** 2)

ax.plot([-10, 50], [0, 0], 'k')
ax.plot([0, 0], [-10, 10], 'k')

ax.plot(X, Y, linewidth=2, label='$sin(x) / x$')
#ax.plot(X, D, linewidth=2, label='$3x^2$')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size': 20})

ax.set_xlim(-5, 45)

#ax.axis('equal')
ax.grid(True)

plt.show()
