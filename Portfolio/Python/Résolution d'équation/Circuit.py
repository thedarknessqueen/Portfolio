"""
@author: thais
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import sys

# Choix du modèle de voiture 
print("Quel modèle de voiture choisissez vous ? ")
print("1. Dodge Charger R/T")
print("2. Toyota Supra Mark IV")
print("3. Chevrolet Yenko Camaro 1969")
print("4. Mazda RX-7 FD")
print("5. Nissan Skyline GTR-R34")
print("6. Mitsubishi Lancer Evolution VII")
modele =int(input())
if modele ==1 :
    masse =1760
    acceleration = 5.1
    acceleration2 = 5.1
    acceleration3 = 5.1
    longueur = 5.28
    largeur = 1.95
    hauteur = 1.35
    Ox = 0.38
    Oz = 0.3
    mu = 0.1
elif modele ==2 :
    masse =1615
    acceleration = 5
    acceleration2 = 5
    acceleration3 = 5
    longueur = 4.51
    largeur = 1.81
    hauteur = 1.27
    Ox = 0.29
    Oz = 0.3
    mu = 0.1
elif modele ==3 :
    masse =1498
    acceleration = 5.3
    acceleration2 = 5.3
    acceleration3 = 5.3
    longueur = 4.72
    largeur = 1.88
    hauteur = 1.3
    Ox = 0.35
    Oz = 0.3
    mu = 0.1
elif modele ==4 :
    masse =1385
    acceleration = 5.2
    acceleration2 = 5.2
    acceleration3 = 5.2
    longueur = 4.3
    largeur = 1.75
    hauteur = 1.23
    Ox = 0.28
    Oz = 0.3
    mu = 0.1
elif modele ==5 :
    masse =1540
    acceleration = 5.8
    acceleration2 = 5.8
    acceleration3 = 5.8
    longueur = 4.6
    largeur = 1.79
    hauteur = 1.36
    Ox = 0.34
    Oz = 0.3
    mu = 0.1
elif modele ==6 :
    masse =1600
    acceleration = 5
    acceleration2 = 5
    acceleration3 = 5
    longueur = 4.51
    largeur = 1.81
    hauteur = 1.48
    Ox = 0.28
    Oz = 0.3
    mu = 0.1
else :
    print("Veuillez rentré un numéro valide")
    modele =int(input())
print("masse : ", masse, "kg , acceleration : ", acceleration, "m/s , longueur : ", longueur, "m , largeur : ", largeur, "m , hauteur : ", hauteur,"m.")

# Constantes 
g=9.81
inclinaison=0.06
distance = 31
diameter = 12
r= 6
k = (1/2)*1.2*hauteur*largeur*Ox
kp = (1/2)*1.2 *largeur*longueur*Oz
kt = (1/2)*1.2 *largeur*hauteur*Ox
Vi = 0
t0=0
tf=3.59
v0=0

# Ajout des accessoires 
print ("Souhaitez vous mettre un boost ? ")
boost = str(input())
if boost=="oui":
   print ("Sur quelle partie souhaitez vous le mettre ? \n1. La descente. \n2. Le looping. \n3. Le saut.") 
   boost = int(input())
   if boost == 1 :
       acceleration = acceleration * 1.3
   if boost == 2 :
       acceleration2 = acceleration * 1.3
   if boost == 3 :
       acceleration3 = acceleration * 1.3
print ("Souhaitez vous mettre des ailerons ? ")
aile = str(input())
if aile=="oui":
   kp= kp * 1.1
   masse = masse + 30
print ("Souhaitez vous mettre une jupe ? ")
jupe = str(input())
if jupe=="oui":
   kt= kt * 0.95
   masse = masse + 15


# Ajustement de la courbe 
t = np.linspace(t0, tf, 100) 

# Définition de l'équation différentielle
def descente(V, t):  
    a = -(k/masse)
    b = g * (-mu*np.cos(inclinaison)+np.sin(inclinaison)) + acceleration
    return a*V**2+b
  
# Résolution de l'équation différencielle
V = odeint(descente, Vi, t)


# Tracé du graphique 
plt.plot(t, V[:, 0], color="blue")
plt.title("Évolution de la vitesse au cours de la descente")
plt.ylabel('Vitesse (m/s)')
plt.xlabel("Temps (s)")

# Affichage de la vitesse en fin de looping
a, b = np.polyfit(t, V, 1)
plt.plot(t,V)
plt.plot(t,a*t+b)
vf=float( a*tf+b)
print("la valeur de la vitesse en fin de pente est : {:.2f}".format(vf)," m/s.")
print("Le temps pris pour faire la descente est : ", tf, " s.")
vf=float( a*tf+b)
if vf>17:
    print("Le véhicule passe donc le looping.")
else:
    print("Le véhicule ne passe donc pas le looping.")

# Réglage des graduations et du quadrillage
plt.xticks(np.arange(t0, tf + 1, 0.5))
plt.yticks(np.arange(0, max(V[:, 0]) + 1, 2))
plt.grid(True)
plt.show()

# Conversion en radians par secondes
acceleration2 = 5/r 
# Vitesse angulaire initiale en rad/s
theta_dot_initial =vf/r

# Conditions initiales
theta_initial = 0
theta_final = 2 * np.pi
theta = np.linspace(theta_initial, theta_final, 1000)

# Vitesse angulaire initiale en rad/s
theta_dot_initial =vf/r

# Définition d'équation différentielle
def looping(y, theta):
    theta1, theta2 = y
    theta1dt = theta2
    theta2dt = -math.sqrt(masse * r * theta2 - masse * g * (-np.sin(theta) - mu * np.cos(theta)) / (mu * masse * r + k * r**2)) + acceleration2 
    return [theta1dt, theta2dt]


# Résolution de l'équation différentielle
solution = odeint(looping, [theta_dot_initial,0], theta)

# Extraction de theta1 de la solution
theta1 = solution[:, 0]

# Tracé du graphique
plt.figure(figsize=(8, 6))
plt.plot(theta, theta1, color="blue")
plt.title("Évolution de la vitesse angulaire au cours du looping")
plt.xlabel("Angle theta (rad)")
plt.ylabel("Vitesse angulaire (rad/s)")
plt.grid(True)
plt.show()

# Affichage de la vitesse en fin de looping
derniere_valeur = theta1[-1]
#print("La valeur de la vitesse angulaire en sortie de looping est :", derniere_valeur)
print("La valeur de la vitesse en sortie de looping est : {:.2f}".format(derniere_valeur*r), " m/s.")


# Calcul de la vitesse angulaire moyenne
vitesse_angulaire_moyenne = np.mean(theta1)

# Convertir la vitesse angulaire moyenne en mètres par seconde
vitesse_lineaire_moyenne = vitesse_angulaire_moyenne * r

# Calcul du temps pris pour faire le looping
temps_looping = 2 * np.pi * r / vitesse_lineaire_moyenne

#print("La vitesse angulaire moyenne au cours du looping est :", vitesse_angulaire_moyenne, "rad/s")
#print("La vitesse linéaire moyenne au cours du looping est :", vitesse_lineaire_moyenne, "m/s")
print("Le temps pris pour faire le looping est : {:.2f}".format(temps_looping), " s.")


# Constantes
ro = 1.2
V0x = derniere_valeur * r
V0y = 0
t0 = 0
tfinal = 2

# Déclaration des conditions initiales
S_init=[0,0,V0x,V0y]
t = np.linspace(t0,tfinal,100)

# Declaration de l'équation différentielle avec le vecteur d'etat Sp
def Sp(S,t):
   Sp = [S[2],S[3],-ro/(2*masse)*np.sqrt(S[2]**2+S[3]**2)*(kt*S[2]+kp*S[3]),-ro/(2*masse)*np.sqrt(S[2]**2+S[3]**2)*(kt*S[3]-kp*S[2])-g]
   return Sp

# Resolution de l'équation différentielle pour déterminer S
S = odeint(Sp,S_init,t)

# Tracé du graphique
plt.plot(S[:,0],S[:,1])
plt.title('Trajectoire du véhicule')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.ylim(-1, 0)
plt.xlim(0, 12)
plt.xticks(np.arange(t0, 13 + 1, 1))
x = S[:,0]

a, b, c = np.polyfit(x,S[:,1], 2)
y2 = a*x**2 + b*x + c
plt.plot(x,y2)
plt.show()

posit9 = a*9**2+b*9+c
tbas = None
for i, p in enumerate(S[:,0]):
    if p >= 9:
        tbas = t[i]
        break
print("L'altitude du véhicule à 9m est de : {:.2f}".format(posit9)," m.")

if posit9 < -1 :
    print("Le véhicule ne passe donc pas le ravin.")
else :
    print("Le véhicule passe donc le ravin.")
    if tbas is not None:
        print("Le temps pris pour faire le saut est : {:.2f}".format(tbas), " s.")
    else:
        print("La position n'est pas atteinte dans la plage de temps spécifiée.")

print("Le temps total mis par la voiture du haut de la pente jusqu'a l'attérissage après le ravin est de : {:.2f}".format( tf + temps_looping + tbas), " s.")

if tf + temps_looping + tbas <8:
    print("Votre voiture bat celle de Owen Shaw ! ")
else :
    print("Retentez votre chance, votre voiture ne bat pas celle de Owen Shaw avec ce temps")
  