n = int(input())


if n == 1:
    length = 4
else:
    length = n + 2 + 4
    n -= 2
    length += 3 * n

print(length)