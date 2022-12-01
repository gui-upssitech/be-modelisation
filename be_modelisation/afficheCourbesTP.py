# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:17:54 2020

@author: taix
"""
import matplotlib.pyplot as plt;
import numpy as np
#############################################################################
# Affichage de la fonction f(t) et de ses dérivées fd(t) et fdd(t) 
#           et des temps de commutation
#INPUT:
#    numfig: numéro de la figure (entier)
#    nom: chaîne de caractèreS qui correspond à la fonction à afficher
#    f: valeurs discrètes de la fonction s en ordonnée du subplot haut
#    fd: valeurs discrètes de la fonction fd en ordonnée du subplot milieu
#    fdd: valeurs discrètes de la fonction fdd en ordonnée du subplot bas
#    t: valeurs discrètes du temps de 0 à tf en abscisse des 3 subplot
#    tc: liste des instants de commutation 
#
#    ATTENTION: il faut que les dimensions de f,fd,fdd et t soient identiques
#############################################################################
def affiche3courbes(numfig,nom,f,fd,fdd,t,tc):
    plt.figure(numfig)

    plt.subplot(311)
    plt.plot(t, f, "r-")
    plt.xlabel('Temps')
    plt.ylabel('Valeur de ' + nom)
    plt.grid(True)
    for x in tc:
        plt.axvline(x,color="g",linestyle="--")
    plt.title('Affichage des courbes fonction de ' + nom)
    plt.subplot(312)
    plt.plot(t, fd, "r-")
    plt.xlabel('Temps')
    plt.ylabel('Valeur de ' + nom+'d')
    plt.grid(True)
    for x in tc:
        plt.axvline(x,color="g",linestyle="--")
    plt.subplot(313)
    plt.plot(t, fdd, "r-")
    plt.xlabel('Temps')
    plt.ylabel('Valeur de ' + nom+'dd')
    plt.grid(True)
    for x in tc:
        plt.axvline(x,color="g",linestyle="--")   
    
    plt.show(block=False)
    
#############################################################################
# Affichage d'une courbe 2D d'abscisse t et d'ordonnée d(t)
#INPUT:
#    numfig: numéro de la figure (entier)
#    nom: chaîne de caractèreS qui correspond à la fonction à afficher
#    t: valeurs discrètes du temps  en abscisse
#    d: valeurs discrètes de la fonction s en ordonnée 
#    coul: couleur de la courbe (exemple "r" pour rouge)
#
#    ATTENTION: il faut que les dimensions de d et t soient identiques
#############################################################################  
def affiche_courbe2D(numfig,nom,t,d,coul):
    plt.figure(numfig)
    plt.axis([np.min(t)-1,  np.max(t), np.min(d), 1.2* np.max(d)])
    plt.plot(t, d,"-", label="ligne -",color=coul)
    plt.xlabel('Temps')
    plt.ylabel('Valeur de ' + nom)
    plt.title('Affichage de la courbe ' + nom)
    plt.show(block=False) # affiche la figure a l'ecran
################################
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
    
