from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

class TKFigure:

    @staticmethod
    def new_fig():
        return Figure(figsize = (5, 5), dpi = 100)

    @staticmethod
    def add_to_frame(fig, frame, padding = 0):
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True, padx=padding, pady=padding)