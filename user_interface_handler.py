from math import pi
import math

try:
    from matplotlib import pyplot
except ImportError:
    raise ImportError("Visualizer requires module Matplotlib")

try:
    from tkinter import *
except ImportError:
    raise ImportError("Visualizer require module tkinter")

import itertools


class UserInterfaceHandler:

    def __init__(self, vis):
        self.vis = vis
        # build the ui
        #self.option_window = Toplevel()
        #self.option_window.geometry("300x700+50+50")
        #self.option_window.wm_title("Visualizer Toolbar")

        self.option_window = Frame(self.vis.tk_root, width=250)
        self.option_window.pack(side=RIGHT, fill=BOTH)

        row_counter = (x for x in itertools.count(start=0, step=1))

        self.canvas = Canvas(self.option_window, borderwidth=0.5, width=250)
        self.frame = Frame(self.canvas, width=250)
        self.vsb = Scrollbar(self.option_window, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side=RIGHT, fill=BOTH)
        self.canvas.pack(side=RIGHT, fill=Y, expand=True)
        self.canvas.create_window((1, 2), window=self.frame, anchor="ne", tags="self.frame")
        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(int(-(event.delta / 120)), "units"))

        self.frame.bind("<Configure>", lambda *args: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.coord = StringVar(value="[x , y]")
        self.coord_label = Label(self.frame, font=("Helvetica", 15), textvariable=self.coord)
        self.coord_label.grid(row=next(row_counter), column=0, columnspan=2)
        self.top_spacer = Label(self.frame, text="\t\t\t", width=5)
        self.top_spacer.grid(row=next(row_counter), column=0)

        # PROJECTILE
        self.proj1_label = Label(self.frame, font=("Helvetica", 12), text="Trajectory one", width=20)
        self.proj1_label.grid(row=next(row_counter), column=0, columnspan=2)

        self.proj1_v0 = DoubleVar()
        self.proj1_vx = DoubleVar()
        self.proj1_vy = DoubleVar()
        self.proj1_vz = DoubleVar()
        self.proj1_x0 = DoubleVar()
        self.proj1_y0 = DoubleVar()
        self.proj1_z0 = DoubleVar()
        self.proj1_alpha = DoubleVar()
        self.proj1_theta = DoubleVar()

        self.proj1_v0_input = Entry(self.frame, textvariable=self.proj1_v0)
        self.proj1_v0_input.bind('<Return>',
                                 lambda event: self.projectile_change(event, self.vis.plotter.proj, self.proj1_v0.get(),
                                                                      'v0'))

        self.proj1_vx_input = Entry(self.frame, textvariable=self.proj1_vx)
        self.proj1_vx_input.bind('<Return>',
                                 lambda event: self.projectile_change(event, self.vis.plotter.proj, self.proj1_vx.get(),
                                                                      'vx'))

        self.proj1_vy_input = Entry(self.frame, textvariable=self.proj1_vy)
        self.proj1_vy_input.bind('<Return>',
                                 lambda event: self.projectile_change(event, self.vis.plotter.proj, self.proj1_vy.get(),
                                                                      'vy'))

        self.proj1_vz_input = Entry(self.frame, textvariable=self.proj1_vz)
        self.proj1_vz_input.bind('<Return>',
                                 lambda event: self.projectile_change(event, self.vis.plotter.proj, self.proj1_vz.get(),
                                                                      'vz'))

        self.proj1_x0_input = Entry(self.frame, textvariable=self.proj1_x0)
        self.proj1_x0_input.bind('<Return>',
                                 lambda event: self.projectile_change(event, self.vis.plotter.proj, self.proj1_x0.get(),
                                                                      'x0'))

        self.proj1_y0_input = Entry(self.frame, textvariable=self.proj1_y0)
        self.proj1_y0_input.bind('<Return>',
                                 lambda event: self.projectile_change(event, self.vis.plotter.proj, self.proj1_y0.get(),
                                                                      'y0'))

        self.proj1_z0_input = Entry(self.frame, textvariable=self.proj1_z0)
        self.proj1_z0_input.bind('<Return>',
                                 lambda event: self.projectile_change(event, self.vis.plotter.proj, self.proj1_z0.get(),
                                                                      'z0'))

        self.proj1_alpha_input = Scale(self.frame, tickinterval=0.01, from_=0, to=90, orient=HORIZONTAL,
                                       variable=self.proj1_alpha, length=120)
        self.proj1_alpha_input.bind('<B1-Motion>', lambda event: self.projectile_change(event, self.vis.plotter.proj,
                                                                                        self.proj1_alpha.get(),
                                                                                        'alpha'))

        self.proj1_theta_input = Scale(self.frame, tickinterval=0.01, from_=0, to=360, orient=HORIZONTAL,
                                       variable=self.proj1_theta, length=120)
        self.proj1_theta_input.bind('<B1-Motion>', lambda event: self.projectile_change(event, self.vis.plotter.proj,
                                                                                        self.proj1_theta.get(),
                                                                                        'theta'))

        v0_row = next(row_counter)
        vx_row = next(row_counter)
        vy_row = next(row_counter)
        vz_row = next(row_counter)
        self.proj1_v0_input.grid(row=v0_row, column=1)
        self.proj1_vx_input.grid(row=vx_row, column=1)
        self.proj1_vy_input.grid(row=vy_row, column=1)
        self.proj1_vz_input.grid(row=vz_row, column=1)

        x0_row = next(row_counter)
        y0_row = next(row_counter)
        z0_row = next(row_counter)
        self.proj1_x0_input.grid(row=x0_row, column=1)
        self.proj1_y0_input.grid(row=y0_row, column=1)
        self.proj1_z0_input.grid(row=z0_row, column=1)

        alpha_row = next(row_counter)
        theta_row = next(row_counter)
        self.proj1_alpha_input.grid(row=alpha_row, column=1)
        self.proj1_theta_input.grid(row=theta_row, column=1)

        self.proj1_v0_label = Label(self.frame, text="v0:")
        self.proj1_vx_label = Label(self.frame, text="vx:")
        self.proj1_vy_label = Label(self.frame, text="vy:")
        self.proj1_vz_label = Label(self.frame, text="vz:")
        self.proj1_x0_label = Label(self.frame, text="x0:")
        self.proj1_y0_label = Label(self.frame, text="y0:")
        self.proj1_z0_label = Label(self.frame, text="z0:")
        self.proj1_alpha_label = Label(self.frame, text="alpha:")
        self.proj1_theta_label = Label(self.frame, text="theta:")

        self.proj1_v0_label.grid(row=v0_row, column=0)
        self.proj1_vx_label.grid(row=vx_row, column=0)
        self.proj1_vy_label.grid(row=vy_row, column=0)
        self.proj1_vz_label.grid(row=vz_row, column=0)

        self.proj1_x0_label.grid(row=x0_row, column=0)
        self.proj1_y0_label.grid(row=y0_row, column=0)
        self.proj1_z0_label.grid(row=z0_row, column=0)

        self.proj1_alpha_label.grid(row=alpha_row, column=0)
        self.proj1_theta_label.grid(row=theta_row, column=0)

        self.proj1_point_a = StringVar()
        self.proj1_point_a_label = Label(self.frame, textvariable=self.proj1_point_a)
        self.proj1_point_b = StringVar()
        self.proj1_point_b_label = Label(self.frame, textvariable=self.proj1_point_b)
        self.proj1_point_c = StringVar()
        self.proj1_point_c_label = Label(self.frame, textvariable=self.proj1_point_c)
        self.proj1_point_d = StringVar()
        self.proj1_point_d_label = Label(self.frame, textvariable=self.proj1_point_d)

        self.proj1_point_a_label.grid(row=next(row_counter), column=0, columnspan=2)
        self.proj1_point_b_label.grid(row=next(row_counter), column=0, columnspan=2)
        self.proj1_point_c_label.grid(row=next(row_counter), column=0, columnspan=2)
        self.proj1_point_d_label.grid(row=next(row_counter), column=0, columnspan=2)

        # SPIRAL
        self.spiral_label = Label(self.frame, text="Spiral", font=("Helvetica", 12), width=20)
        self.spiral_prescript = Label(self.frame,
                                      text="x(t) = r * cos (omega * t) + x0\ny(t) = y0 - 0.5 * g * t ** 2\nz(t) = r * sin(omega * t) + z0")
        self.spiral_label.grid(row=next(row_counter), column=0, columnspan=2)
        self.spiral_prescript.grid(row=next(row_counter), column=0, columnspan=2)

        self.spiral_locked_var = StringVar(self.frame)
        self.spiral_locked_var.set('radius')  # default value

        def lm(*args):
            self.vis.plotter.spiral.locked_var = self.spiral_locked_var.get()

        self.spiral_locked_var.trace('w', lm)

        self.spiral_locked_var_label = Label(self.frame, text='Locked Variable')
        self.spiral_locked_var_input = OptionMenu(self.frame, self.spiral_locked_var,
                                                    'radius', 'velocity', 'omega', 'acceleration')
        locked_var_row = next(row_counter)
        self.spiral_locked_var_label.grid(row=locked_var_row, column=0)
        self.spiral_locked_var_input.grid(row=locked_var_row, column=1)

        self.spiral_value_names = ['radius', 'velocity', 'omega', 'acceleration', 'period', 'frequency', 'x0', 'y0',
                                   'z0', 'phi0']

        self.spiral_vars = {label: DoubleVar() for label in self.spiral_value_names}

        self.spiral_labels = {label: Label(self.frame, text=label) for label in self.spiral_value_names}
        self.spiral_inputs = {label: Entry(self.frame, textvariable=self.spiral_vars[label]) for label in
                              self.spiral_value_names}

        self.spiral_inputs['radius'].bind('<Return>', lambda event: self.spiral_change(event, self.vis.plotter.spiral,
                                                                                       self.spiral_vars['radius'].get(),
                                                                                       'radius'))
        self.spiral_inputs['velocity'].bind('<Return>', lambda event: self.spiral_change(event, self.vis.plotter.spiral,
                                                                                         self.spiral_vars[
                                                                                             'velocity'].get(),
                                                                                         'velocity'))
        self.spiral_inputs['omega'].bind('<Return>', lambda event: self.spiral_change(event, self.vis.plotter.spiral,
                                                                                      self.spiral_vars['omega'].get(),
                                                                                      'omega'))
        self.spiral_inputs['acceleration'].bind('<Return>',
                                                lambda event: self.spiral_change(event, self.vis.plotter.spiral,
                                                                                 self.spiral_vars['acceleration'].get(),
                                                                                 'acceleration'))
        self.spiral_inputs['period'].bind('<Return>', lambda event: self.spiral_change(event, self.vis.plotter.spiral,
                                                                                       self.spiral_vars['period'].get(),
                                                                                       'period'))
        self.spiral_inputs['frequency'].bind('<Return>',
                                             lambda event: self.spiral_change(event, self.vis.plotter.spiral,
                                                                              self.spiral_vars['frequency'].get(),
                                                                              'frequency'))
        self.spiral_inputs['x0'].bind('<Return>', lambda event: self.spiral_change(event, self.vis.plotter.spiral,
                                                                                   self.spiral_vars['x0'].get(),
                                                                                   'x0'))
        self.spiral_inputs['y0'].bind('<Return>', lambda event: self.spiral_change(event, self.vis.plotter.spiral,
                                                                                   self.spiral_vars['y0'].get(),
                                                                                   'y0'))
        self.spiral_inputs['z0'].bind('<Return>', lambda event: self.spiral_change(event, self.vis.plotter.spiral,
                                                                                   self.spiral_vars['z0'].get(),
                                                                                   'z0'))
        self.spiral_inputs['phi0'].bind('<Return>', lambda event: self.spiral_change(event, self.vis.plotter.spiral,
                                                                                     self.spiral_vars['phi0'].get(),
                                                                                     'phi0'))

        for name in self.spiral_value_names:
            row_index = next(row_counter)
            self.spiral_labels[name].grid(row=row_index, column=0)
            self.spiral_inputs[name].grid(row=row_index, column=1)

        # PLANE
        self.plane_label = Label(self.frame, text="Plane", font=("Helvetica", 12), width=20)
        self.plane_prescript = Label(self.frame, text="y = ax + bz + c\na = tan(alpha), b = tan(beta)")
        self.plane_label.grid(row=next(row_counter), column=0, columnspan=2)
        self.plane_prescript.grid(row=next(row_counter), column=0, columnspan=2)

        a_row = next(row_counter)
        b_row = next(row_counter)
        c_row = next(row_counter)
        self.plane_a_label = Label(self.frame, text="a:")
        self.plane_b_label = Label(self.frame, text="b:")
        self.plane_c_label = Label(self.frame, text="c:")

        alpha_row = next(row_counter)
        beta_row = next(row_counter)
        self.plane_alpha_label = Label(self.frame, text="alpha")
        self.plane_beta_label = Label(self.frame, text="beta")

        self.plane_a = DoubleVar()
        self.plane_b = DoubleVar()
        self.plane_c = DoubleVar()

        self.plane_alpha = DoubleVar()
        self.plane_beta = DoubleVar()

        self.plane_a_input = Entry(self.frame, textvariable=self.plane_a)
        self.plane_a_input.bind('<Return>',
                                lambda event: self.plane_change(event, self.vis.plotter.plane, self.plane_a.get(), 'a'))
        self.plane_b_input = Entry(self.frame, textvariable=self.plane_b)
        self.plane_b_input.bind('<Return>',
                                lambda event: self.plane_change(event, self.vis.plotter.plane, self.plane_b.get(), 'b'))
        self.plane_c_input = Entry(self.frame, textvariable=self.plane_c)
        self.plane_c_input.bind('<Return>',
                                lambda event: self.plane_change(event, self.vis.plotter.plane, self.plane_c.get(), 'c'))

        self.plane_alpha_input = Scale(self.frame, variable=self.plane_alpha, tickinterval=0.01, from_=-80,
                                       to=80, orient=HORIZONTAL, length=120)
        self.plane_alpha_input.bind('<B1-Motion>', lambda event: self.plane_change(event, self.vis.plotter.plane,
                                                                                   self.plane_alpha.get(), 'alpha'))

        self.plane_beta_input = Scale(self.frame, variable=self.plane_beta, tickinterval=0.01, from_=-80, to=80,
                                      orient=HORIZONTAL, length=120)
        self.plane_beta_input.bind('<B1-Motion>',
                                   lambda event: self.plane_change(event, self.vis.plotter.plane, self.plane_beta.get(),
                                                                   'beta'))

        self.plane_a_label.grid(row=a_row, column=0)
        self.plane_b_label.grid(row=b_row, column=0)
        self.plane_c_label.grid(row=c_row, column=0)

        self.plane_a_input.grid(row=a_row, column=1)
        self.plane_b_input.grid(row=b_row, column=1)
        self.plane_c_input.grid(row=c_row, column=1)

        self.plane_alpha_label.grid(row=alpha_row, column=0)
        self.plane_beta_label.grid(row=beta_row, column=0)

        self.plane_alpha_input.grid(row=alpha_row, column=1)
        self.plane_beta_input.grid(row=beta_row, column=1)

        self.plane_update_btn = Button(self.frame, text="Update Plane",
                                       command=lambda: self.update_plane(self.vis.plotter.plane))
        self.plane_update_btn.grid(row=next(row_counter), column=0)

    def spiral_change(self, event, spiral, value, prop):
        if prop == 'radius':
            spiral.radius = value
        elif prop == 'velocity':
            spiral.velocity = value
        elif prop == 'omega':
            spiral.omega = value
        elif prop == 'acceleration':
            spiral.acceleration = value
        elif prop == 'period':
            spiral.period = value
        elif prop == 'frequency':
            spiral.frequency = value
        elif prop == 'x0':
            spiral.x0 = value
        elif prop == 'y0':
            spiral.y0 = value
        elif prop == 'z0':
            spiral.z0 = value
        elif prop == 'phi0':
            spiral.phi0 = value
        self.update_spiral_inputs(spiral)
        self.update_spiral(self.vis.plotter.spiral)
        self.vis.canvas.draw()

    def update_spiral_inputs(self, spiral):
        self.spiral_vars['radius'].set("{:.2f}".format(spiral.radius))
        self.spiral_vars['velocity'].set("{:.2f}".format(spiral.velocity))
        self.spiral_vars['omega'].set("{:.2f}".format(spiral.omega))
        self.spiral_vars['acceleration'].set("{:.2f}".format(spiral.acceleration))
        self.spiral_vars['period'].set("{:.2f}".format(spiral.period))
        self.spiral_vars['frequency'].set("{:.2f}".format(spiral.frequency))
        self.spiral_vars['x0'].set("{:.2f}".format(spiral.x0))
        self.spiral_vars['y0'].set("{:.2f}".format(spiral.y0))
        self.spiral_vars['z0'].set("{:.2f}".format(spiral.z0))
        self.spiral_vars['phi0'].set("{:.2f}".format(spiral.phi0))

    def update_spiral(self, spiral):
        plots = self.vis.plotter.plots

        X, Y, Z = spiral.calculate_trajectory()
        spiral_id = id(spiral)
        if spiral_id not in plots['xyz'].keys():
            return
        plots['xyz'][spiral_id]['main']._verts3d = (X, Z, Y)

        plots['xy'][spiral_id]['main'].set_xdata(X)
        plots['xy'][spiral_id]['main'].set_ydata(Y)

        plots['zy'][spiral_id]['main'].set_xdata(Z)
        plots['zy'][spiral_id]['main'].set_ydata(Y)

        plots['xz'][spiral_id]['main'].set_xdata(X)
        plots['xz'][spiral_id]['main'].set_ydata(Z)

    def plane_change(self, event, plane, value, prop):
        angle = False
        if prop == 'a':
            plane.a = value
            self.plane_a.set("{:.2f}".format(plane.a))
            self.plane_alpha.set("{:.2f}".format(math.degrees(plane.alpha)))
        elif prop == 'b':
            plane.b = value
            self.plane_b.set("{:.2f}".format(plane.b))
            self.plane_beta.set("{:.2f}".format(math.degrees(plane.beta)))
        elif prop == 'c':
            plane.c = value
            self.plane_c.set("{:.2f}".format(plane.c))
        elif prop == 'alpha':
            plane.alpha = math.radians(value)
            self.plane_alpha.set("{:.2f}".format(math.degrees(plane.alpha)))
            self.plane_a.set("{:.2f}".format(plane.a))
        elif prop == 'beta':
            plane.beta = math.radians(value)
            self.plane_beta.set("{:.2f}".format(math.degrees(plane.beta)))
            self.plane_b.set("{:.2f}".format(plane.b))
        self.update_plane(plane)
        self.update_traj(self.vis.plotter.proj)
        self.vis.canvas.draw()

    def update_plane_inputs(self, plane):
        self.plane_a.set("{:.2f}".format(plane.a))
        self.plane_b.set("{:.2f}".format(plane.b))
        self.plane_c.set("{:.2f}".format(plane.c))
        self.plane_alpha.set("{:.2f}".format(math.degrees(plane.alpha)))
        self.plane_beta.set("{:.2f}".format(math.degrees(plane.beta)))

    def update_plane(self, plane):
        plots = self.vis.plotter.plots
        plane_id = id(plane)

        x, y, z = plane.get_coords(self.vis.plotter.proj._last_calc[0][0],
                                   self.vis.plotter.proj._last_calc[0][-1],
                                   self.vis.plotter.proj._last_calc[2][0],
                                   self.vis.plotter.proj._last_calc[2][-1])
        for obj in plots['xyz'][plane_id].values():
            obj.remove()

        self.vis.plotter.plot_plane_3d(plane_id, x, y, z)

        plots['xy'][plane_id]['main'].set_xdata(x)
        plots['xy'][plane_id]['main'].set_ydata(y)

        plots['zy'][plane_id]['main'].set_xdata(z)
        plots['zy'][plane_id]['main'].set_ydata(y)

        plots['xz'][plane_id]['main'].set_xdata(x)
        plots['xz'][plane_id]['main'].set_ydata(z)

    def projectile_change(self, event, traj, value, prop):
        angle = False
        if prop == 'v0':
            traj.v0 = value
        elif prop == 'vx':
            traj._vel_x = value
        elif prop == 'vy':
            traj.vel_y = value
        elif prop == 'vz':
            traj.vel_z = value
        elif prop == 'x0':
            traj.x0 = value
        elif prop == 'y0':
            traj.y0 = value
        elif prop == 'z0':
            traj.z0 = value
        elif prop == 'alpha':
            angle = True
            traj.alpha = math.radians(value)
        elif prop == 'theta':
            angle = True
            traj.theta = math.radians(value)
        self.update_projectile_inputs(traj, angle)
        self.update_traj(self.vis.plotter.proj)
        self.vis.canvas.draw()

    def update_projectile_inputs(self, traj, angle):
        self.proj1_v0.set("{:.2f}".format(traj.v0))
        self.proj1_vx.set("{:.2f}".format(traj.vel_x))
        self.proj1_vy.set("{:.2f}".format(traj.vel_y))
        self.proj1_vz.set("{:.2f}".format(traj.vel_z))
        self.proj1_x0.set("{:.2f}".format(traj.x0))
        self.proj1_y0.set("{:.2f}".format(traj.y0))
        self.proj1_z0.set("{:.2f}".format(traj.z0))
        if not angle:
            self.proj1_alpha.set(math.degrees(traj.alpha))
            self.proj1_theta.set(math.degrees(traj.theta))
        a_pos = traj.a_pos()
        self.proj1_point_a.set("A = [{:.2f} , {:.2f} , {:.2f}]".format(a_pos[0], a_pos[1], a_pos[2]))
        b_pos = traj.b_pos()
        self.proj1_point_b.set("B = [{:.2f} , {:.2f} , {:.2f}]".format(b_pos[0], b_pos[1], b_pos[2]))
        c_pos = traj.c_pos()
        self.proj1_point_c.set("C = [{:.2f} , {:.2f} , {:.2f}]".format(c_pos[0], c_pos[1], c_pos[2]))
        d_pos = traj.d_pos()
        self.proj1_point_d.set("D = [{:.2f} , {:.2f} , {:.2f}]".format(d_pos[0], d_pos[1], d_pos[2]))

    def display_coords(self, x, y):
        if x < 0:
            pol_x = '-'
        else:
            pol_x = '+'
        if y < 0:
            pol_y = '-'
        else:
            pol_y = '+'
        self.coord.set("[{}{:2.3f} , {}{:2.3f}]".format(pol_x, abs(x), pol_y, abs(y)))
        return ''

    def update_traj(self, traj):
        plots = self.vis.plotter.plots

        xyz = traj.calculate_trajectory()
        X = xyz[0]
        Y = xyz[1]
        Z = xyz[2]
        b_pos = traj.b_pos()
        c_pos = traj.c_pos()

        traj_id = id(traj)
        if traj_id not in plots['xyz'].keys():
            return
        plots['xyz'][traj_id]['main']._verts3d = (X, Z, Y)
        plots['xyz'][traj_id]['A']._verts3d = ([X[0]], [Z[0]], [Y[0]])
        plots['xyz'][traj_id]['B']._verts3d = ([b_pos[0]], [b_pos[2]], [b_pos[1]])
        plots['xyz'][traj_id]['C']._verts3d = ([c_pos[0]], [c_pos[2]], [c_pos[1]])
        plots['xyz'][traj_id]['D']._verts3d = ([X[-1]], [Z[-1]], [Y[-1]])
        plots['xyz'][traj_id]['A0']._verts3d = ([X[0], X[0]], [Z[0], Z[0]], [0, Y[0]])

        plots['xy'][traj_id]['main'].set_xdata(X)
        plots['xy'][traj_id]['main'].set_ydata(Y)
        plots['xy'][traj_id]['A'].set_xdata([X[0]])
        plots['xy'][traj_id]['A'].set_ydata([Y[0]])
        plots['xy'][traj_id]['B'].set_xdata([b_pos[0]])
        plots['xy'][traj_id]['B'].set_ydata([b_pos[1]])
        plots['xy'][traj_id]['C'].set_xdata([c_pos[0]])
        plots['xy'][traj_id]['C'].set_ydata([c_pos[1]])
        plots['xy'][traj_id]['D'].set_xdata([X[-1]])
        plots['xy'][traj_id]['D'].set_ydata([Y[-1]])
        plots['xy'][traj_id]['A0'].set_xdata([X[0], X[0]])
        plots['xy'][traj_id]['A0'].set_ydata([0, Y[0]])

        plots['zy'][traj_id]['main'].set_xdata(Z)
        plots['zy'][traj_id]['main'].set_ydata(Y)
        plots['zy'][traj_id]['A'].set_xdata([Z[0]])
        plots['zy'][traj_id]['A'].set_ydata([Y[0]])
        plots['zy'][traj_id]['B'].set_xdata([b_pos[2]])
        plots['zy'][traj_id]['B'].set_ydata([b_pos[1]])
        plots['zy'][traj_id]['C'].set_xdata([c_pos[2]])
        plots['zy'][traj_id]['C'].set_ydata([c_pos[1]])
        plots['zy'][traj_id]['D'].set_xdata([Z[-1]])
        plots['zy'][traj_id]['D'].set_ydata([Y[-1]])
        plots['zy'][traj_id]['A0'].set_xdata([Z[0], Z[0]])
        plots['zy'][traj_id]['A0'].set_ydata([0, Y[0]])

        plots['xz'][traj_id]['main'].set_xdata(X)
        plots['xz'][traj_id]['main'].set_ydata(Z)
        plots['xz'][traj_id]['A'].set_xdata([X[0]])
        plots['xz'][traj_id]['A'].set_ydata([Z[0]])
        plots['xz'][traj_id]['B'].set_xdata([b_pos[0]])
        plots['xz'][traj_id]['B'].set_ydata([b_pos[2]])
        plots['xz'][traj_id]['C'].set_xdata([c_pos[0]])
        plots['xz'][traj_id]['C'].set_ydata([c_pos[2]])
        plots['xz'][traj_id]['D'].set_xdata([X[-1]])
        plots['xz'][traj_id]['D'].set_ydata([Z[-1]])
