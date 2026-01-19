import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
n, m = map(int, input().split())   # n이 y축 m이 x축

def bfs(arr, y, x):
    size = 0
    while queue:
        k = queue.popleft()
        ny, nx = k[0], k[1]
        size += 1
        for i in range(4):
            if (nx + dx[i] < m and nx + dx[i] >= 0) and (ny + dy[i] < n and ny + dy[i] >= 0):
                if arr[ny + dy[i]][nx + dx[i]] == '1':
                    queue.append((ny + dy[i], nx + dx[i]))
                    arr[ny + dy[i]][nx + dx[i]] = '0'
    return size
    
            

paintings = []
cnt, biggest = 0, 0

for _ in range(n):
    paintings.append(list(input().split()))
    
for i in range(n):
    for j in range(m):
        if paintings[i][j] == '1':  # i 가 y좌표 j 가 x 좌표
            queue.append((i, j)) 
            paintings[i][j] = '0'
            biggest = max(bfs(paintings, i, j), biggest)
            cnt += 1

print(cnt)
print(biggest)