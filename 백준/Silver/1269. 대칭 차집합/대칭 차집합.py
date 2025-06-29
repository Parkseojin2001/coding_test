n, m = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

A_B = A - B
B_A = B - A

result_set = A_B | B_A

print(len(result_set))