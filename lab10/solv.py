import math

delta = 0

def getsolution1(a, b, c):
    d = calculatedelta(a,b,c)
    if d >= 0:
        x1 = (-b-math.sqrt(d))/(2*a)
    else:
        return -1
    return x1


def getsolution2(a, b, c):
    d = calculatedelta(a,b,c)
    if d >= 0:
        x2 = (-b+math.sqrt(d))/(2*a)
    else:
        return -1

    return x2
