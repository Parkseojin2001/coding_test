import sys

input = sys.stdin.readline

N = int(input())

i = 1

while i * (i + 1) <= N * 2:
    i += 1

print(i - 1)