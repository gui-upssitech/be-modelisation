import numpy as np
from math import cos, sin

from .point import Point
from .loiMouvement import LoiMouvement

class Robot:

    def __init__(self, h: list[float], l: list[float]) -> None:
        self.__h = h
        self.__l = l

        self.__movement_law = LoiMouvement(0, 0)

    def trajectory(self, A: Point, B: Point, theta: float, speed: float):
        # Compute distance between points
        distance = A.dist(B)
        self.__movement_law = LoiMouvement(speed, distance)

        M = self.compute_mgd(A, [0, 0, 0, 0])

        pass

    @property
    def movement_law(self) -> LoiMouvement:
        return self.__movement_law

    def compute_mgd(self, origin: Point, q: list[float]) -> Point:
        # Compute transformation matrix
        t05 = np.matrix([
            [
                cos(q[0]+q[1]) * cos(q[3]) - sin(q[0]+q[1]) * sin(q[3]), 
                -cos(q[0]+q[1]) * sin(q[3]) - sin(q[0]+q[1]) * cos(q[3]), 
                0, 
                cos(q[0] + q[1]) * self.__l[3] + cos(q[0] + q[1]) * self.__l[2] + cos(q[0]) * self.__l[1] + self.__l[0] + self.__l[4]
            ],
            [
                sin(q[0]+q[1]) * cos(q[3]) + cos(q[0]+q[1]) * sin(q[3]),
                -sin(q[0]+q[1]) * sin(q[3]) + cos(q[0]+q[1]) * cos(q[3]),
                0,
                sin(q[0] + q[1]) * self.__l[3] + sin(q[0] + q[1]) * self.__l[2] + sin(q[0]) * self.__l[1]
            ], 
            [ 0, 0, 1, q[2] + self.__h[1] + self.__h[0] ], 
            [ 0, 0, 0, 1 ]
        ])
        
        # Compute final position
        m = t05 * origin.to_column_vec()

        # Convert to Point
        return Point.from_column_vec(m)
    
    def compute_mgi(self, T: Point):
        pass

    def compute_mdd(self, origin: Point, q: list[float]) -> Point:
        pass
