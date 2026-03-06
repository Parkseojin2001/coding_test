import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, numbers: list[int]) -> str:
    stack = []
    nge = ["-1"] * n

    for idx, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            prev_idx = stack.pop()
            nge[prev_idx] = str(num)
        stack.append(idx)

    return " ".join(nge)


def main() -> None:
    N = int(sys_input())
    numbers = list(map(int, sys_input().split()))

    answer: str = solve(N, numbers)
    print(answer)


if __name__ == "__main__":
    main()