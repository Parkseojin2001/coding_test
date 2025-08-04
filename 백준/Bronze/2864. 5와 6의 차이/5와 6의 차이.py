import sys

input = sys.stdin.readline

A, B = map(int, input().split())

min_num , max_num = 0, 0

i = 1

while A > 0:
    if A % 10 == 5:
        max_num += 6 * i
        min_num += 5 * i
    elif A % 10 == 6:
        min_num += 5 * i
        max_num += 6 * i
    else:
        min_num += (A%10) * i
        max_num += (A%10) * i
    i *= 10
    A //= 10

i = 1
while B > 0:
    if B % 10 == 5:
        max_num += 6 * i
        min_num += 5 * i
    elif B % 10 == 6:
        min_num += 5 * i
        max_num += 6 * i
    else:
        min_num += (B % 10) * i
        max_num += (B % 10) * i
        
    i *= 10
    B //= 10
    
print(min_num, max_num)