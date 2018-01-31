import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import style
import numpy as np
from mpl_toolkits.mplot3d import axes3d

import trajectory

print(plt.style.available)
style.use(['fivethirtyeight', 'fast'])


def clear_axes(axes):
    for axis in axes:
        axis.clear()


def plot_axes(axis, data, label):
    axis[0].plot(data[0], data[2], data[1], label=label)
    axis[1].plot(data[0], data[1], label=label)
    axis[2].plot(data[2], data[1], label=label)
    axis[3].plot(data[0], data[2], label=label)


fig = plt.figure()

t1 = trajectory.Trajectory(x=-8, y=5, z=5, h0=2)
t1data = t1.calculate_trajectory()

t2 = trajectory.Trajectory(x=10, y=5, z=10)
t2data = t2.calculate_trajectory()

t3 = trajectory.Trajectory(x=7, y=10, z=6)
t3data = t3.calculate_trajectory()

ax1 = fig.add_subplot(221, projection='3d')
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

axes = [ax1, ax2, ax3, ax4]

ax1.set_title('3d view', loc='left')
ax1.set_xlabel('x-axis', fontsize=10)
ax1.set_ylabel('z-axis', fontsize=10)
ax1.set_zlabel('y-axis', fontsize=10)

ax2.set_title('side view x,y', loc='left')
ax2.set_xlabel('x-axis', fontsize=10)
ax2.set_ylabel('y-axis', fontsize=10)

ax3.set_title('side view z,y', loc='left')
ax3.set_xlabel('z-axis', fontsize=10)
ax3.set_ylabel('y-axis', fontsize=10)

ax4.set_title('top view', loc='left')
ax4.set_xlabel('x-axis', fontsize=10)
ax4.set_ylabel('z-axis', fontsize=10)

plot_axes(axes, t1data, '1')
plot_axes(axes, t2data, '2')
plot_axes(axes, t3data, '3')

ax2.grid(color='grey', linestyle='--', linewidth='0.5')
ax3.grid(color='grey', linestyle='--', linewidth='0.5')
ax4.grid(color='grey', linestyle='--', linewidth='0.5')

axes_style = 'tight'

ax1.axis(axes_style)
ax2.axis(axes_style)
ax3.axis(axes_style)
ax4.axis(axes_style)

# plt.draw()

plt.show()
