from itertools import combinations

def solution(nums):
    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    cnt = 0
    select = combinations(nums, 3)
    
    for s in select:
        result = is_prime(sum(s))
        if result == True:
            cnt += 1
    return cnt
            
            