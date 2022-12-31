from ..point import Point

class Trajectory:

    def __init__(self, a: Point, b: Point) -> None:
        self.__a = a
        self.__b = b

    def k(self, a: float, b: float) -> float:
        return (b-a) / self.__a.dist(self.__b)

    def __apply_func(self, func) -> Point:
        a = self.__a
        b = self.__b

        return Point(func(a.x, b.x), func(a.y, b.y), func(a.z, b.z))

    def get_distance(self, t: float) -> Point:
        def dist(a: float, b: float) -> float:
            return self.k(a, b) * t + a

        return self.__apply_func(dist)

    def get_speed(self, t: float) -> Point:
        def speed(a: float, b: float) -> float:
            return abs(self.k(a, b)) * t

        return self.__apply_func(speed)

    def get_acceleration(self, t: float) -> Point:
        def accel(a: float, b: float) -> float:
            return abs(self.k(a, b)) * t
        
        return self.__apply_func(accel)