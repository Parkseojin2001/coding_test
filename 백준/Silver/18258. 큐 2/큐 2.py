import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def push(n: int, queue: list[int]) -> None:
    queue.append(n)


def remove(queue: list[int]) -> int:
    if not queue:
        return -1
    return queue.popleft()


def size(queue: list[int]) -> int:
    return len(queue)


def empty(queue: list[int]) -> int:
    if queue:
        return 0
    return 1


def front(queue: list[int]) -> int:
    if not queue:
        return -1
    return queue[0]


def back(queue: list[int]) -> int:
    if not queue:
        return -1
    return queue[-1]


def main() -> None:
    N = int(sys_input())
    queue = deque()

    for _ in range(N):
        order = list(sys_input().split())

        if order[0] == "push":
            push(order[1], queue)
        elif order[0] == "pop":
            print(remove(queue))
        elif order[0] == "size":
            print(size(queue))
        elif order[0] == "empty":
            print(empty(queue))
        elif order[0] == "front":
            print(front(queue))
        else:
            print(back(queue))


if __name__ == "__main__":
    main()