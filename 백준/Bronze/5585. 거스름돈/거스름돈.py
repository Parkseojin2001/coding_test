import sys

input = sys.stdin.readline

money = int(input())

rest = 1000 - money

cnt = 0
coin = [500, 100, 50, 10, 5, 1]

for c in coin:
    cnt += rest // c
    rest %= c

print(cnt)