import sys
from collections import deque


while True:
    balance = "yes"
    sentence = sys.stdin.readline().rstrip('\n')
    if sentence == '.':
        break
    stack = []
    for word in sentence:
        if word == '(' or word == '[':
            stack.append(word)
        elif word == ')':
            if not stack or stack[-1] != '(':
                balance = 'no'
                break
            stack.pop()
        elif word == ']':
            if not stack or stack[-1] != '[':
                balance = 'no'
                break
            stack.pop()
    if balance == 'yes' and not stack:
        print(balance)
    else:
        print("no")