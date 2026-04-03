import sys

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(n: int, r: int, c: int) -> int:
    if n == 1:
        if r == 0 and c == 0:
            return 0
        elif r == 0 and c == 1:
            return 1
        elif r == 1 and c == 0:
            return 2
        else:
            return 3
    r_region = r // pow(2, n - 1)
    c_region = c // pow(2, n - 1)
    if r_region == 0 and c_region == 0:
        region = 0
    elif r_region == 0 and c_region == 1:
        region = 1
    elif r_region == 1 and c_region == 0:
        region = 2
    else:
        region = 3
    r = r % pow(2, n - 1)
    c = c % pow(2, n - 1)
    return solve(n - 1, r, c) + region * (pow(2, n - 1) * pow(2, n - 1))



def main() -> None:
    N, r, c = map(int, sys_input().split())
    answer: int = solve(N, r, c)
    print(answer)

if __name__ == "__main__":
    main()