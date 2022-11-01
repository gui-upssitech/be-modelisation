import afficheCourbesTP as affC
import numpy as np


class LoiMouvement:

    def __init__(self, vMax:float,distanceTotal:float) -> None:
        self.vMax = vMax
        self.distanceTotal = distanceTotal

        self.totalTime = 4/vMax
        self.midTime = self.totalTime/2

    def getDistance(self,t:float) -> float:
        if t<=self.midTime :
            return  self.vMax*t*t/self.totalTime
        else:
            return 2*t*self.vMax - self.vMax*t*t/self.totalTime

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


#fonction de test de la loi de mouvement, Te en ms, vMax en m.s-1, distance en m
def testLoiMouvement(vMax,distance, te):
    print("Simulation de la loi de mouvement")
    lm = LoiMouvement(vMax,distance) #vitesse 3, distance de 10
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

    

if __name__ == "__main__":
    testLoiMouvement(4,10,0.01)
    #testLoiMouvement(1,10,0.01)

    affC.bloque_affiche()














































































"""
First Law
A robot may not injure a human being or, through inaction, allow a human being to come to harm.
Second Law
A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
Third Law
A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.
"""
