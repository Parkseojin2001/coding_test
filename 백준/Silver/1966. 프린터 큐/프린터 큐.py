import sys

case = int(sys.stdin.readline())

for _ in range(case):
    N, M = map(int, sys.stdin.readline().split()) # M은 원하는 문서
    queue = list(map(int, sys.stdin.readline().split()))
    
    cnt = 1
    
    while queue:
        best = max(queue)
        
        if queue[0] < best:
            queue.append(queue.pop(0))
        else:
            if M == 0:
                break            
            queue.pop(0)
            cnt += 1
        
        M = M - 1 if M > 0 else len(queue) - 1

    print(cnt)