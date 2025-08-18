import sys
from collections import deque
import sys
sys.setrecursionlimit(10**6)


def bfs(start, target):
    queue = deque([[start, 0]])
    visited = [False] * 100001
    visited[start] = True
    while queue:
        v, cnt = queue.popleft()
        if v == target:
            return cnt
        
        for next in (v - 1, v + 1, v * 2):
            if 0 <= next <= 100000 and not visited[next]:
                visited[next] = True
                queue.append([next, cnt + 1])
        

N, K = map(int, input().split())

print(bfs(N, K))