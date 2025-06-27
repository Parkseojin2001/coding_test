N = int(input())

max_x = -10000
max_y = -10000
min_x = 10000
min_y = 10000

for i in range(1, N + 1):
    x, y = map(int, input().split())
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y
    

if N == 1:
    print(0)
else:
    print((max_x - min_x) * (max_y - min_y))