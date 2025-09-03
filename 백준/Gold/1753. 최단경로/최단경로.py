import sys
from collections import defaultdict
from collections import deque
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


V, E = map(int, input().split())
K = int(input())

graph = defaultdict(list)
dist = [float('inf')] * (V + 1)
dist[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        d, u = heapq.heappop(pq)
        if dist[u] < d:
            continue
        
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
        
            
dijkstra(K)

for i in range(1, V + 1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])