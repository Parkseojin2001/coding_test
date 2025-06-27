a, b, c = map(int, input().split())

max_side = max(a, b, c)

if max_side == a and b + c <= a:
    print(b + c + b + c - 1)
elif max_side == b and a + c <= b:
    print(a + c + a + c - 1)
elif max_side == c and a + b <= c:
    print(a + b + a + b - 1)
else:
    print(a + b + c)