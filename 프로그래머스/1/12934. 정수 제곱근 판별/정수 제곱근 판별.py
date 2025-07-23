def solution(n):
    answer = int(n ** 0.5)
    if answer * answer == n:
        return (answer + 1) ** 2
    else:
        return -1