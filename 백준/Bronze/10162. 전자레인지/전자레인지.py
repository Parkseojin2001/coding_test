import sys

input = sys.stdin.readline

T = int(input())

buttons = [300, 60, 10]

cnt = []

for button in buttons:
    cnt.append(T // button)
    T %= button

if T == 0:
    for c in cnt:
        print(c, end=" ")
else:
    print(-1)
    