import math

class Plane:

    def __init__(self, a=None, b=None, c=0, alpha=None, beta=None):
        self._a = a
        self._b = b
        self._c = c
        self._alpha = alpha
        self._beta = beta
        if a is not None and b is not None:
            self._set_using_ab()
        elif alpha is not None and beta is not None:
            self._set_using_alpha_beta()

    def _set_using_ab(self):
        self._alpha = math.atan(self._a)
        self._beta = math.atan(self._b)

    def _set_using_alpha_beta(self):
        self._a = math.tan(self._alpha)
        self._b = math.tan(self._beta)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
        self._set_using_ab()

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value
        self._set_using_ab()

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
        self._set_using_alpha_beta()

    @property
    def beta(self):
        return self._beta

    @beta.setter
    def beta(self, value):
        self._beta = value
        self._set_using_alpha_beta()

    def get_coords(self, x_min=-10, x_max=10, z_min=-10, z_max=10):
        x = [x_min, x_min, x_max, x_max]
        z = [z_min, z_max, z_min, z_max]
        y = []
        for i in range(len(x)):
            y.append(self._a * x[i] + self._b * z[i] + self._c)
        return x, y, z
