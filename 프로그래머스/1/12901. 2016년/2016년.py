def solution(a, b):
    days = 0
    month_31 = set([1, 3, 5, 7, 8, 10, 12])
    month_30 = set([4, 6, 9, 11])
    dic = {0: 'FRI', 1: 'SAT', 2: 'SUN', 3: 'MON', 4: 'TUE', 5: 'WED', 6: 'THU'}
    
    for i in range(1, a):
        if i == 2:
            days += 29
        elif i in month_31:
            days += 31
        elif i in month_30:
            days += 30
    days = days + b - 1
    res = days % 7
    print(days)
    return dic[res]
