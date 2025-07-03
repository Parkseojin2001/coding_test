import sys

S = set()


n = int(sys.stdin.readline())

for _ in range(n):
    temp = sys.stdin.readline().strip().split()
    if len(temp) == 1:
        order = temp[0]
        if order == "all":
            S = set(i for i in range(1, 21))
        elif order == "empty":
            S = set()
    else:
        order, x = temp[0], int(temp[1])
    if order == "add":
        S.add(x)
    elif order == "remove":
        S.discard(x)
    elif order == "check":
        print(1 if x in S else 0)
    elif order == "toggle":
        if x in S:
            S.discard(x)
        else:
            S.add(x)