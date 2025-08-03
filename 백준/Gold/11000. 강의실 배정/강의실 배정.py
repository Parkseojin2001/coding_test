import sys
from collections import defaultdict
import heapq


input = sys.stdin.readline


N = int(input())

class_time = []

for i in range(N):
    S, T = map(int, input().split())
    
    class_time.append((S, T))

class_time.sort(key=lambda x: (x[0], x[1]))

room = 0
end = 0
time = []
max_class = 0

for c in class_time:
    if time and time[0] <= c[0]:
        heapq.heappop(time)
    
    heapq.heappush(time, c[1])
    max_class = max(max_class, len(time))

print(max_class)