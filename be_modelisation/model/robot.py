import numpy as np
from math import cos, sin

from .point import Point
from .loiMouvement import LoiMouvement

ParamsDict = dict[str, Point | int]

class Robot:

    def __init__(self) -> None:
        self.__h = [1, 1, 1, 1, 1]
        self.__l = [1, 1, 1]

        self.__params: ParamsDict = {
            "A": Point(0, 0, 0),
            "B": Point(1, 1, 1),
            "V": 1,
            "θ": 1
        }

        self.__create_movement_law()

    # Parameters

    def get_params(self) -> ParamsDict:
        return self.__params

    def param(self, key: str) -> Point | int:
        return self.__params[key]

    def set_params(self, params: ParamsDict):
        self.__params = params
        self.__create_movement_law()

    # Movement
    def __create_movement_law(self):
        self.__movement_law = LoiMouvement(self.param("V"), self.param("A").dist(self.param("B")))

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
        c12 = cos(q[0] + q[1])
        s12 = sin(q[0] + q[1])
        
        c1 = cos(q[0])
        s1 = sin(q[0])

        c4 = cos(q[3])
        s4 = sin(q[3])

        # Compute transformation matrix
        t05 = np.matrix([
            [
                c12 * c4 - s12 * s4, 
                -c12 * s4 - s12 * c4, 
                0, 
                c12 * self.__l[3] + c12 * self.__l[2] + c1 * self.__l[1] + self.__l[0] + self.__l[4]
            ],
            [
                c12 * c4 + c12 * s4,
                -s12 * s4 + c12 * c4,
                0,
                s12 * self.__l[3] + s12 * self.__l[2] + s1 * self.__l[1]
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
