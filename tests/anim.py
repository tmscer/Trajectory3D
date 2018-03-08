from matplotlib import pylab as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon
from matplotlib.widgets import Cursor
import numpy as np
import time

plt.style.use("monokai")

fig = plt.figure()
ax = fig.add_subplot(111)

import math

def lcm(a, b):
    return a * b / math.gcd(a, b)

T = 12
T2 = 15
omega = 2 * np.pi / T
omega2 = 2 * np.pi / T2
step = np.pi / 200
n = lcm(T, T2)
x = np.arange(0, n * T + step, step)
y = -np.sin(omega * x)
y2 = -np.sin(omega2 * x)

i = 1

def integral_poly(x, y):
    verts = [(0, 0)] + list(zip(x, y)) + [(x[-1], 0)]
    poly = Polygon(verts, facecolor='1', edgecolor='0.0', alpha=0.2)
    return poly


def animate(_):
    global i, ax, x, y
    l = len(x)
    ax.clear()
    cursor = Cursor(ax, useblit=True, color='red', linewidth=1)
    xr = x[:i % l]
    yr = y[:i % l]
    yr2 = y2[:i % l]
    ax.plot(xr, yr)
    ax.plot(xr, yr2)
    ax.plot(xr, yr + yr2 + yr2)
    #if i % l > 0:
    #    ax.add_patch(integral_poly(xr, yr))
    plt.ylim(-1.2, 1.2)
    plt.xlim(-0.2, n * T + 0.2)
    i += 1
    plt.draw()




cursor = Cursor(ax, useblit=True, color='red', linewidth=1)
#ani = FuncAnimation(fig, animate, interval=10)
ax.plot(x, y)
ax.plot(x, y2)
ax.add_patch(integral_poly(x, y))
ax.add_patch(integral_poly(x, y2))
plt.ylim(-1.2, 1.2)
plt.xlim(-0.2, n + 0.2)
#ax.plot(x, y + y2)
print(n)
plt.show()
