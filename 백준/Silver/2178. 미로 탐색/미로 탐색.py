import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

miro = [list(input().rstrip()) for _ in range(N)]

queue = deque()
queue.append((0, 0))
miro[0][0] = 1

while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if miro[ny][nx] == '1':
                miro[ny][nx] = miro[y][x] + 1
                queue.append((ny, nx))

print(miro[N-1][M-1])