import sys         


input = sys.stdin.readline

N = int(input())
cnt = 0

temp = set([N])

while 1 not in temp:
    t = set()
    for n in list(temp):
        if n % 2 == 0:
            t.add(n // 2)
        if n % 3 == 0:
            t.add(n // 3)
        
        t.add(n - 1)
    cnt += 1
    
    temp = t

print(cnt)