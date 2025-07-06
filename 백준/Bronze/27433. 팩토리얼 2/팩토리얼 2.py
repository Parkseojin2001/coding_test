import sys

def f(N):
    if N == 0:
        return 1
    if N == 1:
        return 1
    return N * f(N - 1)

input = sys.stdin.readline

N = int(input())

print(f(N))