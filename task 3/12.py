n = int(input())
stringi = input()
cnt = 0
itog = 0

for i in range (0, len(stringi)):
    if stringi[i] == 'x':
        cnt += 1
        if cnt >=3:
            itog += 1
    else:
        cnt = 0

print(itog)