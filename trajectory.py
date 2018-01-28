import math
import numpy as np


class Trajectory:

    def __init__(self, x=None, y=None, z=None, alpha=None, theta=None, v0=None, h0=0):
        self.h0 = h0
        self.x = x
        self.y = y
        self.z = z
        self.alpha = alpha
        self.theta = theta
        self.v0 = v0
        if x is not None and y is not None and z is not None:
            self.xz = math.sqrt(self.x ** 2 + self.z ** 2)
            self.set_using_xyz()
            self.ok = True
        elif alpha is not None and theta is not None and v0 is not None:
            self.set_using_alpha_theta_v0()
            self.ok = True
        else:
            self.ok = False

    def set_x(self, x):
        self.x = x
        self.set_using_xyz()

    def set_y(self, y):
        self.y = y
        self.set_using_xyz()

    def set_z(self, z):
        self.z = z
        self.set_using_xyz()

    def set_using_xyz(self):
        self.xz = math.sqrt(self.x ** 2 + self.z ** 2)
        self.theta = math.acos(self.x / self.xz)
        self.v0 = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        self.alpha = math.acos(self.xz / self.v0)

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.set_using_alpha_theta_v0()

    def set_theta(self, theta):
        self.theta = theta
        self.set_using_alpha_theta_v0()

    def set_v0(self, v0):
        self.v0 = v0
        self.set_using_alpha_theta_v0()

    def set_using_alpha_theta_v0(self):
        self.y = self.v0 * math.sin(self.alpha)
        self.xz = self.v0 * math.cos(self.alpha)
        self.x = self.xz * math.cos(self.theta)
        self.z = self.xz * math.sin(self.theta)

    def calculate_trajectory(self, toplimit = 300):
        if not self.ok:
            return None
        X = []
        Y = []
        Z = []
        t = 0
        y = self.h0 + self.y * t - 1/2 * 9.81 * t**2
        while 0 <= y <= toplimit:
            X.append(self.x * t)
            Z.append(self.z * t)
            Y.append(y)
            if y < 0.5:
                t += 0.125 / 8
            else:
                t += 0.125 / 4
            y = self.h0 + self.y * t - 1/2 * 9.81 * t**2
        return [X, Y, Z]


#one = Trajectory(x=1, y=2, z=1)
#two = Trajectory(alpha=one.alpha, theta=one.theta, v0=one.v0)
#print()