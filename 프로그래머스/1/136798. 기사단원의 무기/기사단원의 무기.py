def solution(number, limit, power):
    prime_count = []
    answer = 0
    
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1):
            if j * j == i:
                cnt += 1
            elif i % j == 0:
                cnt += 2
                
        prime_count.append(cnt)
        
    for num in prime_count:
        if num <= limit:
            answer += num
        else:
            answer += power
            
    
    return answer