import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(a: int, b: int, c: int) -> list[int]:
    num = a * b * c
    cnt_list = [0] * 10
    while num > 0:
        rest = num % 10
        num = num // 10
        cnt_list[rest] += 1

    return cnt_list


def main() -> None:
    A = int(input())
    B = int(input())
    C = int(input())

    answer: list[int] = solve(A, B, C)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()