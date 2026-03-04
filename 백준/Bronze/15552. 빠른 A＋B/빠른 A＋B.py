import sys

T = int(sys.stdin.readline())

for i in range(T):
   string = sys.stdin.readline().rstrip()
   nums = list(map(int, string.split()))
   print(nums[0] + nums[1])