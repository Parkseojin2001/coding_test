N, K = map(int, input().split())

count = 0
result = -1

for i in range(1, N + 1):
    if N % i == 0:
        count += 1
    if count == K:
        result = i
        break

if result == -1:
    print('0')
else:
    print(result)