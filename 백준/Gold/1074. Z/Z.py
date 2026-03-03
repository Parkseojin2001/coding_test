import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def z_path(n: int, r: int, c: int) -> int:
    if n == 0:
        return 0

    half = 1 << n - 1
    val = z_path(n - 1, r % half, c % half)
    offset = 2 * (r // half) + (c // half)
    return offset * half * half + val


def main() -> None:
    N, r, c = map(int, sys_input().split())

    answer: int = z_path(N, r, c)
    print(answer)


if __name__ == "__main__":
    main()