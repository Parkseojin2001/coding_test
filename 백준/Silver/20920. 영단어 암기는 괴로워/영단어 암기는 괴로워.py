import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

dic = defaultdict(lambda: 0)

for _ in range(N):
    voca = input().strip()
    if len(voca) >= M:
        dic[voca] += 1

dic = sorted(dic.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))

for k in dic:
    print(k[0])