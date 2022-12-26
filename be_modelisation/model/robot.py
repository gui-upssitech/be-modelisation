from .point import Point
from .loiMouvement import LoiMouvement
from .traj import Trajectory
from .mgd import MGD
from .mgi import MGI

import matplotlib.pyplot as plt

ParamsDict = dict[str, Point | int]

class Robot:

    def __init__(self) -> None:
        self.__params: ParamsDict = {
            "A": Point(0, 0, 0),
            "B": Point(1, 1, 1),
            "V": 1,
            "θ": 1
        }

        self.__measurments = {
            "l": [1, 1, 1, 1, 1],
            "h": [1, 1]
        }

        self.__position = self.param("A")
        self.__q_lists = [0, 0, 0, 0]
        self.__joints: list[Point] = []

        self.__positions: dict[list[float], Point] = {}

        self.__create_movement_law()
        self.__trajectory = Trajectory(self)
        self.__mgd = MGD(self)
        self.__mgi = MGI(self)

    # Parameters

    def get_params(self) -> ParamsDict:
        return self.__params

    def param(self, key: str) -> Point | int:
        return self.__params[key]

    def set_param(self, key: str, value: Point | int):
        self.__params[key] = value
        self.__position = self.param("A")
        self.__update()

    def set_params(self, params: ParamsDict):
        self.__params = params
        self.__update()

    def set_position(self, position: Point):
        self.__position = position
        self.__update()

    def __update(self):
        print("#####")
        print("Updating robot")
        self.__create_movement_law()
        self.trajectory.update_params()
        self.__q_lists = self.mgi.compute(self.__position, self.param("θ"))
        self.__update_joints(0)

        print("Position voulue:", self.__position)
        print("Position actuelle:", self.get_joints()[-1])
        print("Erreur en position:", self.get_error())
        print("#####\n")

    # Measurements

    def get_lengths(self) -> list[float]:
        return self.__measurments["l"]

    def l(self, i: int) -> float:
        return self.__measurments["l"][i-1]
    
    def get_heights(self) -> list[float]:
        return self.__measurments["h"]

    def h(self, i: int) -> float:
        return self.__measurments["h"][i-1]

    # Movement

    def __create_movement_law(self):
        self.__movement_law = LoiMouvement(self.param("V"), self.param("A").dist(self.param("B")))

    @property
    def movement_law(self) -> LoiMouvement:
        return self.__movement_law

    # Trajectory

    @property
    def trajectory(self) -> Trajectory:
        return self.__trajectory

    # Joints

    def get_joints(self) -> list[Point]:
        return self.__joints

    def __update_joints(self, q_variant: int) -> list[Point]:
        q = self.__q_lists[q_variant]
        t01, t12, t23, t34, t45 = self.mgd.t01(q[0]), self.mgd.t12(q[1]), self.mgd.t23(q[2]), self.mgd.t34(q[3]), self.mgd.t45()

        matrices = [
            t01,
            t01 * t12,
            t01 * t12 * t23,
            t01 * t12 * t23 * t34,
            t01 * t12 * t23 * t34 * t45
        ]

        self.__joints = [ self.mgd.apply_transform(m) for m in matrices ]

    # MGD
    @property
    def mgd(self) -> MGD:
        return self.__mgd

    @property
    def mgi(self) -> MGI:
        return self.__mgi

    # Error
    def get_error(self) -> float:
        desired_point = self.__position
        current_point = self.get_joints()[-1]

        err_point = Point(
            round(desired_point.x - current_point.x, 3), 
            round(desired_point.y - current_point.y, 3), 
            round(desired_point.z - current_point.z, 3)
        )

        return err_point # desired_point.dist(current_point)
