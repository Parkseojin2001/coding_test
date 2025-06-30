def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

A_1, B_1 = map(int, input().split())
A_2, B_2 = map(int, input().split())

result = B_1 * B_2 / gcd(min(B_1, B_2), max(B_1, B_2))  

A_1 = A_1 * result / B_1
A_2 = A_2 * result / B_2

up = A_1 + A_2

k = gcd(min(up, result), max(up, result))

print(int(up / k), int(result/ k))