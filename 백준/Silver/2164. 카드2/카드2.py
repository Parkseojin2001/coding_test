import sys
from collections import deque

N = int(sys.stdin.readline())

cards = deque(range(1, N + 1))

p = 0
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])