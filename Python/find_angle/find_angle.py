'''
Given triangle with points ABC:
-given length of AB and BC, find angle theta
such that it is the angle made between the two sides,
bisected by a going to the midpoint of the hypotenuse side.
'''

import math

AB, BC = int(input()), int(input())

hypotenuse = hypot(AB, BC)
angle = round(math.degrees(math.acos(BC/hypotenuse)))
degree = chr(176) # for degree symbol

print(angle,degree, sep='')
