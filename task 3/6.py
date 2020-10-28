stringi = input()

upper = 0
lower = 0

for i in range(0, len(stringi)):
    if stringi[i] >= 'a' and stringi[i] <= 'z':
        lower += 1
    if stringi[i] >= 'A' and stringi[i] <= 'Z':
        upper += 1

if upper > lower:
    print(stringi.upper())
else:
    print(stringi.lower())