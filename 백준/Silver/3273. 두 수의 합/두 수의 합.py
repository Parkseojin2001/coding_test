import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, x: int, nums: list[int]) -> int:
    cnt = 0

    nums.sort()

    p1, p2 = 0, n - 1

    while p1 < p2:
        if nums[p1] + nums[p2] == x:
            cnt += 1
            p1 += 1
            p2 -= 1
        elif nums[p1] + nums[p2] > x:
            p2 -= 1
        else:
            p1 += 1

    return cnt


def main() -> None:
    n = int(sys_input())
    nums = list(map(int, sys_input().split()))
    x = int(sys_input())

    answer: int = solve(n, x, nums)
    print(answer)


if __name__ == "__main__":
    main()