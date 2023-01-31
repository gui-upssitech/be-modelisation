from tkinter import *
import numpy as np

from ..tkfigure import TKFigure
from be_modelisation.model import Law

class TrajectoryWidget:

    def __init__(self, t, x, y, z):
        self.t = t
        self.x = x
        self.y = y
        self.z = z

    def draw(self, parent):
        # Create widget root
        root = Frame(parent)

        # Draw 3 figures
        self.draw_three_figs(root)

        # Add widget to parent
        root.pack(fill=BOTH, expand=True)
        parent.add(root, text="Trajectoire")

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
        plot_dist.plot(self.t, self.x.dist)
        plot_dist.plot(self.t, self.y.dist)
        plot_dist.plot(self.t, self.z.dist)
        plot_dist.legend(["x", "y", "z"])

        plot_speed = fig.add_subplot(312)
        plot_speed.set_title("Vitesse (m.s-1) dans le temps (s)")
        plot_speed.plot(self.t, self.x.speed)
        plot_speed.plot(self.t, self.y.speed)
        plot_speed.plot(self.t, self.z.speed)
        plot_speed.legend(["x", "y", "z"])

        plot_acc = fig.add_subplot(313)
        plot_acc.set_title("Acceleration (m.s-2) dans le temps (s)")
        plot_acc.plot(self.t, self.x.acc)
        plot_acc.plot(self.t, self.y.acc)
        plot_acc.plot(self.t, self.z.acc)
        plot_acc.legend(["x", "y", "z"])

        TKFigure.add_to_frame(fig, parent, padding=10)

