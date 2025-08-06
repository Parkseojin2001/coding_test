import sys
import heapq


input = sys.stdin.readline

N = int(input())

line = list(map(int, input().split()))

result = [0] * N

for i in range(N):
    cnt = 0
    j = 0
    while cnt <= line[i]:
        if result[j] == 0:
            cnt += 1
        j += 1
    result[j - 1] = i + 1


for k in result:
    print(k, end=" ")