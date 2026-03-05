import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(text: str) -> str:
    left_stack = []
    right_stack = []

    for c in text:
        if c == "<":
            if left_stack:
                right_stack.append(left_stack.pop())
        elif c == ">":
            if right_stack:
                left_stack.append(right_stack.pop())
        elif c == "-":
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(c)

    return "".join(left_stack + list(reversed(right_stack)))


def main() -> None:
    n = int(sys_input())
    for _ in range(n):
        text = sys_input()

        answer: str = solve(text)
        print(answer)


if __name__ == "__main__":
    main()