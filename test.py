import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib import style
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import math

import trajectory

print(plt.style.available)
style.use(['fivethirtyeight', 'fast'])


def clear_axes(axes):
    for axis in axes:
        axis.clear()


def plot_axes(axis, data, label):
    axis[0].plot(data[0], data[2], data[1], label=label)
    axis[0].plot([data[0][0]], data[2][0], [data[1][0]], '*')

    axis[1].plot(data[0], data[1], label=label)
    axis[1].plot([data[0][0]], [data[1][0]], '*')

    axis[2].plot(data[2], data[1], label=label)
    axis[2].plot([data[2][0]], [data[1][0]], '*')

    axis[3].plot(data[0], data[2], label=label)
    axis[3].plot([data[0][0]], [data[2][0]], '*')


fig = plt.figure()

ax1 = fig.add_subplot(221, projection='3d')
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

axes = [ax1, ax2, ax3, ax4]


def label_axes():
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


ax2.grid(color='grey', linestyle='--', linewidth='0.5')
ax3.grid(color='grey', linestyle='--', linewidth='0.5')
ax4.grid(color='grey', linestyle='--', linewidth='0.5')


def gen():
    r = list(range(40, 80, 1))
    r.extend(list(reversed(r))[1:])
    print(r)
    i = 0
    while True:
        yield r[i] / 2
        i += 1
        if not i < len(r):
            i = 0


ge = gen()

t1 = trajectory.Trajectory(xv=8, yv=5, zv=-5, x0=5, y0=0, z0=10)

t2 = trajectory.Trajectory(v0=15, alpha=math.radians(55), theta=math.radians(200), x0=-1, y0=6, z0=-3)

t3 = trajectory.Trajectory(xv=7, yv=10, zv=0, y0=5, z0=10)


print(t1.__dict__)
print(t2.__dict__)
print(t3.__dict__)

plot_axes(axes, t1.calculate_trajectory(), '1')
plot_axes(axes, t2.calculate_trajectory(), '2')
plot_axes(axes, t3.calculate_trajectory(), '3')


def animate(i):
    global t1, t2, t3, ge, axes
    #angle = math.radians(next(ge))
    #t1.alpha = angle
    #t1.theta = 2 * angle
    clear_axes(axes)
    label_axes()
    plot_axes(axes, t1.calculate_trajectory(), '1')
    plot_axes(axes, t2.calculate_trajectory(), '2')
    plot_axes(axes, t3.calculate_trajectory(), '3')


anim = ani.FuncAnimation(fig, animate, 250)
axes_style = 'tight'

ax1.axis(axes_style)
ax2.axis(axes_style)
ax3.axis(axes_style)
ax4.axis(axes_style)

# plt.draw()
plt.title("")
plt.show()
