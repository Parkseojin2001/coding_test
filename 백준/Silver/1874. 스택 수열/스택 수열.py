import sys

n = int(sys.stdin.readline())

nums = [i for i in range(n, 0, -1)]
stack = []
operation = []

# 수열
arr = []

operation = []
for _ in range(n):
    arr.append(int(input()))
    
make = True
    
for i in range(len(arr)):
    
    while len(stack) == 0 or stack[-1] != arr[i]:
        if len(nums) == 0:
            make = False
            break
        k = nums.pop()
        stack.append(k)
        operation.append('+')
    if stack[-1] == arr[i]: 
        stack.pop()
        operation.append('-')

if make == False:
    print("NO")
else:
    for o in operation:
        print(o)