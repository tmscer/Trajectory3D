import math
import itertools

try:
    from matplotlib import pyplot
except ImportError:
    raise ImportError("Visualizer requires module Matplotlib")

try:
    from tkinter import *
except ImportError:
    raise ImportError("Visualizer require module tkinter")

import app_style as style
from details_window import *
from scrollable_side_panel import *


class MainWindow:

    def __init__(self, vis):
        self.vis = vis

        self.side_frame = Frame(self.vis.tk_root, width=style.panel.width)
        self.side_frame.pack(side=RIGHT, fill=BOTH)

        self._row_counter = (x for x in itertools.count(start=0, step=1))

        self.side_panel = ScrollableSidePanel(self.side_frame)

        # GUI
        self.coord = StringVar(value="[x , y]")
        self.coord_label = Label(self.side_panel, font=style.panel.large_text, textvariable=self.coord)
        self.coord_label.grid(row=self._next_row(), column=0, columnspan=2)
        self.top_spacer = Label(self.side_panel, text="\t\t\t", width=5)
        self.top_spacer.grid(row=self._next_row(), column=0)

        self._create_globals_gui()
        self._create_parabola_gui()
        self._create_spiral_gui()
        self._create_plane_gui()

    def _create_globals_gui(self):
        self.globals_label = Label(self.side_panel, font=style.panel.large_text, text="Globals", width=20)
        self.globals_label.grid(row=self._next_row(), column=0, columnspan=2)

        self.g_value = DoubleVar()
        self.g_label = Label(self.side_panel, text='g:')
        self.g_input = Entry(self.side_panel, textvariable=self.g_value)
        self.g_input.bind('<Return>',
                          lambda event: self.grav_acceleration_change(event, self.g_value.get()))
        g_row = self._next_row()
        self.g_label.grid(row=g_row, column=0)
        self.g_input.grid(row=g_row, column=1)

        low_btn_row = row = self._next_row()

        self.plane_update_btn = Button(self.side_panel, text="Update Plane",
                                       command=lambda: self.plane_change(None, self.vis.plotter.plane, None, ''))
        self.plane_update_btn.grid(row=low_btn_row, column=0)

        self.details_window = None
        self.toggle_details_btn = Button(self.side_panel, text="Details",
                                         command=lambda: self.toggle_details())
        self.toggle_details_btn.grid(row=low_btn_row, column=1)

    def _create_parabola_gui(self):
        self.parabola_label = Label(self.side_panel, font=style.panel.large_text, text="Parabolic Trajectory", width=20)
        self.parabola_label.grid(row=self._next_row(), column=0, columnspan=2)

        self.parabola_prescript = Label(self.side_panel, text="x(t) = v0 * cos (alpha) * cos(omega) * t + x0\ny(t) = v0 * sin(alpha) - 0.5 * g * t ** 2 + y0\nz(t) = v0 * cos(alpha) * sin(omega) * t + z0")
        self.parabola_prescript.grid(row=self._next_row(), column=0, columnspan=2)

        self.parabola_v0 = DoubleVar()
        self.parabola_vx = DoubleVar()
        self.parabola_vy = DoubleVar()
        self.parabola_vz = DoubleVar()
        self.parabola_x0 = DoubleVar()
        self.parabola_y0 = DoubleVar()
        self.parabola_z0 = DoubleVar()
        self.parabola_alpha = DoubleVar()
        self.parabola_theta = DoubleVar()

        self.parabola_v0_input = Entry(self.side_panel, textvariable=self.parabola_v0)
        self.parabola_v0_input.bind('<Return>',
                                 lambda event: self.parabola_change(event, self.vis.plotter.parabola,
                                                                    self.parabola_v0.get(),
                                                                      'v0'))

        self.parabola_vx_input = Entry(self.side_panel, textvariable=self.parabola_vx)
        self.parabola_vx_input.bind('<Return>',
                                 lambda event: self.parabola_change(event, self.vis.plotter.parabola,
                                                                    self.parabola_vx.get(),
                                                                      'vx'))

        self.parabola_vy_input = Entry(self.side_panel, textvariable=self.parabola_vy)
        self.parabola_vy_input.bind('<Return>',
                                 lambda event: self.parabola_change(event, self.vis.plotter.parabola,
                                                                    self.parabola_vy.get(),
                                                                      'vy'))

        self.parabola_vz_input = Entry(self.side_panel, textvariable=self.parabola_vz)
        self.parabola_vz_input.bind('<Return>',
                                 lambda event: self.parabola_change(event, self.vis.plotter.parabola,
                                                                    self.parabola_vz.get(),
                                                                      'vz'))

        self.parabola_x0_input = Entry(self.side_panel, textvariable=self.parabola_x0)
        self.parabola_x0_input.bind('<Return>',
                                 lambda event: self.parabola_change(event, self.vis.plotter.parabola,
                                                                    self.parabola_x0.get(),
                                                                      'x0'))

        self.parabola_y0_input = Entry(self.side_panel, textvariable=self.parabola_y0)
        self.parabola_y0_input.bind('<Return>',
                                 lambda event: self.parabola_change(event, self.vis.plotter.parabola,
                                                                    self.parabola_y0.get(),
                                                                      'y0'))

        self.parabola_z0_input = Entry(self.side_panel, textvariable=self.parabola_z0)
        self.parabola_z0_input.bind('<Return>',
                                 lambda event: self.parabola_change(event, self.vis.plotter.parabola,
                                                                    self.parabola_z0.get(),
                                                                      'z0'))

        self.parabola_alpha_input = Scale(self.side_panel, tickinterval=0.01, from_=0, to=90, orient=HORIZONTAL,
                                       variable=self.parabola_alpha, length=120)
        self.parabola_alpha_input.bind('<B1-Motion>', lambda event: self.parabola_change(event, self.vis.plotter.parabola,
                                                                                      self.parabola_alpha.get(),
                                                                                        'alpha'))

        self.parabola_theta_input = Scale(self.side_panel, tickinterval=0.01, from_=0, to=360, orient=HORIZONTAL,
                                       variable=self.parabola_theta, length=120)
        self.parabola_theta_input.bind('<B1-Motion>', lambda event: self.parabola_change(event, self.vis.plotter.parabola,
                                                                                      self.parabola_theta.get(),
                                                                                        'theta'))

        v0_row = self._next_row()
        vx_row = self._next_row()
        vy_row = self._next_row()
        vz_row = self._next_row()
        self.parabola_v0_input.grid(row=v0_row, column=1)
        self.parabola_vx_input.grid(row=vx_row, column=1)
        self.parabola_vy_input.grid(row=vy_row, column=1)
        self.parabola_vz_input.grid(row=vz_row, column=1)

        x0_row = self._next_row()
        y0_row = self._next_row()
        z0_row = self._next_row()
        self.parabola_x0_input.grid(row=x0_row, column=1)
        self.parabola_y0_input.grid(row=y0_row, column=1)
        self.parabola_z0_input.grid(row=z0_row, column=1)

        alpha_row = next(self._row_counter)
        theta_row = self._next_row()
        self.parabola_alpha_input.grid(row=alpha_row, column=1)
        self.parabola_theta_input.grid(row=theta_row, column=1)

        self.parabola_v0_label = Label(self.side_panel, text="v0:")
        self.parabola_vx_label = Label(self.side_panel, text="vx:")
        self.parabola_vy_label = Label(self.side_panel, text="vy:")
        self.parabola_vz_label = Label(self.side_panel, text="vz:")
        self.parabola_x0_label = Label(self.side_panel, text="x0:")
        self.parabola_y0_label = Label(self.side_panel, text="y0:")
        self.parabola_z0_label = Label(self.side_panel, text="z0:")
        self.parabola_alpha_label = Label(self.side_panel, text="alpha:")
        self.parabola_theta_label = Label(self.side_panel, text="theta:")

        self.parabola_v0_label.grid(row=v0_row, column=0)
        self.parabola_vx_label.grid(row=vx_row, column=0)
        self.parabola_vy_label.grid(row=vy_row, column=0)
        self.parabola_vz_label.grid(row=vz_row, column=0)

        self.parabola_x0_label.grid(row=x0_row, column=0)
        self.parabola_y0_label.grid(row=y0_row, column=0)
        self.parabola_z0_label.grid(row=z0_row, column=0)

        self.parabola_alpha_label.grid(row=alpha_row, column=0)
        self.parabola_theta_label.grid(row=theta_row, column=0)

        self.parabola_point_a = StringVar()
        self.parabola_point_a_label = Label(self.side_panel, textvariable=self.parabola_point_a)
        self.parabola_point_b = StringVar()
        self.parabola_point_b_label = Label(self.side_panel, textvariable=self.parabola_point_b)
        self.parabola_point_c = StringVar()
        self.parabola_point_c_label = Label(self.side_panel, textvariable=self.parabola_point_c)
        self.parabola_point_d = StringVar()
        self.parabola_point_d_label = Label(self.side_panel, textvariable=self.parabola_point_d)

        self.parabola_point_a_label.grid(row=self._next_row(), column=0, columnspan=2)
        self.parabola_point_b_label.grid(row=self._next_row(), column=0, columnspan=2)
        self.parabola_point_c_label.grid(row=self._next_row(), column=0, columnspan=2)
        self.parabola_point_d_label.grid(row=self._next_row(), column=0, columnspan=2)

        self.parabola_total_time_value = StringVar()
        self.parabola_total_time_display = Label(self.side_panel, textvariable=self.parabola_total_time_value)
        self.parabola_total_time_display.grid(row=self._next_row(), column=0, columnspan=2)

    def _create_spiral_gui(self):
        self.spiral_label = Label(self.side_panel, text="Spiral Trajectory", font=style.panel.large_text, width=20)
        self.spiral_prescript = Label(self.side_panel,
                                      text="x(t) = r * cos (omega * t) + x0\ny(t) = y0 - 0.5 * g * t ** 2\nz(t) = r * sin(omega * t) + z0")
        self.spiral_label.grid(row=self._next_row(), column=0, columnspan=2)
        self.spiral_prescript.grid(row=self._next_row(), column=0, columnspan=2)

        self.spiral_locked_var = StringVar(self.side_panel)
        self.spiral_locked_var.set('radius')  # default value

        def lm(*args):
            self.vis.plotter.spiral.locked_var = self.spiral_locked_var.get()

        self.spiral_locked_var.trace('w', lm)

        self.spiral_locked_var_label = Label(self.side_panel, text='Locked Variable')
        self.spiral_locked_var_input = OptionMenu(self.side_panel, self.spiral_locked_var,
                                                  'radius', 'velocity', 'omega', 'acceleration')
        locked_var_row = self._next_row()
        self.spiral_locked_var_label.grid(row=locked_var_row, column=0)
        self.spiral_locked_var_input.grid(row=locked_var_row, column=1)

        self.spiral_value_names = ['radius', 'velocity', 'omega', 'acceleration', 'period', 'frequency', 'x0', 'y0',
                                   'z0', 'phi0']

        self.spiral_vars = {label: DoubleVar() for label in self.spiral_value_names}

        self.spiral_labels = {label: Label(self.side_panel, text=label) for label in self.spiral_value_names}
        self.spiral_inputs = {label: Entry(self.side_panel, textvariable=self.spiral_vars[label]) for label in
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
            row_index = self._next_row()
            self.spiral_labels[name].grid(row=row_index, column=0)
            self.spiral_inputs[name].grid(row=row_index, column=1)

        self.spiral_start_point = StringVar()
        self.spiral_final_point = StringVar()
        self.spiral_time_value = StringVar()

        self.spiral_start_point_display = Label(self.side_panel, textvariable=self.spiral_start_point)
        self.spiral_start_point_display.grid(row=self._next_row(), column=0, columnspan=2)

        self.spiral_final_point_display = Label(self.side_panel, textvariable=self.spiral_final_point)
        self.spiral_final_point_display.grid(row=self._next_row(), column=0, columnspan=2)

        self.spiral_total_time_display = Label(self.side_panel, textvariable=self.spiral_time_value)
        self.spiral_total_time_display.grid(row=self._next_row(), column=0, columnspan=2)

    def _create_plane_gui(self):
        self.plane_label = Label(self.side_panel, text="Plane", font=style.panel.large_text, width=20)
        self.plane_prescript = Label(self.side_panel, text="y = ax + bz + c\na = tan(alpha), b = tan(beta)")
        self.plane_label.grid(row=self._next_row(), column=0, columnspan=2)
        self.plane_prescript.grid(row=self._next_row(), column=0, columnspan=2)

        a_row = self._next_row()
        b_row = self._next_row()
        c_row = self._next_row()
        self.plane_a_label = Label(self.side_panel, text="a:")
        self.plane_b_label = Label(self.side_panel, text="b:")
        self.plane_c_label = Label(self.side_panel, text="c:")

        alpha_row = self._next_row()
        beta_row = self._next_row()
        self.plane_alpha_label = Label(self.side_panel, text="alpha")
        self.plane_beta_label = Label(self.side_panel, text="beta")

        self.plane_a = DoubleVar()
        self.plane_b = DoubleVar()
        self.plane_c = DoubleVar()

        self.plane_alpha = DoubleVar()
        self.plane_beta = DoubleVar()

        self.plane_a_input = Entry(self.side_panel, textvariable=self.plane_a)
        self.plane_a_input.bind('<Return>',
                                lambda event: self.plane_change(event, self.vis.plotter.plane, self.plane_a.get(), 'a'))
        self.plane_b_input = Entry(self.side_panel, textvariable=self.plane_b)
        self.plane_b_input.bind('<Return>',
                                lambda event: self.plane_change(event, self.vis.plotter.plane, self.plane_b.get(), 'b'))
        self.plane_c_input = Entry(self.side_panel, textvariable=self.plane_c)
        self.plane_c_input.bind('<Return>',
                                lambda event: self.plane_change(event, self.vis.plotter.plane, self.plane_c.get(), 'c'))

        self.plane_alpha_input = Scale(self.side_panel, variable=self.plane_alpha, tickinterval=0.01, from_=-80,
                                       to=80, orient=HORIZONTAL, length=120)
        self.plane_alpha_input.bind('<B1-Motion>', lambda event: self.plane_change(event, self.vis.plotter.plane,
                                                                                   self.plane_alpha.get(), 'alpha'))

        self.plane_beta_input = Scale(self.side_panel, variable=self.plane_beta, tickinterval=0.01, from_=-80, to=80,
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

    def toggle_details(self):
        if self.details_window is None:
            self.details_window = DetailsWindow(self.vis, master=self.vis.tk_root)
        self.details_window.show()

    def grav_acceleration_change(self, event, value):
        if value > 0:
            self.vis.plotter.parabola.g = value
            self.vis.plotter.spiral.g = value
            # Update Parabola
            self.vis.plotter.update_traj()
            self.update_parabola_points(self.vis.plotter.parabola)
            # Update Spiral
            self.vis.plotter.update_spiral()
            self.vis.canvas.draw()
        self.g_value.set(self.vis.plotter.parabola.g)
        if self.details_window is not None:
            self.details_window.redraw()
        self.vis.plotter.adjust_axes()

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
        self.vis.plotter.update_spiral()
        if self.details_window is not None:
            self.details_window.redraw()
        self.vis.plotter.adjust_axes()
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
        self.spiral_start_point.set("E = [{:.2f}, {:.2f}, {:.2f}]".format(spiral.x0, spiral.y0, spiral.z0))
        self.spiral_final_point.set("F = [{:.2f}, {:.2f}, {:.2f}]".format(spiral._last_calc[0][-1], spiral._last_calc[1][-1], spiral._last_calc[2][-1]))
        self.spiral_time_value.set("Total time: {:.2f} s".format(spiral._last_calc[3][-1]))

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
        self.vis.plotter.update_plane(plane)
        self.vis.plotter.update_traj()
        self.vis.plotter.update_spiral()
        if self.details_window is not None:
            self.details_window.redraw()
        self.vis.plotter.adjust_axes()
        self.vis.canvas.draw()

    def update_plane_inputs(self, plane):
        self.plane_a.set("{:.2f}".format(plane.a))
        self.plane_b.set("{:.2f}".format(plane.b))
        self.plane_c.set("{:.2f}".format(plane.c))
        self.plane_alpha.set("{:.2f}".format(math.degrees(plane.alpha)))
        self.plane_beta.set("{:.2f}".format(math.degrees(plane.beta)))

    def parabola_change(self, event, parabola, value, prop):
        angle = False
        if prop == 'v0':
            parabola.v0 = value
        elif prop == 'vx':
            parabola._vel_x = value
        elif prop == 'vy':
            parabola.vel_y = value
        elif prop == 'vz':
            parabola.vel_z = value
        elif prop == 'x0':
            parabola.x0 = value
        elif prop == 'y0':
            parabola.y0 = value
        elif prop == 'z0':
            parabola.z0 = value
        elif prop == 'alpha':
            angle = True
            parabola.alpha = math.radians(value)
        elif prop == 'theta':
            angle = True
            parabola.theta = math.radians(value)
        self.update_projectile_inputs(parabola, angle)
        self.update_parabola_points(parabola)
        self.vis.plotter.update_traj()
        if self.details_window is not None:
            self.details_window.redraw()
        self.vis.plotter.adjust_axes()
        self.vis.canvas.draw()

    def update_projectile_inputs(self, parabola, angle):
        self.parabola_v0.set("{:.2f}".format(parabola.v0))
        self.parabola_vx.set("{:.2f}".format(parabola.vel_x))
        self.parabola_vy.set("{:.2f}".format(parabola.vel_y))
        self.parabola_vz.set("{:.2f}".format(parabola.vel_z))
        self.parabola_x0.set("{:.2f}".format(parabola.x0))
        self.parabola_y0.set("{:.2f}".format(parabola.y0))
        self.parabola_z0.set("{:.2f}".format(parabola.z0))
        if angle:
            self.parabola_alpha.set(math.degrees(parabola.alpha))
            self.parabola_theta.set(math.degrees(parabola.theta))
        self.parabola_total_time_value.set("Total time: {:.2f} s".format(parabola._last_calc[3][-1]))

    def update_parabola_points(self, parabola):
        a_pos = parabola.a_pos()
        self.parabola_point_a.set("A = [{:.2f} , {:.2f} , {:.2f}]".format(a_pos[0], a_pos[1], a_pos[2]))
        b_pos = parabola.b_pos()
        self.parabola_point_b.set("B = [{:.2f} , {:.2f} , {:.2f}]".format(b_pos[0], b_pos[1], b_pos[2]))
        c_pos = parabola.c_pos()
        self.parabola_point_c.set("C = [{:.2f} , {:.2f} , {:.2f}]".format(c_pos[0], c_pos[1], c_pos[2]))
        d_pos = parabola.d_pos()
        if None not in d_pos:
            self.parabola_point_d.set("D = [{:.2f} , {:.2f} , {:.2f}]".format(d_pos[0], d_pos[1], d_pos[2]))

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

    def _next_row(self):
        return next(self._row_counter)
