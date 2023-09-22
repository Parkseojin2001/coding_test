N = int(input())

cnt = 0
i = 665

while cnt < N:
    i += 1
    cnt_6 = 0
    j = i
    while j > 1:
        rest = j % 10
        j = j // 10
        if rest == 6:
            cnt_6 += 1
            if cnt_6 == 3:
                break
        else:
            cnt_6 = 0
    if cnt_6 >= 3:
        cnt += 1

print(i)
