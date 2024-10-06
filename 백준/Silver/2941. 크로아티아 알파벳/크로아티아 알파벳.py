alphabet = ["c=", "c-", "dz=", "d-","lj", "nj", "s=", "z="]

words = input()

count = 0

i = 0

while i < len(words):
    if words[i:i + 3] in alphabet:
        count += 1
        i += 3
    elif words[i: i + 2] in alphabet:
        count += 1
        i += 2
    else:
        i+= 1
        count += 1
print(count)