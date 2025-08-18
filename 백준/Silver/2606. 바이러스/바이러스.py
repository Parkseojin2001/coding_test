import sys
import heapq
from collections import deque
from collections import defaultdict

def bfs(links, start, visited):
    cnt = 0
    queue = deque([start])
    
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        
        for i in links[v]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                queue.append(i)
                
    return cnt
    

links = defaultdict(list)

computer = int(input())

edge = int(input())

visited = [False] * (computer + 1)

for i in range(edge):
    v1, v2 = map(int, input().split())
    links[v1].append(v2)
    links[v2].append(v1)

        
print(bfs(links, 1, visited))