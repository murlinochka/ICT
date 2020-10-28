vowels = ['a', 'o', 'y', 'e', 'i', 'u']

stringi = input().lower()
k = ""

for i in range(0, len(stringi)):
    if stringi[i] not in vowels:
        k += "."
        k += stringi[i]

print (k)
