import afficheCourbesTP as affC
import numpy as np
import math as m

class LoiMouvement:

    def __init__(self, vMax:float,start_point:np.array,end_point:np.array) -> None:
        self.vMax = vMax
        self.start_point = start_point
        self.end_point = end_point

        self.distanceTotal = np.linalg.norm(end_point - start_point)
        self.totalTime =  2 * self.distanceTotal/vMax
        self.midTime = self.totalTime/2
        


    def getDistance(self,t:float) -> float:
        if t<=self.midTime :
            return  self.vMax*t*t/self.totalTime
        else:
            second_order =  -t*t/2 * self.vMax/self.midTime

            first_order =  t* self.totalTime*self.vMax / self.midTime
            
            zero_order =  - ( self.vMax * self.totalTime)/2 

            return  second_order + first_order + zero_order


    def getSpeed(self,t:float) -> float:
        if t<=self.midTime :
            return 2*self.vMax*t/self.totalTime
        else:
            return -2*self.vMax*t/self.totalTime + 2*self.vMax 

    def getAcc(self,t:float) -> float:
        if t<=self.midTime :
            return 2*self.vMax/self.totalTime
        else:
            return -2*self.vMax/self.totalTime

    
    def movementLaw(self, t:float) -> tuple:
        return (self.getDistance(t), self.getSpeed(t), self.getAcc(t))


    def plot(self, t_array, pos_array, speed_array, acc_array) -> None:
        affC.afficheAccSpeedPos(t_array, pos_array, speed_array, acc_array)
        affC.bloque_affiche()
        


#fonction de test de la loi de mouvement, Te en ms, vMax en m.s-1, distance en m
#prend également en entrée la période d'échantillonage Te en s
def testLoiMouvement(vMax:float,point_A:np.array,point_B:np.array, te:float) -> None:
    print("Simulation de la loi de mouvement")

    lm = LoiMouvement(vMax,point_A,point_B) #vitesse 3, distance de 10
    print("Loi de mouvement initialisé")
    print("objectif de vitesse Max : ",lm.vMax)
    print("Distance à parcourir : ", lm.distanceTotal)
    print("Temps total : ",lm.totalTime)
    

    dCurve =[]
    sCurve = []
    aCurve = []

    print("Simulation en cours...")
    simTime = list(np.arange(0,lm.totalTime,te))
    

    for t in simTime:
        dCurve.append(lm.getDistance(t))
        sCurve.append(lm.getSpeed(t))
        aCurve.append(lm.getAcc(t))

    print("Accélération max : ",np.max(aCurve))
    print("Vitesse max : ",np.max(sCurve))
    print("Distance max : ", np.max(dCurve))
    print("Affichage des résultats de simulation")
    
    affC.afficheAccSpeedPos(simTime,aCurve,sCurve,dCurve)

    transition_time =  m.ceil(len(simTime)/2)

    transitionError = dCurve[transition_time] - dCurve[transition_time -1]

    print("\ntransition_time : ",transition_time)
    print("Erreur de transition : ",transitionError)

    

if __name__ == "__main__":
    point_A = np.array([0,0,0])
    point_B = np.array([10,0,0])

    testLoiMouvement(4,point_A,point_B,0.01)

    affC.bloque_affiche()














































































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
