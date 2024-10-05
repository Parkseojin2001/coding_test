NM = list(map(int, input().split()))

N = NM[0]
M = NM[1]

blank = [i + 1 for i in range(N + 1)]

for i in range(M):
    ij = list(map(int, input().split()))
    i = ij[0] - 1
    j = ij[1] - 1
    tmp = blank[i]
    blank[i] = blank[j]
    blank[j] = tmp
    
for i in range(N):
    print(f"{blank[i]} ", end="")