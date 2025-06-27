a, b, c, d, e, f = map(int, input().split())

D = a * e - b * d
Dx = c * e - b * f
Dy = a * f - c * d

x = Dx / D
y = Dy / D
print(int(x), int(y))