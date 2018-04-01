from matplotlib import pylab as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon
from matplotlib.widgets import Cursor
import matplotlib.gridspec as gridspec
import numpy as np
import math
import time

#plt.style.use("monokai")

fig = plt.figure(figsize=(10, 5))

#sound_graph = fig.add_subplot(211)
#circled_graph = fig.add_subplot(234)
#fourier_graph = fig.add_subplot(235)


drawing = False

circle_graph = plt.subplot2grid((4, 10), (0, 0), rowspan=4, colspan=5)
sound_graph = plt.subplot2grid((4, 10), (0, 5), rowspan=2, colspan=5)
fourier_graph = plt.subplot2grid((4, 10), (2, 5), rowspan=2, colspan=5)

step = 0.001
c = 0

x = np.arange(0, 2 * np.pi + step, step)
circle = np.e ** (x * 2 * np.pi * 1j)
circle_graph.plot(circle.real, circle.imag, 'w.', linewidth=0.25)

circle_graph.plot([-1.25, 1.25], [0, 0], 'w', linewidth=1)  # x axis
circle_graph.plot([0, 0], [-1.25, 1.25], 'w', linewidth=1)  # y axis

snd_freq1 = 2  # per second
snd_period1 = 1 / snd_freq1
omega1 = 2 * np.pi * snd_freq1

xf = np.arange(0, 5 * 1 / snd_freq1 + step, step)
func = np.sin(omega1 * xf) + np.sin(2 * np.pi * 3 * xf) + np.sin(2 * np.pi * 5 * xf) + np.sin(2 * np.pi * 7 * xf)

sndx = np.arange(-3 * snd_period1, 10 * snd_period1 + step, step)
sndy = np.sin(omega1 * sndx) + np.sin(2 * np.pi * 3 * sndx) + np.sin(2 * np.pi * 5 * sndx) + np.sin(2 * np.pi * 7 * sndx)

sound_graph.plot(sndx, sndy, linewidth=1)

draw_freq = 0
draw_omega = 2 * np.pi * draw_freq

shape = func * (np.sin(draw_omega * xf) + 1j * np.cos(draw_omega * xf))  ##
line = circle_graph.plot(shape.real, shape.imag, linewidth=1)[0]

circle_graph.axis('equal')
circle_limit = 3
circle_graph.set_ylim(-circle_limit, circle_limit)
circle_graph.set_xlim(-circle_limit, circle_limit)

sound_graph.axis('equal')
sound_graph.set_xlim(-0.5, 10)


def average_location(x, y):
    x_avg = sum(x) / len(x)
    y_avg = sum(y) / len(y)
    return x_avg, y_avg


avg_loc = average_location(shape.real, shape.imag)
avg_point = circle_graph.plot([avg_loc[0]], [avg_loc[1]], 'ro')[0]

four_x = []
four_y1 = []
four_y2 = []

fourier_line1 = fourier_graph.plot(four_x, four_y1, linewidth=1)[0]
fourier_line2 = fourier_graph.plot(four_x, four_y2, linewidth=1)[0]

fourier_graph.set_ylim(-2, 2)
fourier_graph.set_xlim(-0.5, 10)

def animate(i):
    global four_x, four_y1, fourier_line1, fourier_line2, fourier_graph
    freq = draw_freq + i / 250
    if (freq + 1 / 500) % 1 == 0:
        print(freq)
        #time.sleep(3)
    ome = 2 * np.pi * freq
    shape = func * (np.sin(ome * xf) + 1j * np.cos(ome * xf))  ##
    #shape = func * (np.cos(ome * xf) + 1j * np.sin(ome * xf))  ##

    line.set_data(shape.real, shape.imag)
    avg_loc = average_location(shape.real, shape.imag)
    avg_point.set_data([avg_loc[0]], [avg_loc[1]])

    four_x.append(round(freq, 3))
    four_y1.append(avg_loc[0])
    four_y2.append(avg_loc[1])
    fourier_line1.set_data(four_x, four_y1)
    fourier_line2.set_data(four_x, four_y2)
    #plt.draw()

    return line, avg_point, fourier_line1, fourier_line2


if not drawing:
    ani = FuncAnimation(fig, animate, interval=10, blit=True)
else:
    pass

plt.show()
