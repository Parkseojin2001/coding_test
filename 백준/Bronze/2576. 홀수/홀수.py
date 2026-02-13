import sys
input = sys.stdin.readline

min_odd = None
sum_odd = 0

for _ in range(7):
  num = int(input())
  
  if num % 2 == 1:
    sum_odd += num
    if min_odd is None:
      min_odd = num
    else:
      min_odd = min(min_odd, num)

if min_odd is None:
  print(-1)
else:
  print(sum_odd)
  print(min_odd)