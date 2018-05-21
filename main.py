# main.py
import sys
import cv2
from functions_robot import *


# -------------------------------------------
# Programacao Visao Computacional
#--------------------------------------------


# Retorna (x,y,z) - coordenadas destino do elemento final do manipulador.


# -------------------------------------------
# Programacao Cinematica 
#--------------------------------------------


r = Robot('robot') 
r.hello()

r.theta = np.array([0, 0, 0, 0, 0]) #Angulos das juntas desejado para a posicao destino

#Q = r.elo(0)
#A = transf_homogenea(Q)
#print A 


print r.elo(0) , "\n" 

T = transf_homogenea(r.base)
print 'Base: \n', T, "\n" 

T1 = transf_homogenea(r.elo(0))
print '1: \n', T1, "\n" 



