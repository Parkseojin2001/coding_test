import sys
from collections import deque

DIRECTIONS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def bfs(h: int, n: int, m: int, tomatoes: list[list[list[int]]]) -> list[list[list[int]]]:
    starts = [(z, x, y) for z in range(h) for x in range(n) for y in range(m) if tomatoes[z][x][y] == 1]
    deq = deque(starts)
    days = [[[-1] * m for _ in range(n)] for _ in range(h)]

    for z, x, y in starts:
        days[z][x][y] = 0

    while deq:
        z, x, y = deq.popleft()
        for dz, dx, dy in DIRECTIONS:
            nz = z + dz
            nx = x + dx
            ny = y + dy
            
            if not (0 <= nz < h and 0 <= nx < n and 0 <= ny < m):
                continue
            if days[nz][nx][ny] == -1 and tomatoes[nz][nx][ny] == 0:
                days[nz][nx][ny] = days[z][x][y] + 1
                deq.append((nz, nx, ny))
    
    return days


def solve(h: int, n: int, m: int, tomatoes: list[list[list[int]]]) -> int:
    days = bfs(h, n, m, tomatoes)

    min_day = 0

    for z in range(h):
        for x in range(n):
            for y in range(m):
                if days[z][x][y] == -1 and tomatoes[z][x][y] != -1:
                    return -1
                min_day = max(min_day, days[z][x][y])
    
    return min_day

def main() -> None:
    M, N, H = map(int, sys_input().split())
    tomatoes = [[list(map(int, sys_input().split())) for _ in range(N)] for _ in range(H)]
    answer: int = solve(H, N, M, tomatoes)
    print(answer)

if __name__ == "__main__":
    main()