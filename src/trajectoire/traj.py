from point import Point
import matplotlib.pyplot as plt

class Trajectoire:

    def __init__(self, a: Point, b: Point) -> None:
        self._a = a
        self._b = b
    
    def m(self, s: float) -> Point:
        a = self._a
        b = self._b
        distance = a.dist(b)

        def dist(a: float, b: float) -> float:
            return (b - a) / distance * s + a

        return Point(dist(a.x, b.x), dist(a.y, b.y), dist(a.z, b.z))

    def m_speed(self, s: float) -> Point:
        a = self._a
        b = self._b
        dist = a.dist(b)

        def speed(a: float, b: float) -> float:
            return (b - a) / dist

        return Point(speed(a.x, b.x), speed(a.y, b.y), speed(a.z, b.z))

    def m_acc(self, s: float) -> Point:
        return Point(0, 0, 0)

    def afficher(self):
        plt.plot(self._a)

if __name__ == "__main__":
    import math
    import numpy as np

    a = Point(0, 0, 0)
    b = Point(2, 4, 6)

    traj = Trajectoire(a, b)
    n_points = 30

    s: list[float] = np.linspace(0, a.dist(b), n_points).tolist()
    m = [ traj.m(ss) for ss in s ]

    # Graph
    plt.figure()
    ax = plt.axes(projection="3d")

    for p in m:
        p.plot(ax, "blue")

    a.plot(ax, "red")
    b.plot(ax, "red")

    plt.show()