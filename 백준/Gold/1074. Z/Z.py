import sys

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(n: int, r: int, c: int) -> int:
    if n == 0:
        return 0
    r_region = r // pow(2, n - 1)
    c_region = c // pow(2, n - 1)
    region = 2 * r_region + c_region
    r = r % pow(2, n - 1)
    c = c % pow(2, n - 1)
    return solve(n - 1, r, c) + region * (pow(2, n - 1) * pow(2, n - 1))



def main() -> None:
    N, r, c = map(int, sys_input().split())
    answer: int = solve(N, r, c)
    print(answer)

if __name__ == "__main__":
    main()