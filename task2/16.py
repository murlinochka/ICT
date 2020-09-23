i = int(input())
a = []
count = 0
while i!=0:
    i = int(input())
    a.append(i)
for i in range(len(a)):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        count += 1
print(count)