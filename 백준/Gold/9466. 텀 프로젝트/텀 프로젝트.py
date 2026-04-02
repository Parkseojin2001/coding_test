import sys

sys.setrecursionlimit(111111)

def sys_input() -> None:
    return sys.stdin.readline().rstrip()

def dfs(n: int, students: list[int], visited: list[bool], cycle: list[int], team_count) -> None:
    visited[n] = True
    cycle.append(n)
    number = students[n]

    if visited[number] == True:
        if number in cycle:
            idx = cycle.index(number)
            team_count[0] += len(cycle) - idx
            
        return
    else:
        dfs(number, students, visited, cycle, team_count)



def main() -> None:
    T = int(sys_input())
    for _ in range(T):
        n = int(sys_input())
        students = [0] + list(map(int, sys_input().split()))

        visited = [False] * (n + 1)
        visited[0] = True
        team_count = [0]

        for i in range(1, n + 1):
            if not visited[i]:
                cycle = []
                dfs(i, students, visited, cycle, team_count)
        
        print(n - team_count[0])

        


if __name__ == '__main__':
    main()

