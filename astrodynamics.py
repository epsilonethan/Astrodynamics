import math
import sys
import os
import numpy as np


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

#class M_object():

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

def f_grav(m1, m2, pos1, pos2):
    r_vec = pos2 - pos1
    r = math.sqrt(r_vec[0]**2 + r_vec[1]**2 + r_vec[2]**2)
    f_g_vec = -(G*m1*m2*r_vec)/(r**3)
    f_g_mag = math.sqrt(f_g_vec[0]**2 + f_g_vec[1]**2 + f_g_vec[2]**2)

    print(r_vec)
    print(r)
    print(f_g_vec)
    print(f_g_mag)


# TESTING
if __name__ == "__main__":
    G = 6.67408 * 10**-11  # m^3/(kg*s^2)
    m1 = 5.972 * 10**24  # kg Mass of Earth
    m2 = 150.0
    pos1 = np.array((0.0, 0.0, 0.0))
    pos2 = np.array((0.0, 0.0, 6378000.0))
    f_grav(m1, m2, pos1, pos2)
