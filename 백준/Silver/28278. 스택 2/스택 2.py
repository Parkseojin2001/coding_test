import sys


N = int(input())

stack = []

for _ in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == "1":
        stack.append(int(order[1]))
        
    elif order[0] == "2":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == "3":
        print(len(stack))
    elif order[0] == "4":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "5":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])