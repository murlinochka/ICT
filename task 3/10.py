stringi = input()
stringi2 = ""
norm = False

for i in range(1, len(stringi)):
    if stringi[i] >= 'a' and stringi[i] <= 'z':
        norm = True
        break

if norm == False:
    for i in range(0, len(stringi)):
        if stringi[i] >= 'A' and stringi[i] <= 'Z':
            stringi2 += chr(ord(stringi[i]) + 32)
        else:
            stringi2 += chr(ord(stringi[i]) - 32)

if norm:
    print(stringi)
else:
    print(stringi2)


