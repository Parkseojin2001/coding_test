import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, heights: list[int]) -> str:
    stack = []
    receivers = ["0"] * n

    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] < heights[i]:
            prev_idx = stack.pop()
            receivers[prev_idx] = str(i + 1)
        stack.append(i)

    return " ".join(receivers)


def main() -> None:
    N = int(sys_input())

    raser = list(map(int, sys_input().split()))

    answer: str = solve(N, raser)

    print(answer)


if __name__ == "__main__":
    main()
