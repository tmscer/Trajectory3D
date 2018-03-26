from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import math

plt.style.use('default')
fig = plt.figure()
ax = fig.add_subplot(111)

square = Polygon([(-1, -1), (1, -1), (1, 1), (-1, 1)], **{'facecolor': 'blue', 'alpha': 0.6})

d_style = {'facecolor': 'red', 'alpha': 0.65}

rect1 = Polygon([(1.1, -1), (1.5, -1), (1.5, 1), (1.1, 1)], **d_style)
rect2 = Polygon([(-1, 1.1), (-1, 1.5), (1, 1.5), (1, 1.1)], **d_style)
square2 = Polygon([(1.1, 1.1), (1.5, 1.1), (1.5, 1.5), (1.1, 1.5)], **d_style)

fs = 32
ax.text(1.115, 1.22, r'$dx^2$', fontsize=fs)
ax.text(-0.22, 1.22, '$x·dx$', fontsize=fs)
ax.text(-0.075, -0.05, '$x^2$', fontsize=fs)

#ax.plot([-1, 1], [0, 0], 'k')
#ax.plot([0, 0], [-1, 1], 'k')

ax.add_patch(square)
ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(square2)

ax.axis('equal')

ax.set_xlim(-2, 3)
ax.set_ylim(-2, 3)

plt.show()
