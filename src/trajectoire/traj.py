from point import Point
import matplotlib.pyplot as plt
from src.loi_mouvement import LoiMouvement

class Trajectoire:

    def __init__(self, loi_mouvement: LoiMouvement) -> None:
        self.__loi_mouvement = loi_mouvement

    def set_points(self, a: Point, b: Point):
        self.__a = a
        self.__b = b
    
    def __k(self, a: float, b: float) -> float:
        distance = self.__a.dist(self.__b)
        return (b - a) / distance

    def get_dist(self, t: float) -> Point:
        a = self.__a
        b = self.__b

        def dist(a: float, b: float) -> float:
            return self.__k(a, b) * self.__loi_mouvement.getDistance(t) + a

        return Point(dist(a.x, b.x), dist(a.y, b.y), dist(a.z, b.z))

    def get_speed(self, t: float) -> Point:
        a = self.__a
        b = self.__b

        def speed(a: float, b: float) -> float:
            return self.__k(a, b) * self.__loi_mouvement.getSpeed(t)

        return Point(speed(a.x, b.x), speed(a.y, b.y), speed(a.z, b.z))

    def get_acc(self, t: float) -> Point:
        a = self.__a
        b = self.__b

        def speed(a: float, b: float) -> float:
            return self.__k(a, b) * self.__loi_mouvement.getAcc(t)

        return Point(speed(a.x, b.x), speed(a.y, b.y), speed(a.z, b.z))

    def afficher(self):
        plt.plot(self.__a)

if __name__ == "__main__":
    import math
    import numpy as np

    a = Point(0, 0, 0)
    b = Point(2, 4, 6)

    loi_mouvement = LoiMouvement(5, 100)
    traj = Trajectoire(loi_mouvement)
    traj.set_points(a, b)

    n_points = 50

    s: list[float] = np.linspace(0, a.dist(b), n_points).tolist()
    m = [ traj.get_dist(ss) for ss in s ]

    # Graph
    plt.figure()
    ax = plt.axes(projection="3d")

    for p in m:
        p.plot(ax, "blue")

    a.plot(ax, "red")
    b.plot(ax, "red")

    plt.show()