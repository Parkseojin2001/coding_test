import sys
from collections import Counter


input = sys.stdin.readline

T = int(input())

for i in range(T):
    day = int(input())
    price = list(map(int, input().split()))
    
    profit = 0
    max_price = 0
    
    for i in range(len(price) - 1, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        else:
            profit += max_price - price[i]
    
    
    print(profit)