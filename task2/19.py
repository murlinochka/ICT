n = int(input())
a = list(map(int, input().split()))
k = 0
a.sort()

for i in range(n):
    if a[i-1]==a[i]:
        k += 1
print(k) 
