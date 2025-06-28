N = int(input())

num_list = list(map(int, input().split()))

sorted_list = sorted(num_list)

dic = {}
count = 0

for i in range(N):
    if sorted_list[i] not in dic.keys():
        dic[sorted_list[i]] = count
        count += 1
        
for num in num_list:
    print(dic[num], end=" ")