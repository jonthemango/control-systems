## https://python-control.readthedocs.io/en/0.8.3/
from control import *
from control.matlab import * 
import numpy as np
import matplotlib.pyplot as plt

from constants import  mass_of_the_load , mass_of_the_cart , length, gravity, force, kp, ki, kd, a,b,c,d

# theta'' = a*theta + F/b ==> theta(t) 
# Given:
# k*theta'' = k*s^2 * THETA(s)
# k*theta' = k*s * THETA(s)
# k*theta = k*THETA(s)
# k = k
# Then:
#  s^2 * THETA(s) = a*THETA(s) + F(s) / b
#  F(s) = s^2*THETA(s)*b - a*THETA(s)*b
#  F(s) = THETA(s)*[b*s^2 - a*b] (1)
#  F(s)/[b*s^2 - a*b] = THETA(s) (1.2)
#  THETA(s)/F(s) = 1 / [b*s^2 - a*b]  

# x'' = c*theta + F/d ==> x(t)
# k*x'' = k*s^2  * X(s)
# k*x' = k*s * X(s)
# k*x = k*X(s)
# k = k
# Then:
# s^2*X(s) = c *s^2*THETA(s) + F(s)/d
# F(s) = d*s^2*X(s) - d*c*s^2*THETA(s) (2)
# (F(s) - d*s^2*X(s)) / (- d*c*s^2) = THETA(s) (2.2)
# if (1) = (2) :
# b*s^2*THETA(s) - a*b*THETA(s) = d*s^2*X(s) - d*c *s^2*THETA(s)
# b*s^2*THETA(s) - a*b*THETA(s) + d*c*s^2*THETA(s) = d*s^2*X(s) 
# THETA(s) * [b*s^2 + a*b + d*c*s^2] = d*s^2*X(s) 
# THETA(s) / X(s) =  d*s^2 / [b*s^2 + a*b + d*c*s^2]
# THETA(s) / X(s) = d*s^2 / [(b+d*c)*s^2 + a*b]
# if (1.2) = (2.2):
# F(s)/[b*s^2 - a*b] = (F(s) - d*s^2*X(s)) / (- d*c *s^2)
# F(s) / [F(s) - d*s^2*X(s)] = [b*s^2 - a*b] / (- d*c *s^2)


# basic tf  G(s) = s
s = tf('s')

# PID Controller
C = kp + ki/s + kd*s 
print("PID C = ",C)