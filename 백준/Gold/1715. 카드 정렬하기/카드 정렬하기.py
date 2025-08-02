import sys
import heapq

input = sys.stdin.readline


N = int(input())
groups = []

for i in range(N):
    heapq.heappush(groups, int(input()))

total = []

while len(groups) > 1:
    min_1 = heapq.heappop(groups)
    min_2 = heapq.heappop(groups)
    new = min_1 + min_2
    total.append(new)
    heapq.heappush(groups, new)

print(sum(total))