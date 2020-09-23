a = list(map(int, input().split()))
n = a[0]
k = a[1]
while True:
    b = input()
    if b:
        a.append(list(map(int, b)))
    else:
        break