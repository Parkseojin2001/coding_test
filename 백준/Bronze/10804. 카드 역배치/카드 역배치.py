import sys

input = sys.stdin.readline


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(start: int, end: int, arr: list[int]) -> None:
    head = arr[0:start]
    part = arr[start : end + 1]
    part = part[::-1]
    tail = arr[end + 1 :]

    return head + part + tail


def main() -> None:
    lines = [i for i in range(1, 21)]
    for _ in range(10):
        start, end = map(int, sys_input().split())
        lines = solve(start - 1, end - 1, lines)
    print(*lines)


if __name__ == "__main__":
    main()