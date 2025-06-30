def is_prime(m, n):
    cnt = 0
    num_list = [1 for x in range(n + 1)]
    p = 2
    while (p * p) <= n:
        if num_list[p] == 1:
            for i in range(p * p, n + 1, p):
                num_list[i] = 0
        p += 1
    
    for i in range(m + 1, n + 1):
        if num_list[i] == 1:
            cnt += 1
    return cnt
    
    
    

while True:
    n = int(input())
    if n == 0:
        break
    count = is_prime(n, 2 * n)
    print(count)