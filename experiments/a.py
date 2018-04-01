from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import math

plt.style.use('default')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.axis('equal')
step = 1 / 1000
theta = np.arange(0, 2 * np.pi + step, step)
circle = np.cos(theta) + 1j * np.sin(theta)
ax.plot(circle.real, circle.imag, linewidth=2)
ax.plot([0], [0], 'ko')
#ax.plot([0, 0], [-1, 1], '0.8')
#ax.plot([-1, 1], [0, 0], '0.8')

ax.arrow(1, 0, 0, 0.75, fc='k', ec='k', linewidth=2, head_width=0.05, head_length=0.05)
ax.arrow(1, 0, -0.5, 0.0, fc='k', ec='k', linewidth=2, head_width=0.05, head_length=0.05)

ax.plot([0], [1.55], 'w')

ax.arrow(math.sqrt(2)/2, math.sqrt(2)/2, -math.sqrt(0.75 / 2), math.sqrt(0.75 / 2), fc='k', ec='k', linewidth=2, head_width=0.05, head_length=0.05)
ax.arrow(math.sqrt(2)/2, math.sqrt(2)/2, -math.sqrt(2) / 4, -math.sqrt(2) / 4, fc='k', ec='k', linewidth=2, head_width=0.05, head_length=0.05)

theta2 = np.arange(0, 0.25 * np.pi + step, step)
qcircle = np.cos(theta2) + 1j * np.sin(theta2)

verts = [(0, 0)] + list(zip(qcircle.real, qcircle.imag))
poly = Polygon(verts, **{'facecolor': 'grey', 'alpha': 0.33})

ax.add_patch(poly)

plt.show()
