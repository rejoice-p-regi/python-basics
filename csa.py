from math import pi
# r = float(input("input the radius of thr circle : "))
# area = pi*r**2
# print(area)
# r = float(input('radius of sphere'))
# area = 4*pi*radius*2
# print(area)

def surfacearea(r, h):
    return pi*r*h+pi*r*r
radius = float(input("input the radius of corn: "))
height = float(input("input the height of corn"))
print(surfacearea(radius,height))
