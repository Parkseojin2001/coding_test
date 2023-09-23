N = int(input())
student_list = []
for i in range(N):
    kg, cm = map(int, input().split())
    student_list.append((kg, cm))

rank = []

for st1 in student_list:
    rank = 1
    for st2 in student_list:
        if st1[0] < st2[0] and st1[1] < st2[1]:
            rank += 1
    print(f'{rank} ', end = '')