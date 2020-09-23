n = int(input())
count = 1
fib0 = 0
fib1 = 1
fibn = 1
while fibn<n:
    fibn = fib0 + fib1
    fib0 = fib1
    fib1 = fibn
    count = count+1
if fibn==n:
    print(count)
else:
    print(-1)