import sys
from collections import deque

MONKEY_DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
HORSE_DIRECTIONS = [(1, 2), (2, 1), (1, -2), (2, -1), (-2, 1), (-1, 2), (-1, -2), (-2, -1)]

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def bfs(w: int, h: int, board: list[list[int]], k: int) -> int:
    dist = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]
    queue = deque([(0, 0, 0)])
    dist[0][0][0] = 0
    while queue:
        x, y, used = queue.popleft()
        if x == h - 1 and y == w - 1:
            return dist[x][y][used]
        for dx, dy in MONKEY_DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < h and 0 <= ny < w) or board[nx][ny] == 1:
                continue
            if dist[nx][ny][used] != -1:
                continue
            dist[nx][ny][used] = dist[x][y][used] + 1
            queue.append((nx, ny, used))
        if used < k:
            for dx, dy in HORSE_DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < h and 0 <= ny < w) or board[nx][ny] == 1:
                    continue
                if dist[nx][ny][used + 1] != -1:
                    continue
                dist[nx][ny][used + 1] = dist[x][y][used] + 1
                queue.append((nx, ny, used + 1))
            
    return -1
                

def solve(w: int, h: int, board: list[list[int]], k: int) -> int:
    return bfs(w, h, board, k)
    

def main() -> None:
    K = int(sys_input())
    W, H = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(H)]

    answer: int = solve(W, H, board, K)
    print(answer)


if __name__ == "__main__":
    main()