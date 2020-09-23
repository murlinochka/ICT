n = int(input())
i = 0
a = []
while n>=2**i:
    a.append(2**i)
    i += 1
print(' '.join(map(str, a)))