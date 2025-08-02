import sys


input = sys.stdin.readline

N = input().strip()
list_N = list(N)
total = 0

for k in list_N:
    num = int(k)
    total += num

if '0' not in list_N or total % 3 != 0:
    print(-1)
else:
    list_N.sort(reverse=True)
    print(''.join(list_N))