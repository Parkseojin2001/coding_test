import sys

input = sys.stdin.readline


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def main() -> None:
    A, B = map(int, sys_input().split())

    if A > B:
        B, A = A, B

    answer: list = [i for i in range(A + 1, B)]
    print(len(answer))
    print(*answer)


if __name__ == "__main__":
    main()