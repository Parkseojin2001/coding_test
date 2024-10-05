N, M = map(int, input().split())

blanks = [i + 1 for i in range(N)]

for i in range(M):
    i, j = map(int, input().split())
    
    i = i - 1
    j = j - 1
    blanks[i: j + 1] = reversed(blanks[i:j+1])

print(" ".join(map(str, blanks)))