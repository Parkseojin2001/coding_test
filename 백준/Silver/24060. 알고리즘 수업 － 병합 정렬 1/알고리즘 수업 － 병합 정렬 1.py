import sys

def merge_sort(A, p, r, K):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q, K)
        merge_sort(A, q + 1, r, K)
        merge(A, p, q, r, K)

def merge(A, p, q, r, K):
    global k, result
    tmp = []
    i, j = p, q + 1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    for t in range(len(tmp)):
        A[p + t] = tmp[t]
        k += 1
        if K == k:
            result = A[p + t]
            
        
    

input = sys.stdin.readline

A, K = map(int, input().split())

a_list = list(map(int, input().split()))

result = -1
k = 0

merge_sort(a_list, 0, len(a_list) - 1, K)
print(result)