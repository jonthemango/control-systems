from control import *
from control.matlab import * 
import numpy as np
import matplotlib.pyplot as plt


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

def plot_root_locus(g):
    root_locus(g)


g = feedback(tf([1, 0.5],[1,2,-8,4]), tf([1],[1,0.2]))

