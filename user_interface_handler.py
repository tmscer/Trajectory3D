from math import pi

try:
    from matplotlib import pyplot
except ImportError:
    raise ImportError("Visualizer requires module Matplotlib")

try:
    from tkinter import *
except ImportError:
    raise ImportError("Visualizer require module tkinter")


class UserInterfaceHandler:

    def __init__(self, vis):
        self.vis = vis
        # build the ui
        self.option_window = Toplevel()
        self.option_window.geometry("500x800+250+125")
        self.option_window.wm_title("Visualizer Toolbar")

        self.coord = StringVar(value="[x , y]")
        self.coord_label = Label(self.option_window, font=("Helvetica", 15), textvariable=self.coord)
        self.coord_label.grid(row=0, column=0, columnspan=2)
        self.top_spacer = Label(self.option_window, text="\t\t\t", width=50)
        self.top_spacer.grid(row=1, column=0)

        self.proj1_label = Label(self.option_window, font=("Helvetica", 12), text="Trajectory one")
        self.proj1_label.grid(row=2, column=0)

        self.proj1_v0 = DoubleVar()
        self.proj1_vx = DoubleVar()
        self.proj1_vy = DoubleVar()
        self.proj1_vz = DoubleVar()
        self.proj1_x0 = DoubleVar()
        self.proj1_y0 = DoubleVar()
        self.proj1_z0 = DoubleVar()
        self.proj1_alpha = DoubleVar()
        self.proj1_theta = DoubleVar()

        self.proj1_v0_input = Entry(self.option_window, textvariable=self.proj1_v0)
        self.proj1_v0_input.bind('<Return>', lambda event: self.projectile_change(event, self.vis.plotter.proj, 0, self.proj1_v0.get(), 'v0'))

        self.proj1_vx_input = Entry(self.option_window, textvariable=self.proj1_vx)
        self.proj1_vx_input.bind('<Return>', lambda event: self.projectile_change(event, self.vis.plotter.proj, 0, self.proj1_vx.get(), 'vx'))

        self.proj1_vy_input = Entry(self.option_window, textvariable=self.proj1_vy)
        self.proj1_vy_input.bind('<Return>', lambda event: self.projectile_change(event, self.vis.plotter.proj, 0, self.proj1_vy.get(), 'vy'))

        self.proj1_vz_input = Entry(self.option_window, textvariable=self.proj1_vz)
        self.proj1_vz_input.bind('<Return>', lambda event: self.projectile_change(event, self.vis.plotter.proj, 0, self.proj1_vz.get(), 'vz'))

        self.proj1_x0_input = Entry(self.option_window, textvariable=self.proj1_x0)
        self.proj1_x0_input.bind('<Return>', lambda event: self.projectile_change(event, self.vis.plotter.proj, 0, self.proj1_x0.get(), 'x0'))

        self.proj1_y0_input = Entry(self.option_window, textvariable=self.proj1_y0)
        self.proj1_y0_input.bind('<Return>', lambda event: self.projectile_change(event, self.vis.plotter.proj, 0, self.proj1_y0.get(), 'y0'))

        self.proj1_z0_input = Entry(self.option_window, textvariable=self.proj1_z0)
        self.proj1_z0_input.bind('<Return>', lambda event: self.projectile_change(event, self.vis.plotter.proj, 0, self.proj1_z0.get(), 'z0'))

        self.proj1_alpha_input = Scale(self.option_window, from_=0, to=90, orient=HORIZONTAL, variable=self.proj1_alpha, length=120)
        self.proj1_alpha_input.bind('<B1-Motion>', lambda event: self.projectile_change(event, self.vis.plotter.proj, 0, self.proj1_alpha.get(), 'alpha'))

        self.proj1_theta_input = Scale(self.option_window, from_=0, to=360, orient=HORIZONTAL, variable=self.proj1_theta, length=120)
        self.proj1_theta_input.bind('<B1-Motion>', lambda event: self.projectile_change(event, self.vis.plotter.proj, 0, self.proj1_theta.get(), 'theta'))

        self.proj1_v0_input.grid(row=3, column=1)
        self.proj1_vx_input.grid(row=4, column=1)
        self.proj1_vy_input.grid(row=5, column=1)
        self.proj1_vz_input.grid(row=6, column=1)

        self.proj1_x0_input.grid(row=7, column=1)
        self.proj1_y0_input.grid(row=8, column=1)
        self.proj1_z0_input.grid(row=9, column=1)

        self.proj1_alpha_input.grid(row=10, column=1)
        self.proj1_theta_input.grid(row=11, column=1)

        self.proj1_v0_label = Label(self.option_window, text="v0:")
        self.proj1_vx_label = Label(self.option_window, text="vx:")
        self.proj1_vy_label = Label(self.option_window, text="vy:")
        self.proj1_vz_label = Label(self.option_window, text="vz:")
        self.proj1_x0_label = Label(self.option_window, text="x0:")
        self.proj1_y0_label = Label(self.option_window, text="y0:")
        self.proj1_z0_label = Label(self.option_window, text="z0:")
        self.proj1_alpha_label = Label(self.option_window, text="alpha:")
        self.proj1_theta_label = Label(self.option_window, text="theta:")

        self.proj1_v0_label.grid(row=3, column=0)
        self.proj1_vx_label.grid(row=4, column=0)
        self.proj1_vy_label.grid(row=5, column=0)
        self.proj1_vz_label.grid(row=6, column=0)

        self.proj1_x0_label.grid(row=7, column=0)
        self.proj1_y0_label.grid(row=8, column=0)
        self.proj1_z0_label.grid(row=9, column=0)

        self.proj1_alpha_label.grid(row=10, column=0)
        self.proj1_theta_label.grid(row=11, column=0)

        self.proj1_point_a = StringVar()
        self.proj1_point_a_label = Label(self.option_window, textvariable=self.proj1_point_a)
        self.proj1_point_b = StringVar()
        self.proj1_point_b_label = Label(self.option_window, textvariable=self.proj1_point_b)
        self.proj1_point_c = StringVar()
        self.proj1_point_c_label = Label(self.option_window, textvariable=self.proj1_point_c)
        self.proj1_point_d = StringVar()
        self.proj1_point_d_label = Label(self.option_window, textvariable=self.proj1_point_d)

        self.proj1_point_a_label.grid(row=12, column=0)
        self.proj1_point_b_label.grid(row=13, column=0)
        self.proj1_point_c_label.grid(row=14, column=0)
        self.proj1_point_d_label.grid(row=15, column=0)

        self.plane_label = Label(self.option_window, text="Plane")
        self.plane_prescript = Label(self.option_window, text="y = ax + bz + c")

        self.plane_a_label = Label(self.option_window)
        self.plane_b_label = Label(self.option_window)
        self.plane_c_label = Label(self.option_window)

        self.plane_a = DoubleVar()
        self.plane_b = DoubleVar()
        self.plane_c = DoubleVar()

        self.plane_a_input = Entry(self.option_window, textvariable=self.plane_a)
        self.plane_a_input.bind('<Return>', lambda event: self.plane_change(event, self.vis.plotter.proj, 0, self.plane_a.get(), 'a'))
        self.plane_a_input = Entry(self.option_window, textvariable=self.plane_b)
        self.plane_a_input.bind('<Return>', lambda event: self.plane_change(event, self.vis.plotter.proj, 0, self.plane_b.get(), 'b'))
        self.plane_a_input = Entry(self.option_window, textvariable=self.plane_c)
        self.plane_a_input.bind('<Return>', lambda event: self.plane_change(event, self.vis.plotter.proj, 0, self.plane_c.get(), 'c'))

    @staticmethod
    def number_validation(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def plane_change(self, event, plane, proj, value, prop):
        pass

    def plotter_callback(self):
        self.update_inputs(self.vis.plotter.proj, 0)

    def update_inputs(self, traj, proj, angle):
        if proj == 0:
            self.proj1_v0.set("{:.2f}".format(traj.v0))
            self.proj1_vx.set("{:.2f}".format(traj.vel_x))
            self.proj1_vy.set("{:.2f}".format(traj.vel_y))
            self.proj1_vz.set("{:.2f}".format(traj.vel_z))
            self.proj1_x0.set("{:.2f}".format(traj.x0))
            self.proj1_y0.set("{:.2f}".format(traj.y0))
            self.proj1_z0.set("{:.2f}".format(traj.z0))
            if not angle:
                self.proj1_alpha.set(traj.alpha * 180 / pi)
                self.proj1_theta.set(traj.theta * 180 / pi)
            a_pos = traj.a_pos()
            self.proj1_point_a.set("A = [{:.2f} , {:.2f} , {:.2f}]".format(a_pos[0], a_pos[1], a_pos[2]))
            b_pos = traj.b_pos()
            self.proj1_point_b.set("B = [{:.2f} , {:.2f} , {:.2f}]".format(b_pos[0], b_pos[1], b_pos[2]))
            c_pos = traj.c_pos()
            self.proj1_point_c.set("C = [{:.2f} , {:.2f} , {:.2f}]".format(c_pos[0], c_pos[1], c_pos[2]))
            d_pos = traj.d_pos()
            self.proj1_point_d.set("D = [{:.2f} , {:.2f} , {:.2f}]".format(d_pos[0], d_pos[1], d_pos[2]))

    def projectile_change(self, event, traj, proj, value, prop):
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
            if value < 0:
                return
            traj.y0 = value
        elif prop == 'z0':
            traj.z0 = value
        elif prop == 'alpha':
            traj.alpha = self.to_rad(value)
            angle = True
        elif prop == 'theta':
            traj.theta = self.to_rad(value)
            angle = True
        self.update_inputs(traj, proj, angle)
        self.update_traj(traj)

    @staticmethod
    def to_rad(d):
        return d * pi / 180

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

    def btn(self, event2=None):
        self.update_traj(self.vis.plotter.proj)

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

        self.vis.canvas.draw()
