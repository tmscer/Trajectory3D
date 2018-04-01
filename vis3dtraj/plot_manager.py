#!/bin/env python

try:
    import matplotlib
    from mpl_toolkits.mplot3d import axes3d
except ImportError:
    raise ImportError("Visualizer requires module Matplotlib")

try:
    import numpy as np
except ImportError:
    raise ImportError("Visualizer requires module Numpy")

from vis3dtraj.actors.parabola import Parabola
from vis3dtraj.actors.spiral import Spiral
from vis3dtraj.actors.plane import Plane
import vis3dtraj.app_style as style


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

        self.spiral = Spiral(radius=20, omega=7, plane=self.plane, y0=200, z0=40)
        self.parabola = Parabola(self.plane, vel_x=-13.5, vel_y=28, vel_z=25, x0=50, y0=70)

        self.plot_parabola(self.parabola)
        self.plot_spiral(self.spiral)
        self.plot_plane(self.plane)

        self.set_axes_labels()
        self.set_axes_props()

    def set_axes_props(self):
        self.axes['xyz'].axis('equal')
        self.axes['xyz'].set_zlim(0)

        self.axes['xz'].grid(style.plot.grid_kwargs)

        self.axes['xy'].grid(style.plot.grid_kwargs)
        self.axes['xy'].set_ylim(0)

        self.axes['zy'].grid(style.plot.grid_kwargs)
        self.axes['xy'].set_ylim(0)
        for axis in self.axes.values():
            axis.axis('equal')
            axis.format_coord = self.vis.ui_handler.display_coords
            axis.autoscale(True)

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

    def create_obj_dicts(self, name):
        self.plots['xyz'][name] = {}
        self.plots['xy'][name] = {}
        self.plots['zy'][name] = {}
        self.plots['xz'][name] = {}

    def plot_component(self, obj_id, x, y, z, name, *args, **kwargs):
        self.plots['xyz'][obj_id][name] = self.axes['xyz'].plot(x, z, y, *args, **kwargs)[0]
        self.plots['xy'][obj_id][name] = self.axes['xy'].plot(x, y, *args, **kwargs)[0]
        self.plots['zy'][obj_id][name] = self.axes['zy'].plot(z, y, *args, **kwargs)[0]
        self.plots['xz'][obj_id][name] = self.axes['xz'].plot(x, z, *args, **kwargs)[0]

    def plot_parabola(self, parabola):
        x, y, z, _ = parabola.calculate_trajectory()
        parabola_id = id(parabola)

        self.create_obj_dicts(parabola_id)

        self.plot_component(parabola_id, x, y, z, 'main')
        self.plot_component(parabola_id, [parabola.x0] * 2, [0, parabola.y0], [parabola.z0] * 2, 'A0', 'k:')
        point_args = 'ko'
        self.plot_component(parabola_id, x, y, z, 'A', point_args)
        self.plot_component(parabola_id, x, y, z, 'B', point_args)
        self.plot_component(parabola_id, x, y, z, 'C', point_args)
        self.plot_component(parabola_id, x, y, z, 'D', point_args)

    def update_traj(self):
        xyz = self.parabola.calculate_trajectory()
        X = xyz[0]
        Y = xyz[1]
        Z = xyz[2]
        b_pos = self.parabola.b_pos()
        c_pos = self.parabola.c_pos()

        parabola_id = id(self.parabola)

        if parabola_id not in self.plots['xyz'].keys():
            return

        self.plots['xyz'][parabola_id]['main']._verts3d = (X, Z, Y)
        self.plots['xyz'][parabola_id]['A']._verts3d = ([X[0]], [Z[0]], [Y[0]])
        self.plots['xyz'][parabola_id]['B']._verts3d = ([b_pos[0]], [b_pos[2]], [b_pos[1]])
        self.plots['xyz'][parabola_id]['C']._verts3d = ([c_pos[0]], [c_pos[2]], [c_pos[1]])
        self.plots['xyz'][parabola_id]['D']._verts3d = ([X[-1]], [Z[-1]], [Y[-1]])
        self.plots['xyz'][parabola_id]['A0']._verts3d = ([X[0], X[0]], [Z[0], Z[0]], [0, Y[0]])

        self.plots['xy'][parabola_id]['main'].set_xdata(X)
        self.plots['xy'][parabola_id]['main'].set_ydata(Y)
        self.plots['xy'][parabola_id]['A'].set_xdata([X[0]])
        self.plots['xy'][parabola_id]['A'].set_ydata([Y[0]])
        self.plots['xy'][parabola_id]['B'].set_xdata([b_pos[0]])
        self.plots['xy'][parabola_id]['B'].set_ydata([b_pos[1]])
        self.plots['xy'][parabola_id]['C'].set_xdata([c_pos[0]])
        self.plots['xy'][parabola_id]['C'].set_ydata([c_pos[1]])
        self.plots['xy'][parabola_id]['D'].set_xdata([X[-1]])
        self.plots['xy'][parabola_id]['D'].set_ydata([Y[-1]])
        self.plots['xy'][parabola_id]['A0'].set_xdata([X[0], X[0]])
        self.plots['xy'][parabola_id]['A0'].set_ydata([0, Y[0]])

        self.plots['zy'][parabola_id]['main'].set_xdata(Z)
        self.plots['zy'][parabola_id]['main'].set_ydata(Y)
        self.plots['zy'][parabola_id]['A'].set_xdata([Z[0]])
        self.plots['zy'][parabola_id]['A'].set_ydata([Y[0]])
        self.plots['zy'][parabola_id]['B'].set_xdata([b_pos[2]])
        self.plots['zy'][parabola_id]['B'].set_ydata([b_pos[1]])
        self.plots['zy'][parabola_id]['C'].set_xdata([c_pos[2]])
        self.plots['zy'][parabola_id]['C'].set_ydata([c_pos[1]])
        self.plots['zy'][parabola_id]['D'].set_xdata([Z[-1]])
        self.plots['zy'][parabola_id]['D'].set_ydata([Y[-1]])
        self.plots['zy'][parabola_id]['A0'].set_xdata([Z[0], Z[0]])
        self.plots['zy'][parabola_id]['A0'].set_ydata([0, Y[0]])

        self.plots['xz'][parabola_id]['main'].set_xdata(X)
        self.plots['xz'][parabola_id]['main'].set_ydata(Z)
        self.plots['xz'][parabola_id]['A'].set_xdata([X[0]])
        self.plots['xz'][parabola_id]['A'].set_ydata([Z[0]])
        self.plots['xz'][parabola_id]['B'].set_xdata([b_pos[0]])
        self.plots['xz'][parabola_id]['B'].set_ydata([b_pos[2]])
        self.plots['xz'][parabola_id]['C'].set_xdata([c_pos[0]])
        self.plots['xz'][parabola_id]['C'].set_ydata([c_pos[2]])
        self.plots['xz'][parabola_id]['D'].set_xdata([X[-1]])
        self.plots['xz'][parabola_id]['D'].set_ydata([Z[-1]])

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

        self.plot_plane_3d(plane_id, x, y, z)

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
        x, y, z, _ = spiral.calculate_trajectory()
        sid = id(spiral)

        self.create_obj_dicts(sid)

        self.plot_component(sid, x, y, z, 'main')

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
