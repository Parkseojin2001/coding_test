import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

balloon = deque(enumerate(map(int, input().split())))
answer = []

while balloon:
    idx, num = balloon.popleft()
    answer.append(idx + 1)
    
    if num > 0:
        balloon.rotate(-(num - 1))
    else:
        balloon.rotate(-num)

for k in answer:
    print(k, end=" ")