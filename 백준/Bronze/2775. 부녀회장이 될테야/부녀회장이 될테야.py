T = int(input())

for i in range(T):
    k = int(input())    # 층
    n = int(input())     # 호
    f = [x for x in range(1, n + 1)]
    
    for x in range(k):
        people = []
        for y in range(n):
            people.append(sum(f[: y + 1]))
        f = people.copy()
    print(people[-1])