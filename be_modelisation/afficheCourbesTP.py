# -*- coding: utf-8 -*-
# Path: src/loi_mouvement/afficheCourbesTP.py

import matplotlib.pyplot as plt;
import numpy as np

#affiche les figures qui on été créées
def bloque_affiche():
    plt.show(block=True)


def afficheAccSpeedPos( t, acc, speed, pos, nom="s"):  
    
    fig, axs = plt.subplots(3)

    axs[2].plot(t,pos)
    axs[2].set_title("Distance(m) dans le temps(s)")

    axs[1].plot(t,speed)
    axs[1].set_title("Vitesse(m.s-1) dans le temps(s)")

    axs[0].plot(t, acc)
    axs[0].set_title("acceleration(m.s-2) dans le temps(s)")

    # fig.('Affichage des courbes fonction de ' + nom)
    fig.set_label("temps en s")
    plt.show(block=False)
    


