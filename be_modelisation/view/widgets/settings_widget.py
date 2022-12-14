from tkinter import *

from be_modelisation.model import Robot, Point

class SettingsWidget:

    def __init__(self, wm, robot: Robot):

        def parse_robot_param(value: Point | int):
            var = StringVar()
            var.set(str(value) if isinstance(value, int) else f"{value.x};{value.y};{value.z}")
            return var

        self.__wm = wm
        self.__robot = robot
        self.__ui_params = { key: parse_robot_param(value) for (key, value) in self.__robot.get_params().items()}

    # =================
    # Public methods
    # =================

    def draw(self, parent):
        root = Frame(parent)

        for (key, value) in self.__ui_params.items():
            box = Frame(root)

            Label(box, text=f"{key}:").grid(row=0, column=0)
            Entry(box, textvariable=value).grid(row=0, column=1)

            box.pack(padx=10, pady=10)

        btn = Button(root, text="Modifier les paramètres", command=self.__on_click)
        btn.pack(padx=10, pady=10)

        root.pack(fill=BOTH, expand=True)
        parent.add(root, text="Paramètres")

    # =================
    # Private methods
    # =================

    def __parse_input(self, value: str):
        try:
            if ";" in value:
                return Point(*[float(i) for i in value.split(";")])
            else:
                return float(value)
        except:
            return False


    def __on_click(self):
        params = { key: self.__parse_input(value.get()) for (key, value) in self.__ui_params.items() }
        
        if False in params.values():
            print("Error: Invalid parameters")
            return

        print(params)
        self.__robot.set_params(params)
        self.__wm.redraw() 