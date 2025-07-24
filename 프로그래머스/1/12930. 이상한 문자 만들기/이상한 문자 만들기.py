def solution(s):
    words = s.split(' ')
    results = []
    
    for word in words:
        temp = []
        for i, value in enumerate(word):
            temp.append(value.upper() if i % 2 == 0 else value.lower())
        
        results.append(''.join(temp))
    return ' '.join(results)
                
            