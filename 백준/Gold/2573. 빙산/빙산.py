import sys
from collections import deque

DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def sys_input() -> None:
    return sys.stdin.readline().rstrip()

def bfs(n: int, m: int, board:list[list[int]], visited: list[list[bool]], start: tuple[int, int],) -> int:
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


def solve(n: int, m: int, board: list[list[int]]) -> int:
    year = 0
    area = 1

    while area > 0:
        melting = [[0] * m for _ in range(n)]
        year += 1

        for x in range(n):
            for y in range(m):
                if board[x][y] == 0:
                    continue
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                        melting[x][y] += 1
        
        # 실제로 빙산 녹이기
        for x in range(n):
            for y in range(m):
                if board[x][y] > 0:
                    height = board[x][y] - melting[x][y]
                    board[x][y] = height if height > 0 else 0

        visited = [[False] * m for _ in range(n)]
        area = 0

        for x in range(n):
            for y in range(m):
                if board[x][y] != 0 and not visited[x][y]:
                    bfs(n, m, board, visited, (x, y))
                    area += 1
        
        if area >= 2:
            break
    
    return year if area > 0 else 0

def main() -> None:
    N, M = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(N)]

    answer: int = solve(N, M, board)
    print(answer)


if __name__ == '__main__':
    main()