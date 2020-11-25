n=int(input())

ans = 0
bns = 0
cns = 0

for i in range(n):
    a,b,c=map(int,input().split())
    ans += a
    bns += b
    cns += c

if(ans==0 and bns==0 and cns==0):
    print("YES")
else:
    print("NO")


# Input
# The first line contains a positive integer n (1 ≤ n ≤ 100), then follow n lines containing three integers each: the xi coordinate, the yi coordinate and the zi coordinate of the force vector, applied to the body.

# Output
# Print the word "YES" if the body is in equilibrium, or the word "NO" if it is not.

# Examples
# input
# 3
# 4 1 7
# -2 4 -1
# 1 -5 -3
# output
# NO
# input
# 3
# 3 -1 7
# -5 2 -4
# 2 -1 -3
# output
# YES