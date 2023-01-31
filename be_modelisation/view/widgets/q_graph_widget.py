from tkinter import *

from ..tkfigure import TKFigure

class QGraphWidget:

    def __init__(self, t, q):
        self.t = t
        self.q_lists = q
        self.cur_list = 0

    @property
    def q_list(self):
        return self.q_lists[self.cur_list]

    def draw(self, parent):
        # Create widget root
        root = Frame(parent)

        # Draw 3 figures
        self.draw_fig(root)

        # Add widget to parent
        root.pack(fill=BOTH, expand=True)
        parent.add(root, text="Evolution des Q")

        self.__parent = parent
        self.__root = root

    def redraw(self):
        self.__root.destroy()        
        self.draw(self.__parent)

    def draw_fig(self, parent):
        fig = TKFigure.new_fig()
        fig.set_constrained_layout(True)

        plot_dist = fig.add_subplot(211)
        plot_dist.set_title("Evolution des q dans le temps (Option 1)")
        plot_dist.plot(self.t, self.q_lists[0])
        plot_dist.legend(["q1", "q2", "q3", "q4"])

        plot_dist = fig.add_subplot(212)
        plot_dist.set_title("Evolution des q dans le temps (Option 2)")
        plot_dist.plot(self.t, self.q_lists[1])
        plot_dist.legend(["q1", "q2", "q3", "q4"])

        TKFigure.add_to_frame(fig, parent, padding=10)

