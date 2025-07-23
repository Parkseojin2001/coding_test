def solution(x):
    total = 0
    y = x
    while y > 0:
        total += (y % 10)
        y //= 10
    return x % total == 0