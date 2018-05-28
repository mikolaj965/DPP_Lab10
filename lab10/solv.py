import math

def getsolution1(a, b, c):
    delta = b*b - 4*a*c
    x1 = -b-math.sqrt(delta)/(2*a)

    return x1

def getsolution2(a, b, c):
    delta = b*b - 4*a*c
    x2 = -b+math.sqrt(delta)/(2*a)

    return x2
