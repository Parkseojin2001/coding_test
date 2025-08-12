def solution(emergency):
    answer = []
    sort_emergency = sorted(emergency, reverse=True)
    
    for i, e in enumerate(emergency):
        answer.append(sort_emergency.index(e) + 1)
        
    return answer