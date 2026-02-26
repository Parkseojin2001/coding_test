import sys
from collections import deque

input = sys.stdin.readline
MAX = 100001

N, K = map(int, input().split())

dist = [-1] * MAX


def bfs():
    queue = deque([N])
    dist[N] = 0

    while queue:
        curr = queue.popleft()
        if curr == K:
            return dist[curr]

        for next in (curr - 1, curr + 1, curr * 2):
            if 0 <= next < MAX:
                if dist[next] == -1:
                    dist[next] = dist[curr] + 1
                    queue.append(next)


print(bfs())