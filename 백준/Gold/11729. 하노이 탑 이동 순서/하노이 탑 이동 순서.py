import sys

POLES = {1, 2, 3}


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def save_path(src: int, dest: int, n: int, path: list[str]) -> None:
    if n == 0:
        return

    before = (POLES - {src, dest}).pop()
    save_path(src, before, n - 1, path)
    path.append(f"{src} {dest}")
    save_path(before, dest, n - 1, path)


def hanoi(n: int) -> tuple[int, list[str]]:
    path = []
    save_path(1, 3, n, path)
    return len(path), path


def main() -> None:
    N = int(sys_input())

    answer: tuple[int, list[str]] = hanoi(N)
    print(answer[0])
    for p in answer[1]:
        print(p)


if __name__ == "__main__":
    main()
