import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> int:
    cnt = [0] * 10
    while n > 0:
        rest = n % 10
        n = n // 10
        cnt[rest] += 1
    cnt[6] += cnt[9]
    cnt[9] = 0
    if cnt[6] % 2 == 0:
        cnt[6] = cnt[6] // 2
    else:
        cnt[6] = cnt[6] // 2 + 1
    return max(cnt)


def main() -> None:
    N = int(input())

    answer: int = solve(N)
    print(answer)


if __name__ == "__main__":
    main()