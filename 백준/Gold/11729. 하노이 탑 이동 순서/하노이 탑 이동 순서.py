import sys

POLES = {1, 2, 3}

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(src: int, dest: int, n: int, path: list[str]) -> None:
    if n == 0:
        return
    rest = (POLES - {src, dest}).pop()
    solve(src, rest, n - 1, path)
    path.append(f"{src} {dest}")
    solve(rest, dest, n - 1, path)

def hanoi(n: int) -> list[str]:
    path = []
    solve(1, 3, n, path)
    return path

def main() -> None:
    N = int(sys_input())
    answer: list[str] = hanoi(N)

    print(len(answer))
    for k in answer:
        print(k)


if __name__ == "__main__":
    main()