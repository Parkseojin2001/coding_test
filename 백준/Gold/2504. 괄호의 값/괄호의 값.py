import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(target_str: str) -> int:
    stack = []
    pairs = {")": ("(", 2), "]": ("[", 3)}

    for c in target_str:
        if c in "([":
            stack.append(c)

        else:
            if c not in pairs:
                return 0

            to_be_sum = 0
            while stack and isinstance(stack[-1], int):
                to_be_sum += stack.pop()
            c_open, val = pairs[c]

            if not stack or stack[-1] != c_open:
                return 0

            stack.pop()

            stack.append(val if not to_be_sum else val * to_be_sum)

    if any(isinstance(v, str) for v in stack):
        return 0

    return sum(stack)


def main() -> None:
    target_str = sys_input()
    answer: int = solve(target_str)
    print(answer)


if __name__ == "__main__":
    main()