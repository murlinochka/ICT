stringi = input()
listi = []
a = ""

for i in range(0, len(stringi)):
    if stringi[i] != "+":
        listi.append(stringi[i])

listi.sort()

for i in range(0, len(listi)-1):
    a += (listi[i] + "+")
a += listi[len(listi)-1]
print(a)
    
