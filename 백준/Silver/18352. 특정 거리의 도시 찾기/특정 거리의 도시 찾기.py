import sys
import heapq
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def bfs(graph, start, visited, cnt):
    queue = deque([(start, 0)])
    visited[start] = True
    vertex = []
    
    while queue:
        u, w = queue.popleft()
        if w == cnt:
                vertex.append(u)
        for i in graph[u]:
            if not visited[i]:
                queue.append((i, w + 1))
                visited[i] = True
                
    return vertex
                


N, M, K, X = map(int, input().split())

graph = defaultdict(list)
visited = [False] * (N + 1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    

city = bfs(graph, X, visited, K)

if len(city) == 0:
    print(-1)
else:
    city.sort()
    for c in city:
        print(c)