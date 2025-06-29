from collections import Counter


N = int(input())

cards = list(map(int, input().split()))

counter = Counter(cards)

M = int(input())

nums = list(map(int, input().split()))

for num in nums:
    if num not in counter:
        print("0", end = " ")
    else:
        print(counter[num], end=" ")