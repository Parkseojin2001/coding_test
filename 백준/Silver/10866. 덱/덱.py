# Authored by : 21011645
# https://www.acmicpc.net/problem/10866

import sys
from collections import deque
input = sys.stdin.readline

deq = deque()

for _ in range(int(input())):
    command = input().split()
    
    if command[0] == 'push_front':
        deq.appendleft(command[1])
    elif command[0] == 'push_back':
        deq.append(command[1])
    elif command[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)