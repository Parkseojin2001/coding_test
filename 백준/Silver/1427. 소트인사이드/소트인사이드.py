N = int(input())

num_list = []

while N > 0:
    num_list.append(str(N % 10))
    N //= 10

num_list.sort(reverse=True)

print(int(''.join(num_list)))