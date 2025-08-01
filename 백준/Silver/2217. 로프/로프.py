import sys

input = sys.stdin.readline

N = int(input())

ropes = []
max_weight = 0

for i in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True)

for i, rope in enumerate(ropes):
    max_weight = max(max_weight, rope * (i + 1))

print(max_weight)