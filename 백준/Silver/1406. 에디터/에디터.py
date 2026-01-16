import sys
input = sys.stdin.readline

left_stack = list(input().rstrip())
N = len(left_stack)
M = int(input())

right_stack = []

for i in range(M):
    command = input().rstrip().split()
    
    if command[0] == 'L' and len(left_stack) != 0:
        top = left_stack.pop()
        right_stack.append(top)
    elif command[0] == 'D' and len(right_stack) != 0:
        top = right_stack.pop()
        left_stack.append(top)
    elif command[0] == 'B' and len(left_stack) != 0 :
        left_stack.pop()
        
    elif command[0] == 'P':
        left_stack.append(command[1])
        
print(''.join(left_stack) + ''.join(right_stack[::-1]))