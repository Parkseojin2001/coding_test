import sys


input = sys.stdin.readline

S = input()
change = 0

if S[0] == '0':
    for i in range(len(S) - 1):
        if S[i] == '0' and S[i + 1] == '1':
            change += 1
else:
    for i in range(len(S) - 1):
        if S[i] == '1' and S[i + 1] == '0':
            change += 1
    
    
print(change)