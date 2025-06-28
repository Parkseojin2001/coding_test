N, M = map(int, input().split())

chess = []
for _ in range(N):
    row = input()
    chess.append(list(row))

def bwbw(n , m):
    w_count = 0
    for i in range(n, n + 8):
        for j in range(m, m + 8):
            if (i + j) % 2 == 0 and chess[i][j] == 'W':
                w_count += 1
            elif (i + j) % 2 == 1 and chess[i][j] == 'B':
                w_count += 1
    return w_count

def wbwb(n, m):
    b_count = 0
    for i in range(n, n + 8):
        for j in range(m, m + 8):
            if (i + j) % 2 == 0 and chess[i][j] == 'B':
                b_count += 1
            elif (i + j) % 2 == 1 and chess[i][j] == 'W':
                b_count += 1
    return b_count

w_count = 250
b_count = 250

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        w_count = min(w_count, bwbw(i, j))
        b_count = min(b_count, wbwb(i, j))
        
print(min(w_count, b_count))