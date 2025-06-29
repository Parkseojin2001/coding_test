N, M = map(int, input().split())

dic = {}


for i in range(N):
    name = input()
    dic[i + 1] = name
    dic[name] = i + 1

index = set(str(k + 1) for k in range(N))

for _ in range(M):
    select = input()
    if select in index:
        print(dic[int(select)])
    else:
        print(dic[select])