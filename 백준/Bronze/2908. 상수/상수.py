A, B = map(str, input().split())

A = reversed(list(A))

B = reversed(list(B))

A = "".join(A)
B = "".join(B)

if int(A) > int(B):
    print(A)
else:
    print(B)