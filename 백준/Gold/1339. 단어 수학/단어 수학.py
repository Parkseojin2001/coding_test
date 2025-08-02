import sys
from collections import defaultdict


input = sys.stdin.readline


N = int(input())
dic = defaultdict(int)
max_len = 0

for i in range(N):
    s = input().strip()
    list_s = list(s)
    for i, k in enumerate(list_s):
        dic[k] += 10 ** (len(s) - i - 1)

sort_dic = sorted(dic.items(), reverse=True, key=lambda x: x[1])
    
num = 9
total = 0

for key in sort_dic:
    total += num * key[1]
    num -= 1

print(total)