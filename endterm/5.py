n = int(input())
ans = 1
for i in range(2, n):

    if (n %i==0):
         ans += 1

print (ans)


# Input
# The input consists of a single line containing a positive integer n  — the number of employees in Fafa's company.

# Output
# Print a single integer representing the answer to the problem.

# Examples
# input
# 2
# output
# 1