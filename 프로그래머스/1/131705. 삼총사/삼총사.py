def solution(number):
    number.sort()
    
    count = 0
    for left in range(0, len(number) - 2):
        for mid in range(left + 1, len(number) - 1):
            for right in range(mid + 1, len(number)):
                if number[left] + number[mid] + number[right] == 0:
                    count += 1
    return count