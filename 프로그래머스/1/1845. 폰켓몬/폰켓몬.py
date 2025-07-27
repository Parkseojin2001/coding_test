def solution(nums):
    num_set = set(nums)
    if len(nums) // 2 <= len(num_set):
        return len(nums) // 2
    else:
        return len(num_set)