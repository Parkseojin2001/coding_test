from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

q = deque()

for _ in range(N):
    order = input().split()
    if order[0] == "push_front":
        num = int(order[1])
        q.appendleft(num)
    elif order[0] == "push_back":
        num = int(order[1])
        q.append(num)
    elif order[0] == "pop_front":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif order[0] == "pop_back":
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif order[0] == "size":
        print(len(q))
    elif order[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif order[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q) - 1])