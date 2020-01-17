from math import hypot, sqrt


class Vector:
    def __init__(self, x: int, y: int, z: int = None):
        self._x = x
        self._y = y
        self._z = z

    def __repr__(self):
        return "Vector(%r, %r, %r)" % (self._x, self._y, self._z) if len(self) == 3 \
            else "Vector(%r,%r)" % (self._x, self._y)

    def __add__(self, other):
        if not len(self) == len(other):
            raise IndexError("You can't add vectors of different dimensions")
        return Vector(self._x + other._x, self._y + other._y) if len(self) == 2 \
            else Vector(self._x + other._x, self._y + other._y, self._z + other._z)

    def __mul__(self, other):
        return Vector(self._x * other, self._y * other) if len(self) == 2 \
            else Vector(self._x * other, self._y * other, self._z * other)

    def __abs__(self):
        if len(self) == 3:
            raise AttributeError("3d vectors do not support this method")
        return hypot(self._x, self._y)

    def __len__(self):
        return 3 if self._z != None else 2

    def __bool__(self):
        return bool(self._x or self._y or self._z)


if __name__ == '__main__':
    v = Vector(0, 0)
    v2 = Vector(0, 1)
    v3 = Vector(0, 0, 0)
    print(abs(v))
    print(bool(v2))
