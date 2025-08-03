import sys
from collections import defaultdict
import heapq

def buy_1(n):
    global money
    money += 3 * stores[n]

def buy_2(n):
    global money
    m = min(stores[n: n + 2])
    stores[n] -= m
    stores[n + 1] -= m
    money += 5 * m

def buy_3(n):
    global money
    m = min(stores[n: n + 3])
    stores[n] -= m
    stores[n + 1] -= m
    stores[n + 2] -= m
    money += 7 * m

input = sys.stdin.readline


N = int(input())

stores = list(map(int, input().split())) + [0, 0]
money = 0


for i in range(len(stores) - 2):
    if stores[i + 1] > stores[i + 2]:
        m = min(stores[i], stores[i + 1] - stores[i + 2])
        stores[i] -= m
        stores[i + 1] -= m
        money += 5 * m
        buy_3(i)
        buy_1(i)
    else:
        buy_3(i)
        buy_2(i)
        buy_1(i)
    
print(money)