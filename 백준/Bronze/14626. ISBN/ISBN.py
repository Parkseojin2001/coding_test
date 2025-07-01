import sys

input = sys.stdin.readline
isbn = input().strip()
star_index = isbn.index('*')

for x in range(10):
    test = isbn[:star_index] + str(x) + isbn[star_index + 1:]
    total = 0
    for i in range(13):
        weight = 1 if i % 2 == 0 else 3
        total += weight * int(test[i])
    if total % 10 == 0:
        print(x)