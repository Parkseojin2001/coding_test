from collections import deque
def solution(n, m, section):
    result = 0
    
    section = deque(section)
    
    while section:
        start = section.popleft()
        end = start + m - 1
        result += 1
        
        while section and section[0] <= end:
            section.popleft()
        
        
    return result
