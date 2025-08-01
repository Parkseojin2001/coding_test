import sys
from collections import defaultdict

input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))
count = defaultdict(int)

temp = 0
cnt = 0

for k in arr:
    temp += k
    remainder = temp % M
    count[remainder] += 1

for r in count.keys():
    c = count[r]
    cnt += c * (c - 1) // 2
    if r == 0:
        cnt += c
            
print(cnt)