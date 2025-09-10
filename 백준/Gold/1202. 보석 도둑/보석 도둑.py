import sys
import heapq


input = sys.stdin.readline

N, K = map(int, input().split())

jewels = []
bags = []
max_price = 0

for _ in range(N):
    M, V = map(int, input().split())   
    jewels.append((M, V))

for _ in range(K):
    bags.append(int(input()))
    
bags.sort()
jewels.sort(key=lambda x: x[0])

dummy = []
j = 0

for bag in bags:
    while j < N and jewels[j][0] <= bag:
        heapq.heappush(dummy, -jewels[j][1])
        j += 1
    
    if dummy:
        max_price += -heapq.heappop(dummy)
    
    
print(max_price)