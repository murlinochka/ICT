year = int(input())
n = 1

for i in range(0, 1000):
    year += 1
    tmp = year 
    a = tmp % 10  
    tmp //= 10
    b = tmp % 10
    tmp //= 10
    c = tmp % 10  
    tmp //= 10  
    d = tmp % 10 

    if(a != b and a != c and a != d and b != c and b != d and c != d):

        break
    
print(year)


# Input
# The single line contains integer y (1000 ≤ y ≤ 9000) — the year number.

# Output
# Print a single integer — the minimum year number that is strictly larger than y and all it's digits are distinct. It is guaranteed that the answer exists.

# Examples
# input
# 1987
# output
# 2013
# input
# 2013
# output
# 2014
