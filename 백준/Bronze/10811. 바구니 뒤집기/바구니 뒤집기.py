NM = list(map(int, input().split()))

N = NM[0]
M = NM[1]

blanks = [i + 1 for i in range(N)]

for i in range(M):
    ij = list(map(int, input().split()))
    
    i = ij[0] - 1
    j = ij[1] - 1
    if i == 0:
        blanks[i: j + 1] = blanks[j::-1]
    else:
        blanks[i: j + 1] = blanks[j:i-1:-1]

for i in range(N):
    print(f"{blanks[i]} ", end="")