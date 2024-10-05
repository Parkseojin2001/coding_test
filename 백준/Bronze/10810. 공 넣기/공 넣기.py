NM = list(map(int, input().split()))

N = NM[0]
M = NM[1]

blank = [0] * N

for i in range(M):
    ijk = list(map(int, input().split()))
    for j in range(ijk[0] - 1, ijk[1]):
        blank[j] = ijk[2]

for i in range(N):
    print(f"{blank[i]} ", end="")
print('\n')