import sys
from collections import defaultdict
from collections import deque
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N, M = map(int, input().split())

labs = []

for i in range(N):
    labs.append(list(map(int, input().split())))

empty = []
virus = deque()

for i in range(N):
    for j in range(M):
        if labs[i][j] == 0:
            empty.append((i, j))
        elif labs[i][j] == 2:
            virus.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

wall_coords = combinations(empty, 3)


def bfs(graph, queue):
    cnt = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))
                
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    
    return cnt
    
space = 0

for wall_1, wall_2, wall_3 in wall_coords:
    lab_copy = [row[:] for row in labs]
    copy_virus = virus.copy()
    
    lab_copy[wall_1[0]][wall_1[1]] = 1
    lab_copy[wall_2[0]][wall_2[1]] = 1
    lab_copy[wall_3[0]][wall_3[1]] = 1
    
    space = max(space, bfs(lab_copy, copy_virus))
            
            
print(space)