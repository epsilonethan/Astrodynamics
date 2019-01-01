import math
import sys
import os
import numpy as np

#Magnitude of vector
def magnitude(vector):
    a = 0
    for val in vector:
        a += val**2

    return math.sqrt(a)