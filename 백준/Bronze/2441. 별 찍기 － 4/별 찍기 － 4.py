import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def stars(n: int, m: int) -> str:
    return " " * n + "*" * (m - n)


def main() -> None:
    N = int(sys_input())
    for i in range(0, N):
        print(stars(i, N))


if __name__ == "__main__":
    main()