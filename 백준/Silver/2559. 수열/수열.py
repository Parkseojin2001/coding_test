import sys

input = sys.stdin.readline


N, K = map(int, input().split())
temperature = list(map(int, input().split()))

sum = [0]
temp = 0

for t in temperature:
    temp += t
    sum.append(temp)

sum_temp = []

for i in range(N - K + 1):
    sum_temp.append(sum[K + i] - sum[i])

print(max(sum_temp))