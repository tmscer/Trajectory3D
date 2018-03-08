import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

plt.style.use("monokai")

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)


def get_graduals(y1, y2, iters):
    if len(y1) != len(y2):
        raise ValueError()
    grads = []
    for i in range(iters):
        grads.append(y1 + i * (y2 - y1) / iters)
    return grads


x = np.arange(0, 10 + 0.1, 0.1)
y1 = np.sin(x)
y2 = 2 * np.sin(x)

gs = get_graduals(y2, y1, 100)


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    global x, gs
    line.set_data(x, gs[i % len(gs)])
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()