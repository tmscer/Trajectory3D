import math


class Plane:

    @classmethod
    def init_using_coefficients(cls, a=0, b=0, c=0, *args, **kwargs):
        instance = cls(*args, **kwargs)
        instance.a = a
        instance.b = b
        instance.c = c
        return instance

    @classmethod
    def init_using_angles(cls, alpha=0, beta=0, c=0, *args, **kwargs):
        instance = cls(*args, **kwargs)
        instance.alpha = alpha
        instance.beta = beta
        return instance

    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def __repr__(self):
        return "Plane(a={}, b={}, c={}, alpha={}, beta={}".format(self.a, self.b, self.c, self.alpha, self.beta)

    #def __str__(self):
    #    return ""

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
        self._alpha = math.atan(self.a)

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value
        self._beta = math.atan(self.b)

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = value

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        self._alpha = value
        self._a = math.tan(self.alpha)

    @property
    def beta(self):
        return self._beta

    @beta.setter
    def beta(self, value):
        self._beta = value
        self._b = math.tan(self.beta)

    def y_pos(self, x, z):
        return self._a * x + self._b * z + self._c

    def get_coords(self, x_min=-10, x_max=10, z_min=-10, z_max=10):
        x = [x_min, x_min, x_max, x_max]
        z = [z_min, z_max, z_min, z_max]
        y = [self.y_pos(x[i], z[i]) for i in range(len(x))]
        return x, y, z
