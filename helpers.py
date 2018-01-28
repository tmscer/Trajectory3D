import numpy as np


def set_axis_fontsize_and_label(ax, fontsize, xlabel='x-axis', ylabel='y-axis', zlabel='z-axis'):
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_zlabel(zlabel, fontsize=fontsize)


def plot3d(ax, data1, data2, data3, param_dict):
    out = ax.plot(data1, data2, data3, **param_dict)
    return out


def trajectory2d(v0, alpha, height, g, end):
    X = np.linspace(0, end, end * 2)
    Y = [None] * len(X)
    Z = [0] * len(X)
    v0cos = v0 * np.cos(alpha)
    v0sin = v0 * np.sin(alpha)
    e = len(X)
    for i, x in enumerate(X):
        t = x / v0cos
        y = height + t * (v0sin - 0.5 * g * t)
        if y < 0:
            e = i
            break
        else:
            Y[i] = y
    return [X[0:e], Y[0:e], Z[0:e]]

