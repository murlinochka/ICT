n = int(input())
a = list(map(int, input().split()))
x = a[n-1]

for i in range(n-1,0,-1):
    a[i] = a[i-1]
a[0] = x  

print(' '.join(map(str, a)))