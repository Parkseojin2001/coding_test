import sys
from collections import Counter

input = sys.stdin.readline

name = input().strip()

count = Counter(name).items()

odd = 0

for c in count:
    if c[1] % 2 == 1:
        odd += 1

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    odd_c = ""
    string = []
    for c in count:
        if c[1] % 2 == 1:
            odd_c = c[0]
        string.append(c[0] * (c[1] // 2))
    string.sort()
    string_ = reversed(string)
    
    s1 = "".join(string)
    s2 = "".join(string_)
    
    result = s1 + odd_c + s2
    print(result)