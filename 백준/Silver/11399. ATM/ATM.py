import sys

N = int(input())

P = list(map(int, input().split()))

P.sort()

sum_time = 0
total = 0

for time in P:
    sum_time = (sum_time + time)
    total += sum_time
    
print(total)