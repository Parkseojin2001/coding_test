def solution(s):
    dic = {}
    answer = []
    for i, c in enumerate(s):
        if c not in dic.keys():
            dic[c] = i
            answer.append(-1)
        else:
            answer.append(i - dic[c])
            dic[c] = i
        
    
    return answer