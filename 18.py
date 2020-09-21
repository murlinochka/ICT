HEAT_CAPACITY = 4.186
J_TO_KWH = 2.777e-7 

v = float(input("Enter amount of water in milliliters: "))
t = float(input("Enter amount of temperature increase (degrees Celsius): "))
p = float(input("Enter electricity cost per unit: "))
 
energy  = v * t * HEAT_CAPACITY
kwh     = energy * J_TO_KWH
cost    = kwh * p

print("Amount of energy needed ",round(energy,2),"Joules, which will cost", round(cost,2))