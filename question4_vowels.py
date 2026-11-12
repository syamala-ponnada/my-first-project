s = input("enter sting:")
c = 0
for ch in s:
    if ch in "aeiouAEIOU":
        c = c + 1
print("vowels", c)