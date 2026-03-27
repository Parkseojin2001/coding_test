import sys
from collections import deque

MAX = 1000000

def sys_input() -> None:
    return sys.stdin.readline().rstrip()

def solve(n: int, k: int) -> int:
    queue = deque([n])
    dist = [-1] * (MAX + 1)
    dist[n] = 0

    while queue:
        x = queue.popleft()
        if x == k:
            return dist[x]
        for nx in [2 * x, x - 1, x + 1]:
            if not (0 <= nx < MAX) or dist[nx] != -1:
                continue
            if nx == 2 * x:
                dist[nx] = dist[x]
                queue.appendleft(nx)
            else:
                dist[nx] = dist[x] + 1
                queue.append(nx)

def main() -> None:
    N, K = map(int, sys_input().split())
    answer: int = solve(N, K)
    print(answer)

if __name__ == "__main__":
    main()