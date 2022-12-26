# from . import Robot
# from .loiMouvement import LoiMouvement

import numpy as np

Vec3D = (float, float, float)

class Trajectory:

    def __init__(self, robot) -> None:
        self.__robot = robot
        self.update_params()

    def update_params(self):
        self.__law = self.__robot.movement_law
        self.__a = self.__robot.param("A")
        self.__b = self.__robot.param("B")

    def __k(self, a: float, b: float) -> float:
        return (b-a) / self.__a.dist(self.__b)

    def get_distance(self, t: float) -> Vec3D:
        a = self.__a
        b = self.__b

        def dist(a: float, b: float) -> float:
            return self.__k(a, b) * self.__law.get_distance(t) + a

        res = (dist(a.x, b.x), dist(a.y, b.y), dist(a.z, b.z))
        return res

    def get_speed(self, t: float) -> Vec3D:
        a = self.__a
        b = self.__b

        def speed(a: float, b: float) -> float:
            return abs(self.__k(a, b)) * self.__law.get_speed(t)

        return (speed(a.x, b.x), speed(a.y, b.y), speed(a.z, b.z))

    def get_acceleration(self, t: float) -> Vec3D:
        a = self.__a
        b = self.__b

        def accel(a: float, b: float) -> float:
            return abs(self.__k(a, b)) * self.__law.get_acceleration(t)
        
        return (accel(a.x, b.x), accel(a.y, b.y), accel(a.z, b.z))