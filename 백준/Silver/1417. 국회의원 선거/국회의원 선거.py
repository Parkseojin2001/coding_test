import sys
import heapq


input = sys.stdin.readline

N = int(input())
dasom = int(input())

if N == 1:
    print(0)
else:
    vote = []
    cnt = 0
    
    for i in range(N - 1):
        vote.append(int(input()))
    
    vote.sort(reverse=True)
    
    while vote[0] >= dasom:
        cnt += 1
        dasom += 1
        vote[0] -= 1
        vote.sort(reverse=True)
    
    print(cnt)