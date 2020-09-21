import math

v = float(input("Wind speed: "))
t = float(input("Air temperature: "))

w = 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
print("The wind chill index is ", int(round(w, 0)))
