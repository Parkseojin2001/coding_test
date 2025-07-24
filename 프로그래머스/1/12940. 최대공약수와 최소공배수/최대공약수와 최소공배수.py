def solution(n, m):
    answer = [1, 1]
    min_num = min(n, m)
    max_num = max(n, m)
    
    for i in range(1, min_num + 1):
        if n % i == 0 and m % i == 0:
            answer[0] = i
    for j in range(max_num, min_num * max_num + 1):
        if j % n == 0 and j % m == 0:

            answer[1] = j
            break

    return answer