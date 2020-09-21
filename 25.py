sec = float(input("Input seconds: "))

d = sec // (24 * 3600)
h = (sec % (24 * 3600)) // 3600
sec %= 3600
m = sec // 60
sec %= 60
seconds = sec
print("%d:%d:%d:%d" % (d, h, m, seconds))
