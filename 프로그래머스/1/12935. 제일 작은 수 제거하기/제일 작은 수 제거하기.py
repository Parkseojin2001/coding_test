def solution(arr):
    if len(arr) < 2:
        return [-1]
    min_value = min(arr)
    arr.remove(min_value)
    return arr