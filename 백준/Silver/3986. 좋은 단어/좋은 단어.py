import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(voca: str) -> int:
    stack = []

    for c in voca:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if not stack:
        return 1

    return 0


def main() -> None:
    N = int(sys_input())
    cnt = 0

    for _ in range(N):
        voca = sys_input()
        answer: int = solve(voca)
        cnt += answer

    print(cnt)


if __name__ == "__main__":
    main()