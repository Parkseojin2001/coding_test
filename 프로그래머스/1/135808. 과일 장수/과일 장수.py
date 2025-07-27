def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    score = score[0: len(score) - (len(score) % m)]
    
    for i in range(0, len(score), m):
        min_score = score[i + m - 1]
        answer += min_score * m
        #print(min_score)
    
    
    return answer
    