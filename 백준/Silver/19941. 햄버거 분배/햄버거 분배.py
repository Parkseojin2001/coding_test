import sys
import heapq
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

desk = list(input().strip())

cnt = 0

for i in range(N):
    if desk[i] == 'P':
        for j in range(max(i - K , 0), min(i+K+1, N)):
            if desk[j] == 'H':
                desk[j] = 0
                cnt += 1
                break
    

print(cnt)