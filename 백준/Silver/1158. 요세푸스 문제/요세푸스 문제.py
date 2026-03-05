import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, k: int) -> list[str]:
    nums = []
    circle = deque(range(1, n + 1))

    while circle:
        circle.rotate(-k)
        nums.append(str(circle.pop()))

    return nums


def main() -> None:
    N, K = map(int, sys_input().split())

    answer: list[str] = solve(N, K)
    print(f"<{', '.join(answer)}>")


if __name__ == "__main__":
    main()