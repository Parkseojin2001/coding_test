import sys
from collections import deque

deque = deque()

N = int(sys.stdin.readline())

for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "1":
        deque.appendleft(int(order[1]))
    elif order[0] == "2":
        deque.append(int(order[1]))
    elif order[0] == "3":
        num = deque.popleft() if len(deque) > 0 else -1
        print(num)
    elif order[0] == "4":
        num = deque.pop() if len(deque) > 0 else -1
        print(num)
    elif order[0] == "5":
        print(len(deque))
    elif order[0] == "6":
        print(1 if len(deque) == 0 else 0)
    elif order[0] == "7":
        print(deque[0] if len(deque) > 0 else -1)
    elif order[0] == "8":
        print(deque[-1] if len(deque) > 0 else -1)