X = int(input())

line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    x = X
    y = (line + 1) - x
else:
    y = X
    x = (line + 1) - y

print(f"{x}/{y}")