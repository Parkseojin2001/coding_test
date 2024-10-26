col = 0
row = 0
maximum = 0

matrix = [list(map(int, input().split())) for i in range(9)]

for i in range(9):
    for j in range(9):
        if maximum <= matrix[i][j]:
            maximum = matrix[i][j]
            col = j + 1
            row = i + 1
        
print(maximum)
print(f"{row} {col}")