words = [[0 for i in range(15)] for j in range(5)]

for i in range(5):
    row = list(input())
    for j in range(len(row)):
        words[i][j] = row[j]

for i in range(15):
    for j in range(5):
        if words[j][i] != 0:
            print(words[j][i], end="")