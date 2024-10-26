area = [[0 for i in range(100)] for i in range(100)]

black_paper = int(input())

for i in range(black_paper):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y + 10):
            if area[i][j] == 0:
                area[i][j] = 1

count = 0
for i in range(100):
    for j in range(100):
        if area[i][j] == 1:
            count += 1
            
print(count)