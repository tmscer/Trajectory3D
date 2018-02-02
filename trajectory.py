import math
import numpy as np


def trajectory_calculator(x0, y0, z0, xv, yv, zv, g, time_step=1/16):
    t = 0
    y = y0 + t * (yv - 1 / 2 * g * t)
    while 0 <= y <= 100:
        x = x0 + xv * t
        z = z0 + zv * t
        yield x, y, z
        t += time_step
        y = y0 + t * (yv - 1 / 2 * g * t)
    t = 2 * yv / g
    x = x0 + xv * t
    z = z0 + zv * t
    yield x, 0, z


class Trajectory:

    def __init__(self, xv=None, yv=None, zv=None, alpha=None, theta=None, v0=None, x0=0, y0=0, z0=0):
        if y0 < 0:
            raise ValueError("Initial height y0 cannot be negative: {}".format(y0))
        self._last_values = None
        self._last_calc = None
        self._x0 = x0
        self._y0 = y0
        self._z0 = z0
        self._xv = xv
        self._yv = yv
        self._zv = zv
        self._alpha = alpha
        self._theta = theta
        self._v0 = v0
        if xv is not None and yv is not None and zv is not None:
            self._xz = math.sqrt(self._xv ** 2 + self._zv ** 2)
            self._set_using_xyz()
            self._ok = True
        elif alpha is not None and theta is not None and v0 is not None:
            self._set_using_alpha_theta_v0()
            self._ok = True
        else:
            self._ok = False

    def _set_using_xyz(self):
        self._xz = math.sqrt(self._xv ** 2 + self._zv ** 2)
        self._theta = math.acos(self._xv / self._xz)
        self._v0 = math.sqrt(self._xv ** 2 + self._yv ** 2 + self._zv ** 2)
        self._alpha = math.acos(self._xz / self._v0)

    def _set_using_alpha_theta_v0(self):
        self._yv = self._v0 * math.sin(self._alpha)
        self._xz = self._v0 * math.cos(self._alpha)
        self._xv = self._xz * math.cos(self._theta)
        self._zv = self._xz * math.sin(self._theta)

    @property
    def xv(self):
        return self._xv

    @xv.setter
    def xv(self, value):
        self._xv = value
        self._set_using_xyz()

    @property
    def yv(self):
        return self._yv

    @yv.setter
    def yv(self, value):
        self._yv = value
        self._set_using_xyz()

    @property
    def zv(self):
        return self._zv

    @zv.setter
    def zv(self, value):
        self._zv = value
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
        self.v0 = value
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
        self_y0 = value

    @property
    def z0(self):
        return self._z0

    @z0.setter
    def z0(self, value):
        self._z0 = value

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        if other is None:
            return False
        else:
            return self.__dict__ == other.__dict__

    def calculate_trajectory(self, g=9.81, time_step=1/16):
        values = [self._xv, self._yv, self._zv, self._x0, self._y0, self._z0]
        if self._last_values is not None:
            if self._last_values == values:
                return self._last_calc
        x_values = []
        y_values = []
        z_values = []
        for x, y, z in trajectory_calculator(self._x0, self._y0, self._z0, self._xv, self._yv, self._zv, g, time_step):
            x_values.append(x)
            y_values.append(y)
            z_values.append(z)
        self._last_values = values
        self._last_calc = x_values, y_values, z_values
        return self._last_calc
