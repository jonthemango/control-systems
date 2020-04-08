from control import *
from control.matlab import * 
import numpy as np
import matplotlib.pyplot as plt

from constants import  mass_of_the_load , mass_of_the_cart , length, gravity, force, kp, ki, kd, a,b,c,d

def percent_overshoot(g):
    x =  step_info(g)['Overshoot']
    return x

def is_stable(g):
    poles = pole(g)
    for p in poles:
        if p.real > 0:
            return False
    return True

def get_poles(g):
    poles = pole(g)
    return poles

def get_zeroes(g):
    zeros = zero(g)
    return zeros

def plot_root_locus(g, plot=True):
    root_locus(g, Plot=plot)


def describe_DE(a1, a2, a3, b0, b1,b2):
    sys = tf([b0,b1,b2],[0,a1,a2,a3])
    print(sys)
    print(ss([[0,1,0],[0,0,1],[-a3,-a2,-a1]], [[0],[0],[1]], [b2,b1,b0], 0))

#describe_DE(2,3,4,0,0,5)

#describe_DE(9,26,24,0,0,24)

#describe_DE(8.5,7,4,0,0,5)

#describe_DE(0,1,(mass_of_the_load+mass_of_the_cart) /(mass_of_the_cart*length),0,0,1/(mass_of_the_cart*length))

