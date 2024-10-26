N, B = map(str, input().split())

B = int(B)
num = 0

for i in range(len(N)):
    if 'A' <= N[i] and N[i] <= 'Z':
        n = 10 + ord(N[i]) - ord('A')
    else:
        n = int(N[i])

    num += pow(B, len(N) - 1 - i) * n
    
print(num)