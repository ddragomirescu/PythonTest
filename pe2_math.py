#import math
from math import sin, pi
from random import randrange as rand 
import sys 

# Testing math module
# print(math.sin(math.pi/2), end="\n\n")

print(sin(pi/2))

def sin(x):
    if 2 * x == pi:
        return 0.999999
    else:
        return None
    
pi = 3.14

print(sin(pi/2))

print(round(rand(1,10)/pi , 2))

# print(math.sin(math.pi/2))