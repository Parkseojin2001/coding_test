import sys
from collections import deque

    
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            vx = x + dx[i]
            vy = y + dy[i]
            
            if vx < 0 or vx >= N or vy < 0 or vy >= M:
                continue
            
            if graph[vx][vy] == -1:
                continue
            
            if graph[vx][vy] == 0:
                graph[vx][vy] = 1 + graph[x][y]
                queue.append((vx, vy))
    
M, N = map(int, input().split())
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    graph.append(list(map(int, input().split())))
    
queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs()

day = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            exit()
    day = max(day, max(graph[i]))
        
print(day-1)