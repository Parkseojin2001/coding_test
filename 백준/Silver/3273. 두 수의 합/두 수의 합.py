import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(x: int, nums: list[int]) -> int:
    rest = set()
    cnt = 0

    for num in nums:
        if num in rest:
            cnt += 1
            rest.remove(num)
        else:
            rest.add(x - num)

    return cnt


def main() -> None:
    n = int(sys_input())
    nums = list(map(int, sys_input().split()))
    x = int(sys_input())

    answer: int = solve(x, nums)
    print(answer)


if __name__ == "__main__":
    main()