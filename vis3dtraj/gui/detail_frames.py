from tkinter import *
import itertools


class _DetailsFrame(Frame):

    def __init__(self, **kw):
        super().__init__(**kw)
        self._row_counter = (x for x in itertools.count(start=0, step=1))

    def _next_row(self):
        return next(self._row_counter)


class ParabolaDetailsFrame(_DetailsFrame):

    def __init__(self, parent, axis, parabola, **kw):
        super().__init__(**kw)
        self.parent = parent
        self.axis = axis
        self.parabola = parabola

        self.show_pos_x = IntVar()
        self.show_pos_y = IntVar()
        self.show_pos_z = IntVar()
        self.show_vel_y = IntVar()

        self.show_pos_x_input = Checkbutton(self, text="Show X (blue)", variable=self.show_pos_x)
        self.show_pos_y_input = Checkbutton(self, text="Show Y (orange)", variable=self.show_pos_y)
        self.show_pos_z_input = Checkbutton(self, text="Show Z (green)", variable=self.show_pos_z)
        self.show_vel_y_input = Checkbutton(self, text="Show Vy (red)", variable=self.show_vel_y)

        self.show_pos_x.trace('w', lambda *args: self.redraw())
        self.show_pos_y.trace('w', lambda *args: self.redraw())
        self.show_pos_z.trace('w', lambda *args: self.redraw())
        self.show_vel_y.trace('w', lambda *args: self.redraw())

        self.show_pos_x_input.pack(anchor=W)
        self.show_pos_y_input.pack(anchor=W)
        self.show_pos_z_input.pack(anchor=W)
        self.show_vel_y_input.pack(anchor=W)

        self._on_focus()

    def on_focus(self):
        self._on_focus()

    def _on_focus(self):
        self.line_x = self.axis.plot([], [], label='X')[0]
        self.line_y = self.axis.plot([], [], label='Y')[0]
        self.line_z = self.axis.plot([], [], label='Z')[0]
        self.line_vel_y = self.axis.plot([], [], label='VEL Y')[0]
        self.redraw()

    def redraw(self):
        X, Y, Z, T = self.parabola.calculate_trajectory()
        if self.show_pos_x.get() == 1:
            self.line_x.set_xdata(T)
            self.line_x.set_ydata(X)
        else:
            self.line_x.set_xdata([])
            self.line_x.set_ydata([])

        if self.show_pos_y.get() == 1:
            self.line_y.set_xdata(T)
            self.line_y.set_ydata(Y)
        else:
            self.line_y.set_xdata([])
            self.line_y.set_ydata([])

        if self.show_pos_z.get() == 1:
            self.line_z.set_xdata(T)
            self.line_z.set_ydata(Z)
        else:
            self.line_z.set_xdata([])
            self.line_z.set_ydata([])

        if self.show_vel_y.get() == 1:
            vals = [self.parabola.vy(t) for t in T]
            self.line_vel_y.set_xdata(T)
            self.line_vel_y.set_ydata(vals)
        else:
            self.line_vel_y.set_xdata([])
            self.line_vel_y.set_ydata([])

        if self.parent.lock_axis.get() == 0:
            self.axis.relim()
            self.axis.autoscale_view()
        self.parent.canvas.draw()


class SpiralDetailsFrame(_DetailsFrame):

    def __init__(self, parent, axis, spiral, **kw):
        super().__init__(**kw)
        self.spiral = spiral
        self.parent = parent
        self.axis = axis

        self.show_pos_x = IntVar()
        self.show_pos_y = IntVar()
        self.show_pos_z = IntVar()
        self.show_vel_x = IntVar()
        self.show_vel_y = IntVar()
        self.show_vel_z = IntVar()

        self.show_pos_x_input = Checkbutton(self, text="Show X (blue)", variable=self.show_pos_x)
        self.show_pos_y_input = Checkbutton(self, text="Show Y (orange)", variable=self.show_pos_y)
        self.show_pos_z_input = Checkbutton(self, text="Show Z (green)", variable=self.show_pos_z)
        self.show_vel_x_input = Checkbutton(self, text="Show Vx (red)", variable=self.show_vel_x)
        self.show_vel_y_input = Checkbutton(self, text="Show Vy (purple)", variable=self.show_vel_y)
        self.show_vel_z_input = Checkbutton(self, text="Show Vz (brown)", variable=self.show_vel_z)

        self.show_pos_x.trace('w', lambda *args: self.redraw())
        self.show_pos_y.trace('w', lambda *args: self.redraw())
        self.show_pos_z.trace('w', lambda *args: self.redraw())
        self.show_vel_x.trace('w', lambda *args: self.redraw())
        self.show_vel_y.trace('w', lambda *args: self.redraw())
        self.show_vel_z.trace('w', lambda *args: self.redraw())

        self.show_pos_x_input.pack(anchor=W)
        self.show_pos_y_input.pack(anchor=W)
        self.show_pos_z_input.pack(anchor=W)
        self.show_vel_x_input.pack(anchor=W)
        self.show_vel_y_input.pack(anchor=W)
        self.show_vel_z_input.pack(anchor=W)

        self._on_focus()

    def on_focus(self):
        self._on_focus()

    def _on_focus(self):
        self.line_x = self.axis.plot([], [], label='X')[0]
        self.line_y = self.axis.plot([], [], label='Y')[0]
        self.line_z = self.axis.plot([], [], label='Z')[0]
        self.line_vel_x = self.axis.plot([], [], label='VEL X')[0]
        self.line_vel_y = self.axis.plot([], [], label='VEL Y')[0]
        self.line_vel_z = self.axis.plot([], [], label='VEL Z')[0]
        self.redraw()

    def redraw(self):
        X, Y, Z, T = self.spiral.calculate_trajectory(time_step=0.01)

        if self.show_pos_x.get() == 1:
            self.line_x.set_xdata(T)
            self.line_x.set_ydata(X)
        else:
            self.line_x.set_xdata([])
            self.line_x.set_ydata([])

        if self.show_pos_y.get() == 1:
            self.line_y.set_xdata(T)
            self.line_y.set_ydata(Y)
        else:
            self.line_y.set_xdata([])
            self.line_y.set_ydata([])

        if self.show_pos_z.get() == 1:
            self.line_z.set_xdata(T)
            self.line_z.set_ydata(Z)
        else:
            self.line_z.set_xdata([])
            self.line_z.set_ydata([])

        if self.show_vel_x.get() == 1:
            vals = [self.spiral.vel_x(t) for t in T]
            self.line_vel_x.set_xdata(T)
            self.line_vel_x.set_ydata(vals)
        else:
            self.line_vel_x.set_xdata([])
            self.line_vel_x.set_ydata([])

        if self.show_vel_y.get() == 1:
            vals = [self.spiral.vel_y(t) for t in T]
            self.line_vel_y.set_xdata(T)
            self.line_vel_y.set_ydata(vals)
        else:
            self.line_vel_y.set_xdata([])
            self.line_vel_y.set_ydata([])

        if self.show_vel_z.get() == 1:
            vals = [self.spiral.vel_z(t) for t in T]
            self.line_vel_z.set_xdata(T)
            self.line_vel_z.set_ydata(vals)
        else:
            self.line_vel_z.set_xdata([])
            self.line_vel_z.set_ydata([])
        if self.parent.lock_axis.get() == 0:
            self.axis.relim()
            self.axis.autoscale_view()
        self.parent.canvas.draw()
