from math import cos, sin, sqrt, atan2
from ..point import Point
from ..parameters import Parameters

class MGI:

    def __init__(self, parameters: Parameters):
        self.__parameters = parameters

    def compute(self, dest: Point, theta: float) -> list[list[float]]:
        # Variable setup
        p = self.__parameters
        l1, l2, l3, l4, l5 = p.l(1), p.l(2), p.l(3), p.l(4), p.l(5)
        h1, h2 = p.h(1), p.h(2)

        l34 = l3 + l4

        # angle calculation functions

        def angles_q2(sin_q2_sign: int):
            cos_q2 = ((dest.x - l5 * cos(theta) - l1)** 2 + (dest.y - l5 * sin(theta))**2 - l34**2) / (2 * l2 * l34)
            sin_q2 = sin_q2_sign * sqrt(abs(1 - cos_q2**2))

            return cos_q2, sin_q2

        def angles_q1(cos_q2, sin_q2):
            denom = (l2 + l34 * cos_q2)**2 + (l34 * sin_q2)**2
            nom_py = dest.y - l5 * sin(theta)
            nom_px = dest.x - l5 * cos(theta) - l1

            def cos_sin_calc(p1, p2):
                return ((l2 + l34 * cos_q2 * p1) - (l34 * sin_q2 * p2)) / denom
            
            sin_q1 = cos_sin_calc(nom_py, nom_px)
            cos_q1 = cos_sin_calc(nom_px, nom_py)

            return cos_q1, sin_q1

        def compute_inner(sin_q2_sign: int) -> list[float]:
            # calculate cosine and sine values
            cos_q2, sin_q2 = angles_q2(sin_q2_sign)
            cos_q1, sin_q1 = angles_q1(cos_q2, sin_q2)


            q1 = atan2(sin_q1, cos_q1)
            q2 = atan2(sin_q2, cos_q2)            
            q3 = dest.z - (h1 + h2)
            q4 = theta - q1 - q2

            return [q1, q2, q3, q4]

        
        return [compute_inner(1), compute_inner(-1)]
