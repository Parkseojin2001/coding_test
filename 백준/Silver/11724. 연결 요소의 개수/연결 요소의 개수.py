import sys
import heapq
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
cnt = 0
    
for i in range(1, N + 1):
    if visited[i] == False:
        dfs(graph, i, visited)
        cnt += 1
    
print(cnt)