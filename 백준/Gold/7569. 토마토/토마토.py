import sys
from collections import defaultdict
from collections import deque
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline



M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()
    
def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if boxes[nz][nx][ny] == 0:
                    boxes[nz][nx][ny] = boxes[z][x][y] + 1
                    queue.append((nz, nx, ny))
                    
                    
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 1:
                queue.append((i, j , k))
                
bfs()

not_complete = False
days = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 0:
                not_complete = True
            days = max(days, boxes[i][j][k])
            
            
if not_complete:
    print(-1)
else:
    print(days - 1)