p = int(input("Pressure : "))
v = int(input("Volume : "))
t = int(input("Temperature : "))
r = 8.314

n = ((p*v)/(r*t))

print("The number of moles  %.2f mol." % n)
