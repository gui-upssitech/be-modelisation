from .point import Point
from .parameters import Parameters
from .blocks import LoiMouvement, Trajectory, MGD, MGI

import numpy as np


class Law:
    def __init__(self, dist, speed, acc):
        self.dist = dist
        self.speed = speed
        self.acc = acc

class Livrable:

    def __init__(self, t, s, x, y, z, q, joints):
        self.t = t
        self.s = s

        self.x = x
        self.y = y
        self.z = z

        self.q = q
        self.joints = joints



def trajectoire(a, b, theta, v, parameters):
    mvt_law = LoiMouvement(v, a.dist(b))

    t = np.linspace(0, mvt_law.total_time, 1000)
    
    # ==================================================================================
    # Create movement law
    
    s = Law(
        [ mvt_law.get_distance(i) for i in t ],
        [ mvt_law.get_speed(i) for i in t ],
        [ mvt_law.get_acceleration(i) for i in t ]
    )

    # ==================================================================================
    # Get x,y,z trajectories

    traj = Trajectory(a, b)
    vec_dist = [ traj.get_distance(i) for i in s.dist ]
    vec_speed = [ traj.get_speed(i) for i in s.speed ]
    vec_acc = [ traj.get_acceleration(i) for i in s.acc ]

    def seg(func):

        return Law(
            [ func(x) for x in vec_dist ],
            [ func(x) for x in vec_speed ],
            [ func(x) for x in vec_acc ]
        )

    x = seg(lambda p: p.x)
    y = seg(lambda p: p.y)
    z = seg(lambda p: p.z)

    # ==================================================================================
    # Generate list of Q's
    
    mgi = MGI(parameters)
    q_list = [ mgi.compute(p, theta) for p in vec_dist ]
    q_list = [ [ q[i] for q in q_list ] for i in range(len(q_list[0])) ]

    # ==================================================================================
    # Generate list of joints
    
    mgd = MGD(parameters)
    joints = [ [mgd.compute_joints(q) for q in q_list_opt] for q_list_opt in q_list ]

    # ==================================================================================
    # Return results
    
    return Livrable(t, s, x, y, z, q_list, joints)
