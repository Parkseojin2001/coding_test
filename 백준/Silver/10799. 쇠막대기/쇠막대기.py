import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(target: str) -> int:
    cnt = 0
    prev = ""
    open_brackets = 0

    for c in target:
        if c == "(":
            open_brackets += 1
        elif c == ")":
            open_brackets -= 1
            if prev == "(":
                cnt += open_brackets
            else:
                cnt += 1
        prev = c
    return cnt


def main() -> None:
    position = sys_input()
    answer: int = solve(position)
    print(answer)


if __name__ == "__main__":
    main()