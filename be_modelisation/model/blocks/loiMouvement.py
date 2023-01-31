import numpy as np
import math as m

class LoiMouvement:

    def __init__(self, v_max, distance_total) -> None:
        self.vMax = v_max

        self.total_distance = distance_total
        self.totalTime =  2 * self.total_distance / v_max
        self.midTime = self.totalTime/2
        

    @property
    def total_time(self):
        return self.totalTime

    def get_distance(self, t):
        if t<=self.midTime :
            return  self.vMax*t*t/self.totalTime
        else:
            second_order =  -t*t/2 * self.vMax/self.midTime

            first_order =  t* self.totalTime*self.vMax / self.midTime
            
            zero_order =  - ( self.vMax * self.totalTime)/2 

            return  second_order + first_order + zero_order


    def get_speed(self, t):
        if t<=self.midTime :
            return 2*self.vMax*t/self.totalTime
        else:
            return -2*self.vMax*t/self.totalTime + 2*self.vMax 

    def get_acceleration(self, t):
        if t<=self.midTime :
            return 2*self.vMax/self.totalTime
        else:
            return -2*self.vMax/self.totalTime

    
    def movementLaw(self, t):
        return (self.get_distance(t), self.get_speed(t), self.get_accelaration(t))














































































"""
First Law
    A robot may not injure a human being or, through inaction, allow a human being to come to harm.
Second Law
    A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
Third Law
    A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.

In the event that a robot is found to be in violation of the First Law, the robot must be destroyed.
    
Isaac Asimov
"""
