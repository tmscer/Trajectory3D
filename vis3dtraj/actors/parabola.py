import math
import numpy as np


class Parabola:

    @classmethod
    def init_using_vels_xyz(cls):
        pass

    @classmethod
    def init_using_angles_vel0(cls):
        pass

    def __init__(self, plane, vel_x=None, vel_y=None, vel_z=None, alpha=None, theta=None, v0=None, x0=0, y0=0, z0=0,
                 g=9.81):
        self._plane = plane
        self._last_values = None
        self.last_calc = None
        self._g = g
        self._x0 = x0
        self._y0 = y0
        self._z0 = z0
        self._vel_x = vel_x
        self._vel_y = vel_y
        self._vel_z = vel_z
        self._alpha = alpha
        self._theta = theta
        self._v0 = v0
        if vel_x is not None and vel_y is not None and vel_z is not None:
            self._xz = math.sqrt(self.vel_x ** 2 + self.vel_z ** 2)
            self._set_using_xyz()
            self._ok = True
        elif alpha is not None and theta is not None and v0 is not None:
            self._set_using_alpha_theta_v0()
            self._ok = True
        else:
            self._ok = False

    def __repr__(self):
        return "Parabola(vel_x={}, vel_y={}, vel_z={}, alpha={}, theta={}, v0={}, x0={}, y0={}, z0={}, g={})"\
            .format(self.vel_x, self.vel_y, self.vel_z,
                    self.alpha, self.theta, self.v0,
                    self.x0, self.y0, self.z0,
                    self.g)

    #def __str__(self):
    #    return ""

    def _set_using_xyz(self):
        self._xz = math.sqrt(self.vel_x ** 2 + self.vel_z ** 2)
        self._theta = math.acos(self.vel_x / self._xz)
        self._v0 = math.sqrt(self.vel_x ** 2 + self.vel_y ** 2 + self.vel_z ** 2)
        self._alpha = math.acos(self._xz / self.v0)

    def _set_using_alpha_theta_v0(self):
        self._vel_y = self.v0 * math.sin(self.alpha)
        self._xz = self.v0 * math.cos(self.alpha)
        self._vel_x = self._xz * math.cos(self.theta)
        self._vel_z = self._xz * math.sin(self.theta)

    @property
    def vel_x(self):
        return self._vel_x

    @vel_x.setter
    def vel_x(self, value):
        self._vel_x = value
        self._set_using_xyz()

    @property
    def vel_y(self):
        return self._vel_y

    @vel_y.setter
    def vel_y(self, value):
        self._vel_y = value
        self._set_using_xyz()

    @property
    def vel_z(self):
        return self._vel_z

    @vel_z.setter
    def vel_z(self, value):
        self._vel_z = value
        self._set_using_xyz()

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        self._alpha = value
        self._set_using_alpha_theta_v0()

    @property
    def theta(self):
        return self._theta

    @theta.setter
    def theta(self, value):
        self._theta = value
        self._set_using_alpha_theta_v0()

    @property
    def v0(self):
        return self._v0

    @v0.setter
    def v0(self, value):
        self._v0 = value
        self._set_using_alpha_theta_v0()

    @property
    def x0(self):
        return self._x0

    @x0.setter
    def x0(self, value):
        self._x0 = value

    @property
    def y0(self):
        return self._y0

    @y0.setter
    def y0(self, value):
        self._y0 = value

    @property
    def z0(self):
        return self._z0

    @z0.setter
    def z0(self, value):
        self._z0 = value

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        if value == 0:
            raise ValueError("Gravitational acceleration cannot be 0")
        self._g = value

    @property
    def plane(self):
        return self._plane

    @plane.setter
    def plane(self, value):
        self._plane = value

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        if other is None:
            return False
        else:
            return self.__dict__ == other.__dict__

    def x_pos(self, t):
        return self.x0 + self.vel_x * t

    def y_pos(self, t):
        return self.y0 + self.vel_y * t - 0.5 * self.g * t ** 2

    def z_pos(self, t):
        return self.z0 + self.vel_z * t

    def vy(self, t):
        return self.vel_y - self.g * t

    def calculate_trajectory(self, time_step=1 / 10):
        values = [self.vel_x, self.vel_y, self.vel_z, self.x0, self.y0, self.z0, self.plane.a, self.plane.b,
                  self.plane.c, self.g, time_step]
        if self._last_values == values:
            return self.last_calc
        td = self.time_at_d()
        t_values = np.append(np.arange(0, td, time_step), td)
        x_values = t_values * self.vel_x + self.x0
        y_values = t_values * (self.vel_y - 0.5 * self.g * t_values) + self.y0
        z_values = t_values * self.vel_z + self.z0
        self._last_values = values
        self.last_calc = x_values, y_values, z_values, t_values
        return self.last_calc

    def time_at_b(self):
        return self.vel_y / self.g

    def time_at_c(self):
        return 2 * self.time_at_b()

    def time_at_d(self):
        pb = self.plane.a * self.vel_x + self.plane.b * self.vel_z - self.vel_y
        dis = pb ** 2 - 2 * self.g * (self.plane.a * self.x0 + self.plane.b + self.plane.c - self.y0)
        if dis < 0:
            return None
        sqr = math.sqrt(dis)
        t1 = (- pb + sqr) / self.g
        t2 = (- pb - sqr) / self.g
        return t1 if t2 < 0 else t2

    def a_pos(self):
        return self.x0, self.y0, self.z0

    def b_pos(self):
        tb = self.time_at_b()
        return self.x_pos(tb), \
               self.y_pos(tb), \
               self.z_pos(tb)

    def c_pos(self):
        tc = self.time_at_c()
        return self.x_pos(tc), \
               self.y0, \
               self.z_pos(tc)

    def d_pos(self):
        td = self.time_at_d()
        if td is None:
            return None, None, None
        return self.x_pos(td), \
               self.y_pos(td), \
               self.z_pos(td)
