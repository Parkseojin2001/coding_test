import sys

input = sys.stdin.readline


N, M = map(int, input().split())

num_list = list(map(int, input().split()))

sum = [0]
tmp = 0

for num in num_list:
    tmp += num
    sum.append(tmp)

for k in range(M):
    i, j = map(int, input().split())
    print(sum[j] - sum[i - 1])