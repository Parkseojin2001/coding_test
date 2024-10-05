N = int(input())

nums = input()

nums = list(map(int, nums.split()))

v = int(input())

count = 0

for i in range(N):
    if v == nums[i]:
        count += 1
        
print(count)