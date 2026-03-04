import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def stars(n: int) -> str:
    top = [" " * i + "*" * (2 * (n - i) - 1) for i in range(0, n)]
    bottom = [" " * (n - i - 1) + "*" * (2 * i + 1) for i in range(1, n)]
    return top + bottom


def main() -> None:
    N = int(sys_input())

    answer: list[str] = stars(N)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
