from be_modelisation.model import Robot, Point
from tkinter import *
from ..tkfigure import TKFigure
from matplotlib.animation import FuncAnimation
import numpy as np
import time

from matplotlib.patches import Circle
from mpl_toolkits.mplot3d import art3d

class RobotWidget:

    def __init__(self, robot: Robot):
        self.__robot = robot
        self.__show_bounds = IntVar()

    # =================
    # Public methods
    # =================

    def draw(self, parent):
        root = Frame(parent, bg="#FFFFFF")
        self.__figure = TKFigure.new_fig()
        self.__ax = self.__figure.gca(projection='3d')

        self.__draw_robot()

        TKFigure.add_to_frame(self.__figure, root)

        self.__draw_settings(root)
        root.pack(fill=BOTH, expand=True)

    def redraw(self):
        self.__ax.clear()
        self.__draw_robot()
        self.__figure.canvas.draw_idle()

    def animate(self):
        print("Animating")

        total_time = self.__robot.movement_law.total_time
        for i in np.linspace(0, total_time, 50):
            self.seek(i)
            time.sleep(0.1)
        pass

    def seek(self, value):
        value = float(value)
        r = self.__robot
        
        point = Point(*r.trajectory.get_distance(value))
        r.set_position(point)
        self.redraw()

        print("Seeking", value, "->", point)

    # =================
    # Private methods
    # =================
    def __draw_settings(self, parent):
        settings = Frame(parent, bg="#FFFFFF")

        def draw_button():
            show_btn = Checkbutton(settings, text="Afficher la zone de travail", bg="#FFFFFF", 
                                   variable=self.__show_bounds, onvalue=1, command=self.redraw)
            show_btn.grid(row=0, column=0, pady=10, sticky="w")

        def draw_playback():
            play_btn = Button(settings, text="Lancer simulation", command=self.animate)
            play_btn.grid(row=1, column=0, sticky="w")

            total_time = self.__robot.movement_law.total_time
            play_seek = Scale(settings, from_=0, to=total_time, resolution=total_time/1000, orient=HORIZONTAL, showvalue=0, command=self.seek)
            play_seek.grid(row=1, column=1, sticky="ew", columnspan=2)

        
        draw_button()
        draw_playback()
        
        settings.pack(padx=10, pady=10, side=LEFT, fill=X)

    def __draw_robot(self):
        ax = self.__ax
        r = self.__robot

        def draw_traj():
            a, b = r.param("A"), r.param("B")
            self.__traj_line, = ax.plot3D([a.x, b.x], [a.y, b.y], [a.z, b.z], 'o-', color="#FF0000", lw=2, markersize=4)

        def draw_circle():
            circle = Circle((0, 0), sum(r.get_lengths()), color="#FF0000", alpha=0.1, fill=True)
            ax.add_patch(circle)
            art3d.pathpatch_2d_to_3d(circle, z=0, zdir="z")

        def set_limits():
            limit = sum(r.get_lengths()) * 1.2
            ax.set_xlim(-limit, limit)
            ax.set_ylim(-limit, limit)
            ax.set_zlim(0, limit)

        def draw_joints():
            pair = True
            old_point = Point(0, 0, 0)

            for point in r.get_joints():
                color = "#333333" if pair else "#AAAAAA"
                pair = not pair            
                
                ax.plot3D([old_point.x, point.x], [old_point.y, point.y], [old_point.z, point.z], 'o-', lw=12 , markersize=16, color=color)
                old_point = point

        if self.__show_bounds.get() == 1:
            draw_circle()
        
        draw_joints()
        draw_traj()
        set_limits()
    