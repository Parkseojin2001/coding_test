import sys
from collections import deque

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def fire_bfs(h: int, w: int, map: list[str]) -> list[list[int]]:
    dest = [[-1] * w for _ in range(h)]
    deq = deque()

    for y in range(h):
        for x in range(w):
            if map[y][x] == '*':
                dest[y][x] = 0
                deq.append((x, y))
    while deq:
        x, y = deq.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and dest[ny][nx] == -1 and map[ny][nx] != '#':
                dest[ny][nx] = dest[y][x] + 1
                deq.append((nx, ny))
    return dest

def sanggen_bfs(h: int, w: int, start: tuple[int, int], maps: list[str], fire_dest: list[list[int]]) -> str:
    deq = deque([start])
    dest = [[-1] * w for _ in range(h)]
    dest[start[1]][start[0]] = 0

    while deq:
        x, y = deq.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            nt = dest[y][x] + 1
            if not (0 <= nx < w and 0 <= ny < h):
                return str(nt)
            if  dest[ny][nx] == -1 and maps[ny][nx] != '#':
                if fire_dest[ny][nx] == -1 or fire_dest[ny][nx] > nt:
                    dest[ny][nx] = nt
                    deq.append((nx, ny))
    
    return "IMPOSSIBLE"

def solve(h: int, w: int, maps: list[str]) -> str:
    fire_map = fire_bfs(h, w, maps)

    for y in range(h):
        for x in range(w):
            if maps[y][x] == '@':
                sanggen_start: tuple = (x, y)

    return sanggen_bfs(h, w, sanggen_start, maps, fire_map)


def main() -> None:
    test_case = int(sys_input())
    for _ in range(test_case):
        w, h = map(int, sys_input().split())
        maps = [sys_input() for _ in range(h)]
        answer: str = solve(h, w, maps)
        print(answer)
if __name__ == '__main__':
    main()