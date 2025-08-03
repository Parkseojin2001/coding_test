import sys


input = sys.stdin.readline

N, M = map(int, input().split())

set_lines = []
one_lines = []

for i in range(M):
    set, one = map(int, input().split())
    set_lines.append(set)
    one_lines.append(one)
    
if N < 6:
    min_set_lines = min(set_lines)
    min_one_lines = min(one_lines) * N
    print(min(min_one_lines, min_set_lines))
else:
    min_set_line = min(set_lines)
    min_one_line = min(one_lines)
    
    set_money = min_set_line * (N // 6 + 1)
    one_money = min_one_line * N
    
    set_one_money = min_set_line * (N // 6) + min_one_line * (N % 6)

    print(min([set_money, one_money, set_one_money])) 