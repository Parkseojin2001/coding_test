from collections import Counter

def solution(N, stages):
    present = Counter(stages)
    
    people = [0] * N

    for i in range(1, N + 1):
        for stage in stages:
            if stage >= i:
                people[i - 1] += 1
            
    result = []
    for i in range(1, N + 1):
        if people[i - 1] == 0:
            result.append([i, 0])
        else:
            result.append([i, present[i] / people[i - 1]])
        
    result.sort(reverse = True, key=lambda x: x[1])
    
    answer = []
    
    for r in result:
        answer.append(r[0])
    
    return answer
    
    