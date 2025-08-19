import sys
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(graph, v, visited):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v
            dfs(graph, i, visited)

N = int(input())

graph = defaultdict(list)

for i in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (N + 1)

dfs(graph, 1, visited)

for i in range(2, N + 1):
    print(visited[i])