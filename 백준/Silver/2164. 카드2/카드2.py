import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> int:
    cards = deque(range(1, n + 1))

    while len(cards) > 1:
        cards.popleft()
        cards.rotate(-1)

    return cards[0]


def main() -> None:
    N = int(sys_input())
    answer: int = solve(N)

    print(answer)


if __name__ == "__main__":
    main()