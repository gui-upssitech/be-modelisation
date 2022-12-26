from tkinter import *
from tkinter import ttk

from .tkfigure import TKFigure
from .widgets import *

from be_modelisation.model import Robot

class WindowManager:

    def __init__(self, robot: Robot):
        self.__create_window()

        self.settings_widget = SettingsWidget(self, robot)
        self.movement_law_widget = MovementLawWidget(robot)
        self.trajectory_widget = TrajectoryWidget(robot)

        self.robot_widget = RobotWidget(robot)

        self.__setup_frames()

    # =================
    # Public methods
    # =================

    def start(self):
        self.window.mainloop()

    def redraw(self):
        self.movement_law_widget.redraw()
        self.trajectory_widget.redraw()
        self.robot_widget.redraw()

    # =================
    # Private methods
    # =================

    def __create_window(self) -> tuple[Tk, int, int]:
        window = Tk()
        window.title('BE Modélisation')
        window.geometry("1280x800")
        window.config(bg="#DDD")
        window.resizable(False, False)

        self.window = window

    def __setup_frames(self):
        left_frame = Frame(self.window, bg="#DDD")
        right_frame = Frame(self.window, bg="#FFF")

        # Setup left frame
        notebook = ttk.Notebook(left_frame)

        self.settings_widget.draw(notebook)
        self.movement_law_widget.draw(notebook)
        self.trajectory_widget.draw(notebook)
        
        notebook.pack(fill=BOTH, expand=True)

        # Setup right frame
        self.robot_widget.draw(right_frame)

        # Pack frames
        left_frame.pack(side=LEFT, fill=BOTH, expand=True)
        right_frame.pack(side=RIGHT, fill=BOTH, expand=True)
