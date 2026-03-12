import sys
from collections import deque

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def bfs(n: int, m: int, ground: list[list[int]], visited: list[list[bool]], start: tuple[int, int]) -> None:
    deq = deque([start])
    visited[start[0]][start[1]] = True

    while deq:
        x, y = deq.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and ground[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                deq.append((nx, ny))


def solve(n: int, m: int, cabbage: list[tuple[int, int]]) -> int:
    ground = [[0] * m for _ in range(n)]
    for x, y in cabbage:
        ground[x][y] = 1
    
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    for x, y in cabbage:
        if visited[x][y] == False:
            bfs(n, m, ground, visited, (x, y))
            cnt += 1
    return cnt

def main() -> None:
    T = int(sys_input())

    for _ in range(T):
        M, N, K = map(int, sys_input().split())

        cabbage = [tuple(map(int, sys_input().split())) for _ in range(K)]
        N, M = M, N

        answer: int = solve(N, M, cabbage)
        print(answer)

if __name__ == "__main__":
    main()