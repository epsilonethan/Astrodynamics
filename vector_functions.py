import math
import sys
import os
import numpy as np

def magnitude(vector):
    a = 0
    for val in vector:
        a += val**2

    return math.sqrt(a)

def vec_sum(vec1, vec2):
    if type(vec1).__module__ == np.__name__ and type(vec2).__module__ == np.__name__:
        return vec1 + vec2
    else:
        sys.exit("One or more vecctors are not numpy arrays")

def vec_norm(vec):
    return vec/magnitude(vec)

def vec_dot(vec1, vec2):
    a = 0
    for i in len(vec1):
        a += vec1[i]*vec2[i]
    return a

def vec_angle(vec1, vec2):
    a = vec_norm(vec1)
    b = vec_norm(vec2)
    return math.acos(vec_dot(a,b))

def vec_cross(vec1, vec2):
    return np.cross(vec1, vec2)

def vec_to_polar(vec):
    if len(vec) == 3:
        r = magnitude(vec)
        theta = math.acos(vec[2]/r)
        azimuth = math.atan(vec[1]/vec[0])
        return r, theta, azimuth
    elif len(vec) == 2:
        r = magnitude(vec)
        theta = math.acos(vec[1] / r)
        return r, theta

def vec_to_cart(vec):
    if len(vec) == 3:
        x = vec[0]*math.sin(vec[1])*math.cos(vec[2])
        y = vec[0]*math.sin(vec[1])*math.sin(vec[2])
        z = vec[0]*math.cos(vec[1])
        return x, y, z
    elif len(vc) == 2:
        x = vec[0]*math.cos(vec[1])
        y = vec[0]*math.sin(vec[1])
        return x, y
