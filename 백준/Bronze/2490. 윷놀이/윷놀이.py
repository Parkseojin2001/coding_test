import sys
input = sys.stdin.readline

for _ in range(3):
  nums = list(map(int, input().split()))
  if sum(nums) == 0:
    print('D')
  elif sum(nums) == 1:
    print('C')
  elif sum(nums) == 2:
    print('B')
  elif sum(nums) == 3:
    print('A')
  else:
    print('E')