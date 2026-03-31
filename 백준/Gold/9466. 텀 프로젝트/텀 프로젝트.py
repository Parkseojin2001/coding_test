import sys
from collections import deque

def sys_input() -> None:
    return sys.stdin.readline().rstrip()

def bfs(choice: list[int], visited: list[bool], start: int) -> int:
    queue = deque([start])
    visited[start] = True
    visit_path = [start]

    while queue:
        x = queue.popleft()
        nx = choice[x]
        if visited[nx]:
            if nx in visit_path:
                cycle_start = visit_path.index(nx)
                visit_path = visit_path[:cycle_start]
            break
        visited[nx] = True
        queue.append(nx)
        visit_path.append(nx)
    return len(visit_path)

def solve(n: int, choice: list[int]) -> int:
    visited = [False] * n
    no_team_cnt = 0
    for student in range(n):
        if not visited[student]:
            no_team_cnt += bfs(choice, visited, student)
    return no_team_cnt
        


def main() -> None:
    T = int(sys_input())
    for _ in range(T):
        n = int(sys_input())
        choice = [int(x) - 1 for x in sys_input().split()]

        answer: int = solve(n, choice)
        print(answer)


if __name__ == '__main__':
    main()
