x = {}
y = {}
for i in range(3):
    a, b = map(int, input().split())
    if a not in x:
        x[a] = 0
    x[a] += 1
    if b not in y:
        y[b] = 0
    y[b] += 1
    
for i in x.keys():
    if x[i] == 1:
        print(i, end=' ')
for i in y.keys():
    if y[i] == 1:
        print(i, end=' ')