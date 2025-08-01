import sys

input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 0

while A < B:
    if B % 2 == 0:
        B //= 2
    elif B % 10 == 1:
        B //= 10
    else:
        cnt = -1
        break
    cnt += 1
    
    
if cnt == -1 or A != B:
    print(-1)
else:
    print(cnt + 1)