import sys

def sum_list(L):
    temp = 0
    sum = [0]
    for num in L:
        temp += num
        sum.append(temp)
    
    return sum

input = sys.stdin.readline


N, M = map(int, input().split())
matrix = []

for i in range(N):
    L = list(map(int, input().split()))
    matrix.append(L)
    
dp = [[0] * (N + 1) for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i-1][j-1]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    total = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(total)