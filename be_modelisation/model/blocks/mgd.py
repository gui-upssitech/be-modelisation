from ..point import Point
from ..parameters import Parameters

import numpy as np
from numpy import cos, sin

class MGD:

    def __init__(self, parameters) -> None:
        self.__parameters = parameters
        
    def apply_transform(self, matrix, origin = Point(0, 0, 0)):
        r = matrix[0:3, 0:3]
        p = matrix[0:3, 3]

        res = r * origin.to_column_vec() + p
        return Point.from_column_vec(res)

    def t01(self, q):
        p = self.__parameters
        return np.matrix([
            [cos(q), -sin(q), 0, p.l(1)], 
            [sin(q), cos(q),  0, 0     ], 
            [0,      0,       1, p.h(1)], 
            [0,      0,       0, 1     ]
        ])

    def t12(self, q):
        p = self.__parameters
        return np.matrix([
            [cos(q), -sin(q), 0, p.l(2)], 
            [sin(q), cos(q),  0, 0     ], 
            [0,      0,       1, 0     ], 
            [0,      0,       0, 1     ]
        ])

    def t23(self, q):
        p = self.__parameters
        return np.matrix([
            [1, 0, 0, p.l(3)], 
            [0, 1, 0, 0     ], 
            [0, 0, 1, q     ], 
            [0, 0, 0, 1     ]
        ])

    def t34(self, q):
        p = self.__parameters
        return np.matrix([
            [cos(q), -sin(q), 0, p.l(4)], 
            [sin(q), cos(q),  0, 0     ], 
            [0,      0,       1, p.h(2)], 
            [0,      0,       0, 1     ]
        ])

    def t45(self):
        p = self.__parameters
        return np.matrix([
            [1, 0, 0, p.l(5)], 
            [0, 1, 0, 0     ], 
            [0, 0, 1, 0     ], 
            [0, 0, 0, 1     ]
        ])

    def t05(self, q):
        return self.t01(q[0]) * self.t12(q[1]) * self.t23(q[2]) * self.t34(q[3]) * self.t45()


    def compute_joints(self, q, origin = Point(0, 0, 0)):
        t01 = self.t01(q[0])
        t12 = self.t12(q[1])
        t23 = self.t23(q[2])
        t34 = self.t34(q[3])
        t45 = self.t45()

        t02 = t01 * t12
        t03 = t02 * t23
        t04 = t03 * t34
        t05 = t04 * t45

        return [
            self.apply_transform(t01, origin),
            self.apply_transform(t02, origin),
            self.apply_transform(t03, origin),
            self.apply_transform(t04, origin),
            self.apply_transform(t05, origin)
        ]