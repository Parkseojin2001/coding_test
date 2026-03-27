import sys
from collections import deque
from math import inf

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def sys_input() -> None:
    return sys.stdin.readline().rstrip()

def bfs_labeling(n: int, board: list[list[int]], land_map: list[list[int]], start: tuple[int, int], label: int) -> None:
    queue = deque([start])
    land_map[start[0]][start[1]] = label

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not land_map[nx][ny] and board[nx][ny] == 1:
                land_map[nx][ny] = label
                queue.append((nx, ny))

def bfs_distance(n: int, land_map: list[list[int]], starts: list[tuple[int, int]]):
    queue = deque(starts)
    dist = [[-1] * n for _ in range(n)]
    for start in starts:
        dist[start[0]][start[1]] = 0

    min_bridge_len = inf

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < n) or land_map[nx][ny] == land_map[x][y]:
                continue
            if land_map[nx][ny] == 0:
                land_map[nx][ny] = land_map[x][y]
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
            else:
                bridge_len = dist[x][y] + dist[nx][ny]
                min_bridge_len = min(bridge_len, min_bridge_len)
    return min_bridge_len


def solve(n: int, board: list[list[int]]) -> int:
    land_map = [[0] * n for _ in range(n)]
    
    land_num = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1 and not land_map[x][y]:
                land_num += 1
                bfs_labeling(n, board, land_map, (x, y), land_num)

    starts = []
    for x in range(n):
        for y in range(n):
            if land_map[x][y] == 0:
                continue
            land_idx = land_map[x][y]
            if all(land_map[x + dx][y + dy] == land_idx 
                    for dx, dy in DIRECTIONS
                    if 0 <= x + dx < n and 0 <= y + dy < n):
                continue
            starts.append((x, y))
    
    return bfs_distance(n, land_map, starts)

                

def main() -> None:
    N = int(sys_input())
    land = [list(map(int, sys_input().split(" "))) for _ in range(N)]

    answer: int = solve(N, land)
    print(answer)


if __name__ == '__main__':
    main()