N, M = map(int, input().split())

string_set = set()

for _ in range(N):
    voca = input()
    string_set.add(voca)

count = 0
for _ in range(M):
    new = input()
    if new in string_set:
        count += 1
        
print(count)
    