#!/bin/env python
import math

try:
    import matplotlib
    from mpl_toolkits.mplot3d import axes3d
except ImportError:
    raise ImportError("Visualizer requires module Matplotlib")

try:
    import numpy as np
except ImportError:
    raise ImportError("Visualizer requires module Numpy")

from parabola import Parabola
from spiral import Spiral
from plane import Plane


class Plotter:

    def __init__(self, vis):
        self.vis = vis
        self.axes = {'xyz': self.vis.figure.add_subplot(221, projection='3d'),
                     'xz': self.vis.figure.add_subplot(222),
                     'xy': self.vis.figure.add_subplot(223),
                     'zy': self.vis.figure.add_subplot(224), }
        self.plots = {}
        for key in self.axes.keys():
            self.plots[key] = {}

        self.plane = Plane(alpha=-np.pi/4, beta=0, c=-10)

        self.spiral = Spiral(20, 20, self.plane, y0=50)
        self.parabola = Parabola(self.plane, vel_x=10, vel_y=8, vel_z=25)

        self.plot_projectile(self.parabola)
        self.plot_spiral(self.spiral)
        self.plot_plane(self.plane)


        self.set_axes_labels()
        self.set_axes_props()

    def set_axes_props(self):
        self.axes['xyz'].axis('equal')
        self.axes['xyz'].set_zlim(0)

        self.axes['xz'].grid(color='grey', linestyle='--', linewidth='0.5')

        self.axes['xy'].grid(color='grey', linestyle='--', linewidth='0.5')
        self.axes['xy'].set_ylim(0)

        self.axes['zy'].grid(color='grey', linestyle='--', linewidth='0.5')
        self.axes['xy'].set_ylim(0)
        for axis in self.axes.values():
            axis.axis('equal')
            axis.format_coord = self.vis.ui_handler.display_coords
            #axis.autoscale_view(True, True, True)
            axis.autoscale(True)
            #axis.set_autoscale_on(True)

    def adjust_axes(self):
        for key in self.axes:
            self.axes[key].relim()
            self.axes[key].autoscale_view()

    def remove_trajectory(self, traj):
        traj_id = id(traj)
        for plot in self.plots.values():
            for obj in plot[traj_id].values():
                obj.remove()

    def set_axes_labels(self, x_label='x-axis', y_label='y-axis', z_label='z-axis'):
        self.axes['xyz'].set_title('3d view x,y,z', loc='left')
        self.axes['xyz'].set_xlabel(x_label, fontsize=10)
        self.axes['xyz'].set_zlabel(y_label, fontsize=10)
        self.axes['xyz'].set_ylabel(z_label, fontsize=10)

        self.axes['xz'].set_title('top view x,z', loc='left')
        self.axes['xz'].set_xlabel(x_label, fontsize=10)
        self.axes['xz'].set_ylabel(z_label, fontsize=10)

        self.axes['xy'].set_title('side view x,y', loc='left')
        self.axes['xy'].set_xlabel(x_label, fontsize=10)
        self.axes['xy'].set_ylabel(y_label, fontsize=10)

        self.axes['zy'].set_title('side view z,y', loc='left')
        self.axes['zy'].set_xlabel(z_label, fontsize=10)
        self.axes['zy'].set_ylabel(y_label, fontsize=10)

    def plot_projectile(self, traj):
        X, Y, Z, _ = traj.calculate_trajectory()
        b_pos = traj.b_pos()
        c_pos = traj.c_pos()

        traj_id = id(traj)
        self.plots['xyz'][traj_id] = {}

        self.plots['xyz'][traj_id]['main'] = self.axes['xyz'].plot(X, Z, Y)[0]
        self.plots['xyz'][traj_id]['A'] = self.axes['xyz'].plot([X[0]], [Z[0]], [Y[0]], 'ko')[0]  # A
        self.plots['xyz'][traj_id]['B'] = self.axes['xyz'].plot([b_pos[0]], [b_pos[2]], [b_pos[1]], 'ko')[0]  # B
        self.plots['xyz'][traj_id]['C'] = self.axes['xyz'].plot([c_pos[0]], [c_pos[2]], [c_pos[1]], 'ko')[0]  # C
        self.plots['xyz'][traj_id]['D'] = self.axes['xyz'].plot([X[-1]], [Z[-1]], [Y[-1]], 'k*')[0]  # D
        self.plots['xyz'][traj_id]['A0'] = self.axes['xyz'].plot([X[0], X[0]], [Z[0], Z[0]], [0, Y[0]], 'k:')[0]  # dotted to A

        self.plots['xy'][traj_id] = {}

        self.plots['xy'][traj_id]['main'] = self.axes['xy'].plot(X, Y)[0]
        self.plots['xy'][traj_id]['A'] = self.axes['xy'].plot([X[0]], [Y[0]], 'ko')[0]  # A
        self.plots['xy'][traj_id]['B'] = self.axes['xy'].plot([b_pos[0]], [b_pos[1]], 'ko')[0]  # B
        self.plots['xy'][traj_id]['C'] = self.axes['xy'].plot([c_pos[0]], [c_pos[1]], 'ko')[0]  # C
        self.plots['xy'][traj_id]['D'] = self.axes['xy'].plot([X[-1]], [Y[-1]], 'k*')[0]  # D
        self.plots['xy'][traj_id]['A0'] = self.axes['xy'].plot([X[0], X[0]], [0, Y[0]], 'k:')[0]  # dotted to A

        self.plots['zy'][traj_id] = {}

        self.plots['zy'][traj_id]['main'] = self.axes['zy'].plot(Z, Y)[0]
        self.plots['zy'][traj_id]['A'] = self.axes['zy'].plot([Z[0]], [Y[0]], 'ko')[0]  # A
        self.plots['zy'][traj_id]['B'] = self.axes['zy'].plot([b_pos[2]], [b_pos[1]], 'ko')[0]  # B
        self.plots['zy'][traj_id]['C'] = self.axes['zy'].plot([c_pos[2]], [c_pos[1]], 'ko')[0]  # C
        self.plots['zy'][traj_id]['D'] = self.axes['zy'].plot([Z[-1]], [Y[-1]], 'k*')[0]  # D
        self.plots['zy'][traj_id]['A0'] = self.axes['zy'].plot([Z[0], Z[0]], [0, Y[0]], 'k:')[0]  # dotted to A

        self.plots['xz'][traj_id] = {}

        self.plots['xz'][traj_id]['main'] = self.axes['xz'].plot(X, Z)[0]
        self.plots['xz'][traj_id]['A'] = self.axes['xz'].plot([X[0]], [Z[0]], 'ko')[0]  # A
        self.plots['xz'][traj_id]['B'] = self.axes['xz'].plot([b_pos[0]], [b_pos[2]], 'ko')[0]  # B
        self.plots['xz'][traj_id]['C'] = self.axes['xz'].plot([c_pos[0]], [c_pos[2]], 'ko')[0]  # C
        self.plots['xz'][traj_id]['D'] = self.axes['xz'].plot([X[-1]], [Z[-1]], 'k*')[0]  # D

    def update_traj(self):
        xyz = self.parabola.calculate_trajectory()
        X = xyz[0]
        Y = xyz[1]
        Z = xyz[2]
        b_pos = self.parabola.b_pos()
        c_pos = self.parabola.c_pos()

        parabol_id = id(self.parabola)

        if parabol_id not in self.plots['xyz'].keys():
            return

        self.plots['xyz'][parabol_id]['main']._verts3d = (X, Z, Y)
        self.plots['xyz'][parabol_id]['A']._verts3d = ([X[0]], [Z[0]], [Y[0]])
        self.plots['xyz'][parabol_id]['B']._verts3d = ([b_pos[0]], [b_pos[2]], [b_pos[1]])
        self.plots['xyz'][parabol_id]['C']._verts3d = ([c_pos[0]], [c_pos[2]], [c_pos[1]])
        self.plots['xyz'][parabol_id]['D']._verts3d = ([X[-1]], [Z[-1]], [Y[-1]])
        self.plots['xyz'][parabol_id]['A0']._verts3d = ([X[0], X[0]], [Z[0], Z[0]], [0, Y[0]])

        self.plots['xy'][parabol_id]['main'].set_xdata(X)
        self.plots['xy'][parabol_id]['main'].set_ydata(Y)
        self.plots['xy'][parabol_id]['A'].set_xdata([X[0]])
        self.plots['xy'][parabol_id]['A'].set_ydata([Y[0]])
        self.plots['xy'][parabol_id]['B'].set_xdata([b_pos[0]])
        self.plots['xy'][parabol_id]['B'].set_ydata([b_pos[1]])
        self.plots['xy'][parabol_id]['C'].set_xdata([c_pos[0]])
        self.plots['xy'][parabol_id]['C'].set_ydata([c_pos[1]])
        self.plots['xy'][parabol_id]['D'].set_xdata([X[-1]])
        self.plots['xy'][parabol_id]['D'].set_ydata([Y[-1]])
        self.plots['xy'][parabol_id]['A0'].set_xdata([X[0], X[0]])
        self.plots['xy'][parabol_id]['A0'].set_ydata([0, Y[0]])

        self.plots['zy'][parabol_id]['main'].set_xdata(Z)
        self.plots['zy'][parabol_id]['main'].set_ydata(Y)
        self.plots['zy'][parabol_id]['A'].set_xdata([Z[0]])
        self.plots['zy'][parabol_id]['A'].set_ydata([Y[0]])
        self.plots['zy'][parabol_id]['B'].set_xdata([b_pos[2]])
        self.plots['zy'][parabol_id]['B'].set_ydata([b_pos[1]])
        self.plots['zy'][parabol_id]['C'].set_xdata([c_pos[2]])
        self.plots['zy'][parabol_id]['C'].set_ydata([c_pos[1]])
        self.plots['zy'][parabol_id]['D'].set_xdata([Z[-1]])
        self.plots['zy'][parabol_id]['D'].set_ydata([Y[-1]])
        self.plots['zy'][parabol_id]['A0'].set_xdata([Z[0], Z[0]])
        self.plots['zy'][parabol_id]['A0'].set_ydata([0, Y[0]])

        self.plots['xz'][parabol_id]['main'].set_xdata(X)
        self.plots['xz'][parabol_id]['main'].set_ydata(Z)
        self.plots['xz'][parabol_id]['A'].set_xdata([X[0]])
        self.plots['xz'][parabol_id]['A'].set_ydata([Z[0]])
        self.plots['xz'][parabol_id]['B'].set_xdata([b_pos[0]])
        self.plots['xz'][parabol_id]['B'].set_ydata([b_pos[2]])
        self.plots['xz'][parabol_id]['C'].set_xdata([c_pos[0]])
        self.plots['xz'][parabol_id]['C'].set_ydata([c_pos[2]])
        self.plots['xz'][parabol_id]['D'].set_xdata([X[-1]])
        self.plots['xz'][parabol_id]['D'].set_ydata([Z[-1]])

    def plot_plane(self, plane):
        coords = plane.get_coords(self.parabola._last_calc[0][0], self.parabola._last_calc[0][-1], self.parabola._last_calc[2][0], self.parabola._last_calc[2][-1])
        x = coords[0]
        y = coords[1]
        z = coords[2]
        plane_id = id(plane)

        self.plot_plane_3d(plane_id, x, y, z)

        self.plots['xy'][plane_id] = {}
        self.plots['xy'][plane_id]['main'] = self.axes['xy'].plot(x, y, color=(0.5, 0.5, 0.5))[0]

        self.plots['zy'][plane_id] = {}
        self.plots['zy'][plane_id]['main'] = self.axes['zy'].plot(z, y, color=(0.5, 0.5, 0.5))[0]

        self.plots['xz'][plane_id] = {}
        self.plots['xz'][plane_id]['main'] = self.axes['xz'].plot(x, z, color=(0.5, 0.5, 0.5))[0]

    def plot_plane_3d(self, plane_id, x, y, z):
        self.plots['xyz'][plane_id] = {}
        self.plots['xyz'][plane_id]['main'] = self.axes['xyz'].plot_trisurf(x, z, y, color=(0.5, 0.5, 0.5))

    def update_plane(self, plane):
        plane_id = id(plane)

        x, y, z = plane.get_coords(self.parabola._last_calc[0][0],
                                   self.parabola._last_calc[0][-1],
                                   self.parabola._last_calc[2][0],
                                   self.parabola._last_calc[2][-1])
        for obj in self.plots['xyz'][plane_id].values():
            obj.remove()

        self.vis.plotter.plot_plane_3d(plane_id, x, y, z)

        self.plots['xy'][plane_id]['main'].set_xdata(x)
        self.plots['xy'][plane_id]['main'].set_ydata(y)

        self.plots['zy'][plane_id]['main'].set_xdata(z)
        self.plots['zy'][plane_id]['main'].set_ydata(y)

        self.plots['xz'][plane_id]['main'].set_xdata(x)
        self.plots['xz'][plane_id]['main'].set_ydata(z)

    def clear_axes(self):
        for axis in self.axes:
            axis.clear()

    def plot_spiral(self, spiral):
        X, Y, Z, _ = spiral.calculate_trajectory()
        spiral_id = id(spiral)

        self.plots['xyz'][spiral_id] = {}
        self.plots['xyz'][spiral_id]['main'] = self.axes['xyz'].plot(X, Z, Y)[0]

        self.plots['xy'][spiral_id] = {}
        self.plots['xy'][spiral_id]['main'] = self.axes['xy'].plot(X, Y)[0]

        self.plots['zy'][spiral_id] = {}
        self.plots['zy'][spiral_id]['main'] = self.axes['zy'].plot(Z, Y)[0]

        self.plots['xz'][spiral_id] = {}
        self.plots['xz'][spiral_id]['main'] = self.axes['xz'].plot(X, Z)[0]

    def update_spiral(self):
        X, Y, Z, _ = self.spiral.calculate_trajectory()

        spiral_id = id(self.spiral)

        if spiral_id not in self.plots['xyz'].keys():
            return

        self.plots['xyz'][spiral_id]['main']._verts3d = (X, Z, Y)

        self.plots['xy'][spiral_id]['main'].set_xdata(X)
        self.plots['xy'][spiral_id]['main'].set_ydata(Y)

        self.plots['zy'][spiral_id]['main'].set_xdata(Z)
        self.plots['zy'][spiral_id]['main'].set_ydata(Y)

        self.plots['xz'][spiral_id]['main'].set_xdata(X)
        self.plots['xz'][spiral_id]['main'].set_ydata(Z)
