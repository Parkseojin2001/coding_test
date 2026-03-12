import sys
from collections import deque

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def fill_flood(board: list[str], is_blind=False) -> int:
    n = len(board)
    m = len(board[0])

    visited = [[False] * m for _ in range(n)]
    cnt = 0

    def bfs(start: tuple[int, int], colors: set[str]) -> None:
        deq = deque([start])
        visited[start[0]][start[1]] = True

        while deq:
            x, y = deq.popleft()

            for dx, dy in DIRECTIONS:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] in colors and not visited[nx][ny]:
                    visited[nx][ny] = True
                    deq.append((nx, ny))

    for x in range(n):
        for y in range(m):
            if not visited[x][y]:
                curr_color = board[x][y]
                if is_blind and curr_color in 'RG':
                    bfs((x, y), {'R', "G"})
                else:
                    bfs((x, y), {curr_color})
                cnt += 1
    return cnt


def solve(board: list[str]) -> tuple[int, int]:
    not_blind = fill_flood(board)
    is_blind = fill_flood(board, is_blind=True)

    return not_blind, is_blind

    

def main() -> None:
    N = int(sys_input())
    board = [sys_input() for _ in range(N)]

    answer: tuple[int, int] = solve(board)

    print(answer[0], answer[1])



if __name__ == "__main__":
    main()