from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

plt.style.use('default')

fig = plt.figure()
ax = Axes3D(fig)

ax.plot([2], [3], [5], 'ko')

ax.plot([0, 2], [0, 0], [0, 0], 'r-', linewidth=3, label='x')
ax.plot([2, 2], [0, 3], [0, 0], 'g-', linewidth=3, label='z')
ax.plot([2, 2], [3, 3], [0, 5], 'b-', linewidth=3, label='y')

ax.plot([-5, 5], [0, 0], [0, 0], 'k', linewidth=1)
ax.plot([0, 0], [-5, 5], [0, 0], 'k', linewidth=1)
ax.plot([0, 0], [0, 0], [-5, 5], 'k', linewidth=1)

ax.set_title('3d view x,y,z', loc='left')
ax.set_xlabel('x-axis', fontsize=10)
ax.set_zlabel('y-axis', fontsize=10)
ax.set_ylabel('z-axis', fontsize=10)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, prop={'size': 20})

ax.axis('equal')
plt.show()
