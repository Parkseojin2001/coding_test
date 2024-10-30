N = int(input())


k = 2
arr = []
while N != 1:
    if N % k == 0:
        N  = N // k
        arr.append(k)
    else:
        k += 1

if len(arr) != 0:
    for i in range(len(arr)):
        print(arr[i])