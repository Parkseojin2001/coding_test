import sys
from collections import defaultdict
from collections import deque
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline



N = int(input())

painting = [input().strip() for _ in range(N)]
painting_1 = []
painting_2 = []

for i in range(N):
    painting_1.append(list(painting[i]))
    painting_2.append(list(painting[i].replace('G', 'R')))


normal = [0] * 3
unnormal = [0] * 2

def dfs(paint, x, y, color):
    if x >= N or x <= -1 or y >= N or y <= -1:
        return False
    
    if paint[x][y] == color:
        paint[x][y] = 0
        dfs(paint, x + 1, y, color)
        dfs(paint, x - 1, y, color)
        dfs(paint, x, y - 1, color)
        dfs(paint, x, y + 1, color)
        return True
    
    return False


for i in range(N):
    for j in range(N):
        if dfs(painting_1, i, j, 'R'):
            normal[0] += 1
        if dfs(painting_1, i, j, 'G'):
            normal[1] += 1
        if dfs(painting_1, i, j, 'B'):
            normal[2] += 1
            
for i in range(N):
    for j in range(N):
        if dfs(painting_2, i, j, 'R'):
            unnormal[0] += 1
        if dfs(painting_2, i, j, 'B'):
            unnormal[1] += 1
            
print(sum(normal), sum(unnormal))