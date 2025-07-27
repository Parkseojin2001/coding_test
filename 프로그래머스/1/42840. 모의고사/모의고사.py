def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    count = [0, 0, 0]
    
    for i, a in enumerate(answers):
        if a == p1[i % len(p1)]:
            count[0] += 1
        
        if a == p2[i % len(p2)]:
            count[1] += 1
        
        if a == p3[i % len(p3)]:
            count[2] += 1
    
    max_count = max(count)
    
    result = []
    
    for i, c in enumerate(count):
        if max_count == c:
            result.append(i + 1)
    
    return result
    
    