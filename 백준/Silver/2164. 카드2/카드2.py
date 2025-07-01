import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

cards = [card for card in range(1, N + 1)]

deque_cards = deque(cards)

p = 0
while len(deque_cards) > 1:
    deque_cards.popleft()
    card = deque_cards.popleft()
    deque_cards.append(card)

print(deque_cards[0])