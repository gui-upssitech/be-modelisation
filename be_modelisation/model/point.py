import numpy as np
from typing_extensions import Self

class Point:

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    @staticmethod
    def from_column_vec(vec):
        return Point(vec[0, 0], vec[1, 0], vec[2, 0])

    def to_column_vec(self):
        return np.matrix([self.x, self.y, self.z]).T

    def dist(self, a):
        return np.sqrt((self.x - a.x)**2 + (self.y - a.y)**2 + (self.z - a.z)**2)

    def plot(self, ax, color=""):
        ax.scatter3D(self.x, self.y, self.z, c=color)

    def __repr__(self):
        return "{" + f"x: {self.x}, y: {self.y}, z: {self.z}" + "}"

    def __str__(self):
        return self.__repr__()

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z