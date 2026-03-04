import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def stars(n: int) -> str:
    return [" " * i + "*" * (2 * (n - i) - 1) for i in range(n)]


def main() -> None:
    N = int(sys_input())

    answer: list[str] = stars(N)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()