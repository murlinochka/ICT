import string

stringi = set(input().lower())
alphabet = set(string.ascii_lowercase)

if len(stringi) >= len(alphabet):
    print("YES")
else:
    print("NO")

