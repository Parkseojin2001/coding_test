number = input()

numbers = number.split()

total = 0

for num in numbers:
    total += int(num)

print(total)