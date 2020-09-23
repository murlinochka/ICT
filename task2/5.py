a1 = int(input("First column number: "))
b1 = int(input("First line number: "))
a2 = int(input("Second column number: "))
b2 = int(input("Second line number: "))

if((a1-a2==2) or (a1-a2==-2)) and ((b1-b2==1) or (b1-b2==-1)):
    print("YES")
elif((b1-b2==2) or (b1-b2==-2)) and ((a1-a2==1) or (a1-a2==-1)):
    print("YES")
else:
    print ("NO")