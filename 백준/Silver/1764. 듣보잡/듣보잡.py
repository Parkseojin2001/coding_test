N, M = map(int, input().split())

n = set()
m = set()

for _ in range(N):
    name = input()
    n.add(name)

for _ in range(M):
    name = input()
    m.add(name)
    
nm = list(n & m)

nm.sort()

print(len(nm))

for name in nm:
    print(name)