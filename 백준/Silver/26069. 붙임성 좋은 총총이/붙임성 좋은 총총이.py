import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
dance = set()

for _ in range(N):
    A, B = input().rstrip().split(" ")
    if A == "ChongChong" or B == "ChongChong":
        dance.add("ChongChong")
    if A in dance:
        dance.add(B)
    elif B in dance:
        dance.add(A)

print(len(dance))