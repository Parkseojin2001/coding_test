import sys

input = sys.stdin.readline


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(t: int, n: int, money: int) -> int:
    if t % n == 0:
        return (t // n + 1) * money
    return t // n * money + money


def main() -> None:
    N = int(sys_input())
    calls = list(sys_input().split(" "))

    cost_Y = 0
    cost_M = 0

    for call in calls:
        cost_Y += solve(int(call), 30, 10)
        cost_M += solve(int(call), 60, 15)

    if cost_Y == cost_M:
        print(f"Y M {cost_Y}")
    elif cost_Y > cost_M:
        print(f"M {cost_M}")
    else:
        print(f"Y {cost_Y}")


if __name__ == "__main__":
    main()