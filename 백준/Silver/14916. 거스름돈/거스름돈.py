import sys


input = sys.stdin.readline

rest = int(input())
min_coin = float("inf")
tmp = rest

for i in range(rest // 5, -1, -1):
    tmp -= 5 * i
    if tmp % 2 == 0:
        min_coin = i + tmp // 2
        break
    else:
        tmp = rest

if min_coin == float("inf"):
    print(-1)
else:
    print(min_coin)