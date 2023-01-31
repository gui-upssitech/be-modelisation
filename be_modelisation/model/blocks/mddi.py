from .. import Parameters, Point

import numpy as np
from numpy import sin, cos

class MDDI:

    def __init__(self, q, parameters):
        self.q = q
        self.__params = parameters

    def jacob(self):
        p = self.__params
        l1, l2, l3, l4, l5 = p.l(1), p.l(2), p.l(3), p.l(4), p.l(5)

        s1 = sin(self.q[0])
        c1 = cos(self.q[0])

        s4 = sin(self.q[3])
        c4 = cos(self.q[3])

        a21 = s1*(l2 + l3 + l4 + l5)
        a22 = s1*(l2 - 1) - 2*(l3 + l4 + l5)
        a24 = s1 + 2*(l3 + l4) + l2*s1 + l5*(c1 + 2*s4 - s1 + 2*c4)

        a31 = -l1 - c1*(l2 + l3 +l4 + l5)
        a32 = -l1 - c1*(l2 - 1) + 2*(l3+l4+l5)
        a34 = -l1 - c1*(l2 -1) + 2*(l3 - l4) - l5*(c1 + 2*c4 - s1 + 2*s4)

        return np.matrix(
            [1  , 1  , 0, 1  ],
            [a21, a22, 0, a24],
            [a31, a32, 0, a34],
            [0  , 0  , 1, 0  ]
        )
    
    def jacob_inv(self):
        return np.linalg.inv(self.jacob())

    def compute_mdd(self, qd):
        return self.jacob_inv() * np.matrix(qd).T

    def compute_mdi(self, point):
        return self