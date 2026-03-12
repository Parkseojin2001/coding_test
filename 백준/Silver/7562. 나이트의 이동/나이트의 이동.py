import sys
from collections import deque


DIRECTIONS = [(1, 2), (2, 1), (-1, 2), (-2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]


def sys_input() -> None:
    return sys.stdin.readline().rstrip()

def bfs(l: int, start: tuple[int, int], dest: tuple[int, int]) -> None:
    board = [[-1] * l for _ in range(l)]
    deq = deque([start])
    board[start[0]][start[1]] = 0
    while deq:
        x, y = deq.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == -1:
                board[nx][ny] = board[x][y] + 1
                deq.append((nx, ny))
    
    return board[dest[0]][dest[1]]


def solve(l: int, start: tuple[int, int], dest: tuple[int, int]) -> int:
    return bfs(l, start, dest)

def main() -> None:
    test = int(sys_input())
    for _ in range(test):
        l = int(sys_input())
        start = tuple(map(int, sys_input().split()))
        dest = tuple(map(int, sys_input().split()))

        answer: int = solve(l, start, dest)
        print(answer)

if __name__ == "__main__":
    main()