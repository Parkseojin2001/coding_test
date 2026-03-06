import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, sequence: list[int]) -> str:
    stack = []
    ops = []
    curr = 1

    for c in sequence:
        while curr <= c:
            stack.append(curr)
            ops.append("+")
            curr += 1

        if not (stack and stack[-1] == c):
            return "NO"

        stack.pop()
        ops.append("-")

    return "\n".join(ops)


def main() -> None:
    n = int(sys_input())
    sequence = [int(sys_input()) for _ in range(n)]

    answer: str = solve(n, sequence)
    print(answer)

if __name__ == "__main__":
    main()