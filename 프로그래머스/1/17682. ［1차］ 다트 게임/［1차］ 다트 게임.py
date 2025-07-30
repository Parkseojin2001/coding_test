def solution(dartResult):
    answer = [] 
    length, idx = len(dartResult), 0
    
    while idx < length:
        if dartResult[idx] >= '0' and dartResult[idx] <= '9':
            if dartResult[idx] == '1' and dartResult[idx + 1] == '0':
                num = 10
                idx += 2
            else:
                num = int(dartResult[idx])
                idx += 1
            
            if dartResult[idx] == 'D':
                num = num ** 2
            elif dartResult[idx] == 'T':
                num = num ** 3
                
            answer.append(num)
                
        elif dartResult[idx] == '*':
            answer[-1] *= 2
            if len(answer) >= 2:
                answer[-2] *= 2
        elif dartResult[idx] == '#':
            answer[-1] *= -1
        
        idx += 1
                
        
    return sum(answer)