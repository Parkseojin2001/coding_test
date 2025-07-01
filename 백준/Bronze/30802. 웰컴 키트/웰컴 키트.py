import sys

input = sys.stdin.readline
N = int(input())

t_shirt= list(map(int, input().split()))

T, P = map(int, input().split())


count_t = 0
for t in t_shirt:
    count_t += t // T
    if t % T != 0:
        count_t += 1
    
count_p = 0

print(count_t)
print(N // P, N - P *(N // P))