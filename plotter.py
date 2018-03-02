#!/bin/env python
import math

try:
    import matplotlib
    from mpl_toolkits.mplot3d import axes3d
except ImportError:
    raise ImportError("Visualizer requires module Matplotlib")

try:
    import numpy
except ImportError:
    raise ImportError("Visualizer requires module Numpy")

from projectile import *
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

        self.plane = Plane(1/20, 1/20, -3)

        self.proj = Projectile(self.plane, vel_x=10, vel_y=8, vel_z=25)
        self.plot_projectile(self.proj)
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
            axis.relim()
            #axis.autoscale_view(True, True, True)
            #axis.autoscale(True)
            axis.set_autoscale_on(True)

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
        xyz = traj.calculate_trajectory()
        X = xyz[0]
        Y = xyz[1]
        Z = xyz[2]
        b_pos = traj.b_pos()
        c_pos = traj.c_pos()

        traj_id = id(traj)
        self.plots['xyz'][traj_id] = {}

        self.plots['xyz'][traj_id]['main'] = self.axes['xyz'].plot(X, Z, Y)[0]
        self.plots['xyz'][traj_id]['A'] = self.axes['xyz'].plot([X[0]], [Z[0]], [Y[0]], 'wo')[0]  # A
        self.plots['xyz'][traj_id]['B'] = self.axes['xyz'].plot([b_pos[0]], [b_pos[2]], [b_pos[1]], 'wo')[0]  # B
        self.plots['xyz'][traj_id]['C'] = self.axes['xyz'].plot([c_pos[0]], [c_pos[2]], [c_pos[1]], 'wo')[0]  # C
        self.plots['xyz'][traj_id]['D'] = self.axes['xyz'].plot([X[-1]], [Z[-1]], [Y[-1]], 'k*')[0]  # D
        self.plots['xyz'][traj_id]['A0'] = self.axes['xyz'].plot([X[0], X[0]], [Z[0], Z[0]], [0, Y[0]], 'k:')[
            0]  # dotted to A

        self.plots['xy'][traj_id] = {}

        self.plots['xy'][traj_id]['main'] = self.axes['xy'].plot(X, Y)[0]
        self.plots['xy'][traj_id]['A'] = self.axes['xy'].plot([X[0]], [Y[0]], 'wo')[0]  # A
        self.plots['xy'][traj_id]['B'] = self.axes['xy'].plot([b_pos[0]], [b_pos[1]], 'wo')[0]  # B
        self.plots['xy'][traj_id]['C'] = self.axes['xy'].plot([c_pos[0]], [c_pos[1]], 'wo')[0]  # C
        self.plots['xy'][traj_id]['D'] = self.axes['xy'].plot([X[-1]], [Y[-1]], 'k*')[0]  # D
        self.plots['xy'][traj_id]['A0'] = self.axes['xy'].plot([X[0], X[0]], [0, Y[0]], 'k:')[0]  # dotted to A

        self.plots['zy'][traj_id] = {}

        self.plots['zy'][traj_id]['main'] = self.axes['zy'].plot(Z, Y)[0]
        self.plots['zy'][traj_id]['A'] = self.axes['zy'].plot([Z[0]], [Y[0]], 'wo')[0]  # A
        self.plots['zy'][traj_id]['B'] = self.axes['zy'].plot([b_pos[2]], [b_pos[1]], 'wo')[0]  # B
        self.plots['zy'][traj_id]['C'] = self.axes['zy'].plot([c_pos[2]], [c_pos[1]], 'wo')[0]  # C
        self.plots['zy'][traj_id]['D'] = self.axes['zy'].plot([Z[-1]], [Y[-1]], 'k*')[0]  # D
        self.plots['zy'][traj_id]['A0'] = self.axes['zy'].plot([Z[0], Z[0]], [0, Y[0]], 'k:')[0]  # dotted to A

        self.plots['xz'][traj_id] = {}

        self.plots['xz'][traj_id]['main'] = self.axes['xz'].plot(X, Z)[0]
        self.plots['xz'][traj_id]['A'] = self.axes['xz'].plot([X[0]], [Z[0]], 'wo')[0]  # A
        self.plots['xz'][traj_id]['B'] = self.axes['xz'].plot([b_pos[0]], [b_pos[2]], 'wo')[0]  # B
        self.plots['xz'][traj_id]['C'] = self.axes['xz'].plot([c_pos[0]], [c_pos[2]], 'wo')[0]  # C
        self.plots['xz'][traj_id]['D'] = self.axes['xz'].plot([X[-1]], [Z[-1]], 'k*')[0]  # D

    def plot_plane(self, plane):
        coords = plane.get_coords(-30, 30, -30, 30)
        x = coords[0]
        y = coords[1]
        z = coords[2]
        self.axes['xyz'].plot_trisurf(x, z, y)

    def clear_axes(self):
        for axis in self.axes:
            axis.clear()
