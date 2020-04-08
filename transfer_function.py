## https://python-control.readthedocs.io/en/0.8.3/
from control import *
from control.matlab import * 
import numpy as np
import matplotlib.pyplot as plt

from scratch_pad import percent_overshoot, is_stable, get_poles, get_zeroes, plot_root_locus

# basic tf  G(s) = s
s = tf('s')

kp = 4800 # INCREASING kp => DECREASE rise_time, INCREASE overshoot, SMALL CHANGES in settling_time, DECREASE steady_state_error
ki = 0
kd = 900 # INCREASING kd => SMALL CHANGES in rise_time, DECREASE overshoot, DECREASE in settling_time, NO CHANGE in steady_state_error

gain = 1
# PID Controller
C = kp + ki/s + kd*s 
print("PID C = ",C)

G = tf(1,[240,0,1400])
print(G)

closed_loop = feedback(series(gain,C,G),1)

print(closed_loop)
print(step_info(closed_loop))
print(is_stable(closed_loop))
print(damp(closed_loop))
x,y = step_response(closed_loop)
plt.plot(x,y)
plot_root_locus(closed_loop)
plt.show()
# print(y)