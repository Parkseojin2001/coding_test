N = int(input())
num_list = list(map(int, input().split()))

sorted_unique = sorted(set(num_list))
coord = {num: i for i, num in enumerate(sorted_unique)}

print(' '.join(str(coord[num]) for num in num_list))
