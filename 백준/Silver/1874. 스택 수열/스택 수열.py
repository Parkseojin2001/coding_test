import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
operation = []
make = True

next_push = 1
    

for target in arr:
    
    while next_push <= target:
        stack.append(next_push)
        operation.append('+')
        next_push += 1
    if stack[-1] == target: 
        stack.pop()
        operation.append('-')
    else:
        make = False
        break
if make == False:
    print("NO")
else:
    sys.stdout.write('\n'.join(operation)+'\n')