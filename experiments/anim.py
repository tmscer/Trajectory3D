from matplotlib import pylab as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon
from matplotlib.widgets import Cursor
import random
import numpy as np
import time

#plt.style.use("monokai")

fig = plt.figure()
ax = fig.add_subplot(111)

import math

def lcm(a, b):
    return a * b / math.gcd(a, b)


def integral_poly(x, y):
    verts = [(0, 0)] + list(zip(x, y)) + [(x[-1], 0)]
    poly = Polygon(verts, facecolor='1', edgecolor='0.0', alpha=0.2)
    return poly


x = [0]
y = [0]
line = ax.plot(x, y)[0]

def animate(_):
    global line, x, y, ax
    ax.clear()
    x.append(x[-1] + 0.1)
    y.append(random.randint(1, 4))
    ax.plot(x, y)

cursor = Cursor(ax, useblit=True, color='red', linewidth=1)
ani = FuncAnimation(fig, animate, interval=10)
plt.show()
