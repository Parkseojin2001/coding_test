import sys
from collections import defaultdict
import heapq


input = sys.stdin.readline


S = input().strip()
T = input().strip()

T_list = list(T)

while len(S) < len(T_list):
    if T_list[-1] == 'A':
        T_list.pop()
    else:
        T_list.pop()
        T_list.reverse()

if S == ''.join(T_list):
    print(1)
else:
    print(0)