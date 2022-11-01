import math
from typing_extensions import Self

class Point:

    def __init__(self, x: float, y: float, z: float):
        self._x = x
        self._y = y
        self._z = z

    def to_list(self) -> list[float]:
        return [self.x, self.y, self.z]

    def dist(self, a: Self) -> float:
        return math.sqrt((self.x - a.x)**2 + (self.y - a.y)**2 + (self.z - a.z)**2)

    def plot(self, ax, color=""):
        ax.scatter3D(self.x, self.y, self.z, c=color)

    def __repr__(self) -> str:
        return "{" + f"x: {self.x}, y: {self.y}, z: {self.z}" + "}"

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z