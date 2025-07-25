def solution(n, arr1, arr2):
    def change_bit(num, k):
        two_bit = []
        while num > 0:
            two_bit.append('#' if num % 2 == 1 else ' ')
            num //= 2
        if len(two_bit) < k:
            for i in range(k - len(two_bit)):
                two_bit.append(' ')
        return two_bit
    
    matrix_1 = []
    matrix_2 = []
    
    for i in arr1:
        r = change_bit(i, n)
        r.reverse()
        matrix_1.append(r)
    
    for i in arr2:
        r = change_bit(i, n)
        r.reverse()
        matrix_2.append(r)
        
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[i])):
            if matrix_2[i][j] == '#':
                matrix_1[i][j] = '#'
    
    answer = []
    print(matrix_1)
    for a in matrix_1:
        s = ''.join(a)
        answer.append(s)
    
    return answer
            
