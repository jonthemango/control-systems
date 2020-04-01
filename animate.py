from control import *
from control.matlab import * 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle
from IPython.display import HTML
from constants import  mass_of_the_load , mass_of_the_cart , length, gravity, force, kp, ki, kd, a,b,c,d

def x(t):
    return t

def theta(t):
    z = np.linspace(-90,90,100)
    return z[t]

def run(l=5,x=x, theta=theta, frames=100, interval=20):
    plt.style.use('seaborn-pastel')
    def show(anim):
        return HTML(anim.to_jshtml())
    fig = plt.figure()
    ax = plt.axes(xlim=(-20, 20), ylim=(-20, 20))
    ln, = plt.plot([], [], 'ro-', animated=True)
    cart = Rectangle((0,-1), 5, 5)
    ax.add_artist(cart)
    ax.set_aspect('equal', 'box')
    title = ax.text(0.5,0.85, "", bbox={'facecolor':'w', 'alpha':0.5, 'pad':5},
                    transform=ax.transAxes, ha="center")
    

    def init():
        return ln, title

    def update(i):
        
        t = i
        
        position_of_cart = x(t/20)
        angle_of_pendulum = theta(t)
        title.set_text(u"x(t) = {}, Theta(t) = {}°".format(np.round(position_of_cart), np.round(angle_of_pendulum)))
        
        cart.set_x(position_of_cart)
        
        p1 = (position_of_cart+(cart.get_width()/2), cart.get_y())
        opp = np.sin(np.deg2rad(angle_of_pendulum))*l
        adj = np.cos(np.deg2rad(angle_of_pendulum))*l
        
        
        p2 = (p1[0]-opp,p1[1]-adj)
        ln.set_data([p1[0],p2[0]],[p1[1],p2[1]])
        return ln, cart, title

    anim = FuncAnimation(fig, update, init_func=init, frames=frames, interval=interval, blit=True)
    return show(anim)

if __name__ == "__main__":
    run()
    plt.show()