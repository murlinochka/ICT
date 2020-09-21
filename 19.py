from math import sqrt

g = 9.8

h = float(input("Height of dropping object : "))

v = sqrt(2 * g * h)

print("Object will hit the ground at %.2f m/s." % v)