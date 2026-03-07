import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(func: str, list_str: str) -> str:
    deq = deque(list(list_str.split(","))) if list_str else deque()

    reverse_flag = False

    for c in func:
        if c == "R":
            reverse_flag = not reverse_flag
        elif c == "D":
            if not deq:
                return "error"
            if reverse_flag:
                deq.pop()
            else:
                deq.popleft()
    if reverse_flag:
        deq.reverse()
    return "[" + ",".join(deq) + "]"


def main() -> None:
    T = int(sys_input())

    for _ in range(T):
        p = sys_input()
        n = int(sys_input())
        arr = sys_input()[1:-1]

        answer: str = solve(p, arr)
        print(answer)


if __name__ == "__main__":
    main()