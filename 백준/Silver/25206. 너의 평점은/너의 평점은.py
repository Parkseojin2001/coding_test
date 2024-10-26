total = 0
scores = 0

for i in range(20):
    info = list(map(str, input().split()))
    score = float(info[1])
    grade = info[2]
    if grade == 'A+':
        total += score * 4.5
    elif grade == 'A0':
        total += score * 4.0
    elif grade == 'B+':
        total += score * 3.5
    elif grade == 'B0':
        total += score * 3.0
    elif grade == 'C+':
        total += score * 2.5
    elif grade == 'C0':
        total += score * 2.0
    elif grade == 'D+':
        total += score * 1.5
    elif grade == 'D0':
        total += score * 1.0
    elif grade == 'F':
        total += score * 0.0
    
    if grade == 'P':
        continue
    else:
        scores += score

print(total / scores)