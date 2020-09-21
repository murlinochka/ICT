a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))

x = min(a, b, c)
z = max(a, b, c)
y = (a + b + c) -x - z
print("Numbers in sorted order: ", x, y, z)