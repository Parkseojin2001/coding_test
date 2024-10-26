N = int(input())

count = 0


for i in range(N):
    flag = 1
    word = input()
    dic = {}
    for j in range(len(word)):
        if word[j] not in dic.keys():
            dic[word[j]] = j
        else:
            if j != dic[word[j]] + 1:
                flag = 0
                break
            else:
                dic[word[j]] = j
    if flag == 1:
        count += 1
            
    
print(count)