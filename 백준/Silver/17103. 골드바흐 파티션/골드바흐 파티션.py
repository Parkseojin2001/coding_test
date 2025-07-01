def is_prime(n):
    prime_group = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if  prime_group[p] == True:
            for i in range(p * p, n + 1, p):
                prime_group[i] = False
        p += 1
    
    prime_numbers = [p for p in range(2, n + 1) if prime_group[p] == True]
    return prime_numbers
    

T = int(input())

MAX_NUM = 1000000

prime_num = is_prime(MAX_NUM)
prime_set = set(prime_num)

for _ in range(T):
    number = int(input())
    count = 0
    
    for num in prime_num:
        if num > (number // 2):
            break
        if (number - num) in prime_set:
            count += 1
    print(count)