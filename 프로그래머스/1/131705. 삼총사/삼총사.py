import itertools

def solution(number):
    count = 0
    comb = itertools.combinations(number, 3)
    for c in comb:
        if sum(c) == 0:
            count += 1
    return count
    