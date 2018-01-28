#import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
import pylab as plt
#import matplotlib.pyplot as plt
import numpy as np

import trajectory

#print(mpl.rcsetup.interactive_bk)
#print(mpl.rcsetup.non_interactive_bk)
#print(mpl.rcsetup.all_backends)

#print("Backend in use: " + mpl.get_backend())

def plot_to_plots(axis, data, label):
    axis[0].plot(data[0], data[2], data[1], label=label)
    axis[1].plot(data[0], data[1], label=label)
    axis[2].plot(data[2], data[1], label=label)
    axis[3].plot(data[0], data[2], label=label)


fig = plt.figure()

ax1 = fig.add_subplot(221, projection='3d')
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

axis = [ax1, ax2, ax3, ax4]

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

t1 = trajectory.Trajectory(x=-8, y=5, z=5, h0=2)
t1data = t1.calculate_trajectory()

t2 = trajectory.Trajectory(x=10, y=5, z=10)
t2data = t2.calculate_trajectory()

plot_to_plots(axis, t1data, '1')
plot_to_plots(axis, t2data, '2')

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
