import sys
import heapq
from collections import deque
from collections import defaultdict


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
def bfs(graph, start, visited):
    queue = deque([start])
    
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = defaultdict(list)

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)


for i in range(1, N + 1):
    graph[i] = []

for i in range(M):
    V1, V2 = map(int, input().split())
    graph[V1].append(V2)
    graph[V2].append(V1)
    
for i in range(1, N + 1):
    graph[i].sort()

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)