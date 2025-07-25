from collections import deque
def solution(k, score):
    answer = []
    store = []
    min_score = score[0]
    for num in score:
        if len(store) < k:
            store.append(num)
            min_score = min(min_score, num)
        else:
            if num > min_score:
                store.remove(min_score)
                store.append(num)
                min_score = min(store)
        
        answer.append(min_score)
    return answer