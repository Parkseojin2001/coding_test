def solution(x, n):
    answer = []
    original_x = x
    for i in range(n):
        answer.append(x)
        x += original_x
    return answer