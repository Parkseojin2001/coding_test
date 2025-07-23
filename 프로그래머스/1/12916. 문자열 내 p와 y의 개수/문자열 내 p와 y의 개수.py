from collections import Counter

def solution(s):
    
    s = s.lower()
    count = Counter(s)
    
    if 'p' in count.keys() and 'y' in count.keys():
        return count['p'] == count['y']
    elif 'p' not in count.keys() and 'y' not in count.keys():
        return True

    return False