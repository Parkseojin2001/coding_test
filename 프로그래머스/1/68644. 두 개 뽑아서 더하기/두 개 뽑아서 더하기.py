from itertools import combinations

def solution(numbers):
    answer = set()
    select = combinations(numbers, 2)
    for s in select:
        answer.add(s[0] + s[1])
    
    result = list(answer)
    result.sort()
    return result