import math
import sys
import os
import numpy as np
import vector_functions as vf


#========================
#Keplers Laws
#1. The orbit of each planet is an ellipse, with the sun at a focus
#2. The line joining the planet to the sun sweeps out equal areas in equal times
#3. The square of the period of a planet is proportional to the cube of its mean distance from the sun
#========================

#========================
#Newtons Laws
#1. Every body continues in its state of rest or of uniform motion in a straight line unless it is
#   compelled to change that state by forces impressed upon it
#2. The rate of change of momentum is proportional to the force impressed and is in the same direction as that force
#3. To every action there is always opposed an equal reaction

class M_object():
    def __init__(self, pos, vel, mass):
        self.pos = pos
        self.vel = vel
        self.mass = mass


'''
class Vector(np.ndarray):
    Defines 3D vectors which inherit from Numpy

    def __init__(self, *args):
        np.ndarray.__init__(*args)
        if len(args[0]) == 3:
            self.vec = np.asarray(args[0])
        else:
            print("Initialization Of Vector Aborted Due To Incorrect Number Of Arguments")
            sys.exit("Abort Due To Vector Error")

    # Start filling in vector functions here
'''


# n-body force of gravity
def f_grav(body1, body2):
    r_vec = body2.pos - body1.pos
    r = vf.magnitude(r_vec)
    f_g_vec = -(G*body1.mass*body2.mass*r_vec)/(r**3)
    f_g_mag = vf.magnitude((f_g_vec))

    #print(r_vec)
    #print(r)
    #print(f_g_vec)
    #print(f_g_mag)

    return f_g_vec

def f_grav_n(*args, ref=0):
    ref_body = args[ref]
    list_args = []

    for arg in args:
        list_args.append(arg)

    list_args.remove(ref_body)
    f_g_n_vec = np.array((0.0, 0.0, 0.0))

    for body in list_args:
        f_g_vec = f_grav(ref_body, body)
        f_g_n_vec += f_g_vec

    return f_g_n_vec

def a_grav(f_grav_vec, body):
    a_grav_vec = f_grav_vec/body.mass
    return a_grav_vec

def specific_anglular_momentum(pos_vec, vel_vec):
    return vf.vec_cross(pos_vec, vel_vec)


# TESTING
if __name__ == "__main__":
    G = 6.67408 * 10**-11  # m^3/(kg*s^2)
    m1 = 5.972 * 10**24  # kg Mass of Earth
    m2 = 150.0
    m3 = 200.0
    vel1 = np.array((0.0, 0.0, 0.0))
    vel2 = np.array((0.0, 0.0, 0.0))
    vel3 = np.array((0.0, 0.0, 0.0))
    pos1 = np.array((0.0, 0.0, 0.0))
    pos2 = np.array((0.0, 0.0, 6378000.0))
    pos3 = np.array((0.0, 2.0, 6378002.0))
    body1 = M_object(pos1, vel1, m1)
    body2 = M_object(pos2, vel2, m2)
    body3 = M_object(pos3, vel3, m3)
    force = f_grav_n(body1, body2, body3, ref=0)
    print(force)
    print(a_grav(force, body1))
