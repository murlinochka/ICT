stringi = input()
cnt = 1
opasno = False


for i in range (0, len(stringi)):
    if stringi[i] != stringi[len(stringi)-1]:
        if stringi[i]== stringi[i+1]:
            cnt +=1
            if cnt >= 7:
                opasno = True
                break
        else:
            if cnt >=7:
                opasno = True
                break
            cnt = 1

if opasno:
    print("YES")
else:
    print("NO")
