from .point import Point

import numpy as np
from numpy import cos, sin

class MGD:

    def __init__(self, robot):
        self.__robot = robot
        
    def apply_transform(self, matrix: np.ndarray, origin: Point = Point(0, 0, 0)) -> Point:
        r = matrix[0:3, 0:3]
        p = matrix[0:3, 3]

        res = r * origin.to_column_vec() + p
        return Point.from_column_vec(res)

    def t01(self, q) -> np.ndarray:
        r = self.__robot
        return np.matrix([
            [cos(q), -sin(q), 0, r.l(1)], 
            [sin(q), cos(q),  0, 0     ], 
            [0,      0,       1, r.h(1)], 
            [0,      0,       0, 1     ]
        ])

    def t12(self, q) -> np.ndarray:
        r = self.__robot
        return np.matrix([
            [cos(q), -sin(q), 0, r.l(2)], 
            [sin(q), cos(q),  0, 0     ], 
            [0,      0,       1, 0     ], 
            [0,      0,       0, 1     ]
        ])

    def t23(self, q) -> np.ndarray:
        r = self.__robot
        return np.matrix([
            [1, 0, 0, r.l(3)], 
            [0, 1, 0, 0     ], 
            [0, 0, 1, q     ], 
            [0, 0, 0, 1     ]
        ])

    def t34(self, q) -> np.ndarray:
        r = self.__robot
        return np.matrix([
            [cos(q), -sin(q), 0, r.l(4)], 
            [sin(q), cos(q),  0, 0     ], 
            [0,      0,       1, r.h(2)], 
            [0,      0,       0, 1     ]
        ])

    def t45(self) -> np.ndarray:
        r = self.__robot
        return np.matrix([
            [1, 0, 0, r.l(5)], 
            [0, 1, 0, 0     ], 
            [0, 0, 1, 0     ], 
            [0, 0, 0, 1     ]
        ])

    def t05(self, q: list[float]) -> np.ndarray:
        return self.t01(q[0]) * self.t12(q[1]) * self.t23(q[2]) * self.t34(q[3]) * self.t45()