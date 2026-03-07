import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, nums: list[int]) -> int:
    queue = deque(range(1, n + 1))

    cnt = 0

    for num in nums:
        idx = queue.index(num)

        if idx < n - idx:
            queue.rotate(-idx)
            cnt += idx
        else:
            queue.rotate(n - idx)
            cnt += n - idx

        queue.popleft()
        n -= 1

    return cnt


def main() -> None:
    N, M = map(int, sys_input().split())
    position = deque(map(int, sys_input().split()))

    answer: int = solve(N, position)
    print(answer)


if __name__ == "__main__":
    main()