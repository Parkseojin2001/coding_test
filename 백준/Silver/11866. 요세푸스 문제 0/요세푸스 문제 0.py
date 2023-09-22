# 11866
N, K = map(int, input().split())

List = list(range(1, N + 1))

new_list = []
cnt = K - 1

while len(List) > 0:
    num = List.pop(cnt)
    new_list.append(num)
    cnt = cnt + K - 1
    if cnt >= len(List) and len(List) != 0:
        cnt = cnt % len(List)

print('<', end = '')
for i in range(len(new_list) - 1):
    print(new_list[i], end = '')
    print(', ', end = '')

print(new_list[len(new_list) - 1], end = '')
print('>', end = '')