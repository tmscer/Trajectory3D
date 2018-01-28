import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

import trajectory

print("Backend in use: " + mpl.get_backend())

fig = plt.figure()

ax1 = fig.add_subplot(221, projection='3d')
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

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

g = 9.81
v0 = 30
height = 10.47
alpha = 45 * 3.14 / 180
theta = 0

t1 = trajectory.Trajectory(x=-8, y=5, z=5, h0=2)
t1data = t1.calculate_trajectory()

t2 = trajectory.Trajectory(x=10, y=5, z=10)
t2data = t2.calculate_trajectory()

ax1.plot(t1data[0], t1data[2], t1data[1], label='1')
ax1.plot(t2data[0], t2data[2], t2data[1], label='2')
ax1.legend()

ax2.plot(t1data[0], t1data[1], label='1')
ax3.plot(t1data[2], t1data[1], label='1')
ax4.plot(t1data[0], t1data[2], label='1')

ax2.plot(t2data[0], t2data[1], label='2')
ax3.plot(t2data[2], t2data[1], label='2')
ax4.plot(t2data[0], t2data[2], label='2')

ax2.grid(color='grey', linestyle='--', linewidth='0.5')
ax3.grid(color='grey', linestyle='--', linewidth='0.5')
ax4.grid(color='grey', linestyle='--', linewidth='0.5')

axis = 'tight'

ax1.axis(axis)
ax2.axis(axis)
ax3.axis(axis)
ax4.axis(axis)

#plt.draw()

plt.show()
