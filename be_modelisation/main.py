from view import WindowManager
from model import Robot, Point

def main():
    # Create robot
    robot = Robot()
    robot.set_param("A", Point(4, 2, 3))
    robot.set_param("B", Point(1, 2, 3))

    # Create window manager
    window_manager = WindowManager(robot)
    window_manager.start()


if __name__ == "__main__":
    main()