def solution(d, budget):
    answer = 0
    d.sort()
    
    for part in d:
        if budget >= part:
            budget -= part
            answer += 1
        else:
            break
    
    
    return answer