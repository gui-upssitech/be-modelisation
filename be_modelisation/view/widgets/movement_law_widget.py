from tkinter import *
import numpy as np

from ..tkfigure import TKFigure
from be_modelisation.model import Law

class MovementLawWidget:

    def __init__(self, t, s):
        self.t = t
        self.s = s

    def draw(self, parent):
        # Create widget root
        root = Frame(parent)

        # Draw 3 figures
        self.draw_three_figs(root)

        # Add widget to parent
        root.pack(fill=BOTH, expand=True)
        parent.add(root, text="Loi de mouvement")

        self.__parent = parent
        self.__root = root

    def redraw(self):
        self.__root.destroy()        
        self.draw(self.__parent)

    def draw_three_figs(self, parent):
        fig = TKFigure.new_fig()
        fig.set_constrained_layout(True)

        plot_dist = fig.add_subplot(311)
        plot_dist.set_title("Distance (m) dans le temps (s)")
        plot_dist.plot(self.t, self.s.dist)

        plot_speed = fig.add_subplot(312)
        plot_speed.set_title("Vitesse (m.s-1) dans le temps (s)")
        plot_speed.plot(self.t, self.s.speed)

        plot_acc = fig.add_subplot(313)
        plot_acc.set_title("Acceleration (m.s-2) dans le temps (s)")
        plot_acc.plot(self.t, self.s.acc)

        TKFigure.add_to_frame(fig, parent, padding=10)

