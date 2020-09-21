d = int(input("Days: "))
h = int(input("Hours: "))
m = int(input("Minutes: "))
s = int(input("Seconds: "))

sec = (d*24*60*60 + h*60*60 + m*60 + s)

print("Seconds: ", sec)