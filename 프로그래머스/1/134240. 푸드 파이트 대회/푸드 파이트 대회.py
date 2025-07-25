def solution(food):
    answer = ''
    cal = 1
    for i in range(1, len(food)):
        if food[i] // 2 > 0:
            answer += str(cal) * (food[i] // 2)
        cal += 1
        
    reverse_answer = list(answer)
    reverse_answer.reverse()
    
    answer += '0'
    answer += ''.join(reverse_answer)
    return answer