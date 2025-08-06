import sys
import heapq


input = sys.stdin.readline

n, m = map(int, input().split())

cards = list(map(int, input().split()))
heapq.heapify(cards)

for i in range(m):
    card_1 = heapq.heappop(cards)
    card_2 = heapq.heappop(cards)
    sum_num = card_1 + card_2
    for j in range(2):
        heapq.heappush(cards, sum_num)
    
print(sum(cards))