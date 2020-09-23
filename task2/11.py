n = int(input())
k = 2
i = 3
if (n % 2 == 0): 
    k = 2 

else:
    while(i * i <= n): 
        if (n % i == 0): 
            k = i 
        i += 2
print(k)
  
# This code is contributed by mits 