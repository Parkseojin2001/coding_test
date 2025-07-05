import sys


N = int(sys.stdin.readline())

number = list(map(int, sys.stdin.readline().split()))

stack = []


state = "Nice"

people = 1

while len(stack) > 0 or len(number) > 0:
    if len(stack) > 0 and people == stack[-1]:
        stack.pop()
        people += 1
    elif people in number:
        while number[0] != people:
            stack.append(number.pop(0))
        number.pop(0)
        people += 1
    else:
        state = "Sad"
        break

print(state)