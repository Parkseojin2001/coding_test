import sys

input = sys.stdin.readline
N = int(input())

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
            


for i in range(N):
    n = int(input())
    while True:
        if n == 0 or n == 1:
            print(2)
            break
        elif is_prime(n):
            print(n)
            break
        else:
            n += 1