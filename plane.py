class Plane:

    def __init__(self, a=1, b=1, c=0):
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self.a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    @property
    def c(self):
        return

    @c.setter
    def c(self, value):
        self._c = value

    def get_coords(self, x_min=-10, x_max=10, z_min=-10, z_max=10):
        x = [x_min, x_min, x_max, x_max]
        z = [z_min, z_max, z_min, z_max]
        y = []
        for i in range(len(x)):
            y.append(self._a * x[i] + self._b * z[i] + self._c)
        return x, y, z
