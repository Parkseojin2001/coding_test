import sys

N, K = map(int, sys.stdin.readline().split())

cnt = 0

coins = []

for _ in range(N):
    coins.append(int(sys.stdin.readline()))

for i in range(N - 1, -1, -1):
    if K // coins[i] > 0:
        cnt += K // coins[i]
        K -= coins[i] * (K // coins[i])

print(cnt)