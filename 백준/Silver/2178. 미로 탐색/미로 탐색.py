import sys
import heapq
from collections import deque
from collections import defaultdict

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            vx = x + dx[i]
            vy = y + dy[i]
            
            if vx < 0 or vx >= N or vy < 0 or vy >= M:
                continue
            if graph[vx][vy] == 0:
                continue
            
            if graph[vx][vy] == 1:
                graph[vx][vy] = graph[x][y] + 1
                queue.append((vx, vy))
                
    return graph[N-1][M-1]
        

N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input().strip())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))