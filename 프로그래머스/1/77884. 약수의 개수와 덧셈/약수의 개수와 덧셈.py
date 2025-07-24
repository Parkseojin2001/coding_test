def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        count = 0
        for m in range(1, n + 1):
            if n % m == 0:
                count += 1
        if count % 2 == 0:
            answer += n
        else:
            answer -= n
    return answer