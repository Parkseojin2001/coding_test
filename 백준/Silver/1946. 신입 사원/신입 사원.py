import sys
from collections import Counter


input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    cnt = 1
    scores = []
    
    for i in range(N):
        s1, s2 = map(int, input().split())
        
        scores.append((s1, s2))
        
    scores.sort(key=lambda x: x[0])
    
    score_2 = [y for x, y in scores]
    min_score = score_2[0]
    
    for i in range(1, len(scores)):
        if min_score > score_2[i]:
            cnt += 1
            min_score = score_2[i]

    print(cnt)