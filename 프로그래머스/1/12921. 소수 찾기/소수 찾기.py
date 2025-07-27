def solution(n):
    prime = 0
    numbers = [1 for i in range(n + 1)]
    
    for i in range(2, int(n ** 0.5) + 1):
        if numbers[i] == 1:
            j = 2
            while i * j <= n:
                numbers[i * j] = 0
                j += 1
    
    for i in range(2, len(numbers)):
        if numbers[i] == 1:
            prime += 1
    return prime
            
            