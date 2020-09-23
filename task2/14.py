i = int(input())
a = i
k = 0
while(i!=0):
    i = int(input())
    if a<i:
        k = 1
        a = i
    elif a==i:
        k += 1
print(k)