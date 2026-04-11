import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def back_coord(x: int, y: int, curr_direction: int) -> tuple[int, int]:
    if curr_direction == 0:
        x += 1
    elif curr_direction == 1:
        y -= 1
    elif curr_direction == 2:
        x -= 1
    else:
        y += 1
    
    return x, y

def front_coord(x: int, y: int, curr_direction: int) -> tuple[int, int]:
    if curr_direction == 0:
        x -= 1
    elif curr_direction == 1:
        y += 1
    elif curr_direction == 2:
        x += 1
    else:
        y -= 1
    
    return x, y


def next_direction(curr_direction: int) -> int:
    if curr_direction == 0:
        next_direction = 3
    elif curr_direction == 1:
        next_direction = 0
    elif curr_direction == 2:
        next_direction = 1
    else:
        next_direction = 2
    return next_direction


def solve(curr_x: int, curr_y: int, direction: int, maps: list[list[int]], cnt: list[int]):
    if maps[curr_x][curr_y] == 0:
        cnt[0] += 1
        maps[curr_x][curr_y] = -1
        # 청소되지 않은 빈칸 없는 경우
    if maps[curr_x + 1][curr_y] != 0 and maps[curr_x][curr_y + 1] != 0 and maps[curr_x - 1][curr_y] != 0 and maps[curr_x][curr_y - 1] != 0:
        next_x, next_y = back_coord(curr_x, curr_y, direction)
        if maps[next_x][next_y] == 1:
            return
        else:
            solve(next_x, next_y, direction, maps, cnt)
    # 청소되지 않은 빈칸이 있는 경우
    else:
        for _ in range(4):
            direction = next_direction(direction)
            next_x, next_y = front_coord(curr_x, curr_y, direction)
            if maps[next_x][next_y] == 0:
                solve(next_x, next_y, direction, maps, cnt)
                return

def main() -> None:
    N, M = map(int, sys_input().split())
    x, y, d = map(int, sys_input().split())
    maps = [list(map(int, sys_input().split())) for _ in range(N)]
    count = [0]
    solve(x, y, d, maps, count)

    answer: int = count[0]
    print(answer)

if __name__ == "__main__":
    main()