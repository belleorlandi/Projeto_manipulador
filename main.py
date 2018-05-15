# main.py

import cv2
from functions_robot import *


A = dh(0,90,0,1)
print (A)
r = Robot('5dof')
print (r.elo(0))
print (r.elo(1))
print (r.elo(2))