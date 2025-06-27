M = int(input())
N = int(input())

primary_numbers = []

for i in range(M, N + 1):
    if i < 2:
        continue
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime == True:
        primary_numbers.append(i)

if len(primary_numbers) == 0:
    print(-1)
else:
    print(sum(primary_numbers))
    print(primary_numbers[0])