import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(k: int) -> int:
    stack = []

    for _ in range(k):
        n = int(sys_input())

        if n == 0:
            stack.pop()
        else:
            stack.append(n)

    return sum(stack)


def main() -> None:
    K = int(sys_input())

    answer: int = solve(K)
    print(answer)


if __name__ == "__main__":
    main()