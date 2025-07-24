def solution(n):
    answer = []
    while n > 0:
        answer.append(str(n % 3))
        n //= 3
        
    num = ''.join(answer)
    num = int(num)
    total = 0
    mul = 1
    while num > 0:
        total += (num % 10) * mul
        mul *= 3
        num //= 10
    return total