def solution(my_string):
    answer = []
    
    for s in my_string:
        if s >= '0' and s <= '9':
            answer.append(int(s))
    answer.sort()
    return answer