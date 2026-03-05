import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, k: int) -> str:
    nums = []
    circle = deque(range(1, n + 1))

    while circle:
        circle.rotate(-k)
        nums.append(str(circle.pop()))

    return "<" + ", ".join(nums) + ">"


def main() -> None:
    N, K = map(int, sys_input().split())

    answer: str = solve(N, K)
    print(answer)


if __name__ == "__main__":
    main()