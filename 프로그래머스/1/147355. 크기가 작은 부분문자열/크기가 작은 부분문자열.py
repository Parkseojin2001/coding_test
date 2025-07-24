def solution(t, p):
    answer = 0
    nums = []
    for i in range(len(t) - len(p) + 1):
        nums.append(t[i: i + len(p)])
    for num in nums:
        if int(p) >= int(num):
            answer += 1
    return answer