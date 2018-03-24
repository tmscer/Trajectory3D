import numpy as np
import math


class Spiral:

    def __init__(self, radius, omega, plane, x0=0, y0=0, z0=0, phi0=0, g=9.81):
        self._last_values = None
        self._last_calc = None
        self._period = 2 * np.pi / omega
        self._frequency = 1 / self._period
        self._velocity = omega * radius
        self._acceleration = omega ** 2 * radius
        self._radius = radius
        self._omega = omega
        self._x0 = x0
        self._y0 = y0
        self._z0 = z0
        self._phi0 = phi0
        self._g = g
        self._plane = plane
        self._locked_var = 'radius'  # other options: omega (meaning period and frequency too), velocity, acceleration

    @property
    def locked_var(self):
        return self._locked_var

    @locked_var.setter
    def locked_var(self, value):
        self._locked_var = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if self.locked_var == 'radius':
            return
        self._radius = value
        if self.locked_var == 'omega':
            self._velocity = self._omega * self._radius
            self._acceleration = self._velocity ** 2 / self._radius
        elif self.locked_var == 'velocity':
            self._omega = self._velocity / self._radius
            self._period = 2 * np.pi / self._omega
            self._frequency = 1 / self._period
            self._acceleration = self._velocity ** 2 / self._radius
        elif self.locked_var == 'acceleration':
            self._velocity = math.sqrt(self._acceleration * self._radius)
            self._omega = self._velocity / self._radius
            self._period = 2 * np.pi / self._omega
            self._frequency = 1 / self._period

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if self.locked_var == 'velocity':
            return
        self._velocity = value
        if self.locked_var == 'omega':
            self._radius = self._velocity / self._omega
            self._acceleration = self._velocity ** 2 / self._radius
        elif self.locked_var == 'radius':
            self._omega = self._velocity / self._radius
            self._period = 2 * np.pi / self._omega
            self._frequency = 1 / self._period
            self._acceleration = self._velocity ** 2 / self._radius
        elif self.locked_var == 'acceleration':
            self._radius = self._velocity ** 2 / self._acceleration
            self._omega = self._velocity / self._radius
            self._period = 2 * np.pi / self._omega
            self._frequency = 1 / self._period

    @property
    def acceleration(self):
        return self._acceleration

    @acceleration.setter
    def acceleration(self, value):
        if self.locked_var == 'acceleration':
            return
        self._acceleration = value
        if self.locked_var == 'omega':
            self._radius = self._acceleration / (self._omega ** 2)
            self._velocity = self._omega * self._radius
        elif self.locked_var == 'radius':
            self._velocity = math.sqrt(self._acceleration * self._radius)
            self._omega = self._velocity / self._radius
            self._period = 2 * np.pi / self._omega
            self._frequency = 1 / self._period
        elif self.locked_var == 'velocity':
            self._radius = self._velocity ** 2 / self._acceleration
            self._omega = self._velocity / self._radius
            self._period = 2 * np.pi / self._omega
            self._frequency = 1 / self._period

    @property
    def omega(self):
        return self._omega

    @omega.setter
    def omega(self, value):
        if self.locked_var == 'omega':
            return
        self._omega = value
        self._period = 2 * np.pi / self._omega
        self._frequency = 1 / self._period
        if self.locked_var == 'radius':
            self._velocity = self._omega * self._radius
            self._acceleration = self._velocity ** 2 / self._radius
        elif self.locked_var == 'velocity':
            self._radius = self._velocity / self._omega
            self._acceleration = self._velocity ** 2 / self._radius
        elif self.locked_var == 'acceleration':
            self._radius = self._omega ** 2 * self._acceleration
            self._velocity = self._omega * self._radius

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value):
        if self.locked_var == 'omega':
            return
        self._frequency = value
        self._omega = 2 * np.pi * self._frequency
        self._period = 2 * np.pi / self._omega
        if self.locked_var == 'radius':
            self._velocity = self._omega * self._radius
            self._acceleration = self._velocity ** 2 / self._radius
        elif self.locked_var == 'velocity':
            self._radius = self._velocity / self._omega
            self._acceleration = self._velocity ** 2 / self._radius
        elif self.locked_var == 'acceleration':
            self._radius = self._omega ** 2 * self._acceleration
            self._velocity = self._omega * self._radius

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        if self.locked_var == 'omega':
            return
        self._period = value
        self._omega = 2 * np.pi / self._period
        self._frequency = 1 / self._period
        if self.locked_var == 'radius':
            self._velocity = self._omega * self._radius
            self._acceleration = self._velocity ** 2 / self._radius
        elif self.locked_var == 'velocity':
            self._radius = self._velocity / self._omega
            self._acceleration = self._velocity ** 2 / self._radius
        elif self.locked_var == 'acceleration':
            self._radius = self._omega ** 2 * self._acceleration
            self._velocity = self._omega * self._radius

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
    def phi0(self):
        return self._phi0

    @phi0.setter
    def phi0(self, value):
        self._phi0 = value

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        self._g = value

    @property
    def plane(self):
        return self._plane

    @plane.setter
    def plane(self, value):
        self._plane = value

    def intersection_proximity(self, t):
        return self._plane.y_xz(self.x(t), self.z(t)) - self.y(t)

    def find_plane_intersection(self):
        t_approx = math.sqrt(2 * self._g * (self._y0 - self._plane.y_xz(self._x0, self._z0))) / self._g
        y_deviation = self.intersection_proximity(t_approx)
        tolerance = 0.1
        if y_deviation < -tolerance:
            while y_deviation < -tolerance:
                t_approx += 0.0001
                y_deviation = self.intersection_proximity(t_approx)
        elif y_deviation > tolerance:
            while y_deviation > tolerance:
                t_approx -= 0.0001
                y_deviation = self.intersection_proximity(t_approx)
        return t_approx

    def find_first_plane_intersection(self, t_values):
        for i in range(len(t_values)):
            if abs(self.intersection_proximity(t_values[i])) < 0.01:
                return t_values[:i]

    # Derivations
    def vel_x(self, t):
        return -1 * self._omega * self._radius * np.sin(self._omega * t + self._phi0)

    def vel_y(self, t):
        return -1 * self._g * t

    def vel_z(self, t):
        return self.omega * self._radius * np.cos(self._omega * t + self._phi0)

    def x(self, t):
        return self._radius * np.cos(self._omega * t + self._phi0) + self._x0

    def y(self, t):
        return self._y0 - 1 / 2 * self._g * t ** 2

    def z(self, t):
        return self._radius * np.sin(self._omega * t + self._phi0) + self._z0

    def calculate_trajectory(self, time_step=1 / 50):
        values = [self._x0, self._y0, self._z0, self._g, self._plane.a, self._plane.b, self._plane.c,
                  self._phi0, self._omega, self._velocity, self._acceleration]
        if self._last_values == values:
            return self._last_calc
        t_max = self.find_plane_intersection()
        t_values = np.append(np.arange(0, t_max, time_step), t_max)
        #t_values = self.find_first_plane_intersection(t_values)
        x_coords = self.x(t_values)
        y_coords = self.y(t_values)
        z_coords = self.z(t_values)
        self._last_calc = x_coords, y_coords, z_coords, t_values
        return self._last_calc
