def solution(price, money, count):
    answer = 0
    for n in range(1, count + 1):
        answer += (price * n)

    if money > answer:
        return 0
    return answer - money