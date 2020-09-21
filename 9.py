n = int(input("Amount of money: "))

x1 = n * 0.04
x2 = (n + x1) * 0.04
x3 = (n + x1 + x2) * 0.04

print(n+x1, round(n+x1+x2, 2) , round(n+x1+x2+x3, 2))