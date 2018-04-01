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



theta2 = np.arange(-np.pi / 6, -np.pi / 6 - np.pi - step, step)
