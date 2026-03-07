import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(target: str) -> int:
    stack = []
    cnt = 0
    idx = 0

    while idx < len(target):
        if target[idx : idx + 2] == "()":
            cnt += len(stack)
            idx += 2
        else:
            if target[idx] == "(":
                stack.append(target[idx])
            else:
                stack.pop()
                cnt += 1
            idx += 1

    return cnt


def main() -> None:
    position = sys_input()
    answer: int = solve(position)
    print(answer)


if __name__ == "__main__":
    main()