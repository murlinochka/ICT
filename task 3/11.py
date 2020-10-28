nn = int(input())

stringi = input()
stringi2 = ""
one = 0
zero = 0

for i in range(0, len(stringi)):
    if stringi[i]=='n':
        one += 1
    elif stringi[i]=='z':
        zero += 1

while(one):
    stringi2 += "1 "
    one -= 1
while(zero):
    stringi2 += "0"
    zero -= 1

print(stringi2)
