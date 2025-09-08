import sys

N = int(sys.stdin.readline())
cnt = 0

if N % 5 == 0:
    cnt = N // 5
else:
    if N % 5 == 4 or N % 5 == 1:
        cnt += N // 5
        if cnt > 0:
            cnt -= 1
            remain = N - 5 * cnt
            cnt += remain // 3
        else:
            cnt = -1
    elif N % 5 == 3:
        cnt += N // 5
        cnt += 1
    elif N % 5 == 2:
        cnt += N // 5
        if cnt > 1:
            cnt -= 2
            remain = N - 5 * cnt
            cnt += remain // 3
        else:
            cnt = -1
print(cnt)