from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

class TKFigure:

    @staticmethod
    def new_fig() -> Figure:
        return Figure(figsize = (5, 5), dpi = 100)
    
    @staticmethod
    def add_to_frame(fig: Figure, frame: Frame, padding: int = 0):
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True, padx=padding, pady=padding)