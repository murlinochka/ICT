from math import tan,pi


l = float(input("Length: "))
n = int(input("Number of sides: "))
 
area = (n * l ** 2)/(4 * tan(pi/n))
 
print("The area of Polygon ", area)