ans = 0 

n, x = map(int, input().split())


for i in range(1, n + 1): 
    if (x % i == 0 and x / i <= n): 
        ans += 1

print(ans)
