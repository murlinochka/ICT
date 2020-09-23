import math
n = int(input())

a = [i**2 for i in range(1, int(math.sqrt(n))+1) if 1**2<n]
print(' '.join(map(str, a)))