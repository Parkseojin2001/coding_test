N = int(input())

cards = set(map(int, input().split()))

M = int(input())

guess = list(map(int, input().split()))

for c in guess:
    if c in cards:
        print("1", end=" ")
    else:
        print("0", end=" ")