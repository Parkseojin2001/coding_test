import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def pow(a: int, b: int, c: int) -> int:
    if b == 0:
        return 1
    half = pow(a, b // 2, c)
    half = (half * half) % c
    if b % 2 == 0:
        return half
    return (half * a) % c


def main() -> None:
    A, B, C = map(int, sys_input().split())

    answer: int = pow(A, B, C)
    print(answer)


if __name__ == "__main__":
    main()