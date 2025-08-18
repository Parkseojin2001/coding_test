import sys
import heapq
from collections import deque
from collections import defaultdict

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        count = 1
        count += dfs(x-1, y)
        count += dfs(x+1, y)
        count += dfs(x, y-1)
        count += dfs(x, y+1)
        return count
    
    return 0

N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int, input().strip())))
    
total = []
cnt = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            size = dfs(i, j)
            total.append(size)
            

total.sort()

print(len(total))
for i in total:
    print(i)