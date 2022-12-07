from tkinter import *
from tkinter import ttk

from .tkfigure import TKFigure
from .widgets import SettingsWidget, MovementLawWidget

class WindowManager:

    def __init__(self):
        self.__create_window()

        self.settings_widget = SettingsWidget()
        self.movement_law_widget = MovementLawWidget()
        self.__setup_frames()

    # =================
    # Public methods
    # =================

    def start(self):
        self.window.mainloop()

    # =================
    # Private methods
    # =================

    def __create_window(self) -> tuple[Tk, int, int]:
        window = Tk()
        window.title('BE Modélisation')
        window.geometry("1024x720")
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
        
        notebook.pack(fill=BOTH, expand=True)

        # Setup right frame
        self.right_frame_plot(right_frame)

        # Pack frames
        left_frame.pack(side=LEFT, fill=BOTH, expand=True)
        right_frame.pack(side=RIGHT, fill=BOTH, expand=True)


    def right_frame_plot(self, parent):
        # TODO: Replace with 3D widget

        fig = TKFigure.new_fig()
  
        # list of squares
        plot1 = fig.add_subplot(111)

        y = [i**2 for i in range(101)]
        plot1.plot(y)

        TKFigure.add_to_frame(fig, parent)
