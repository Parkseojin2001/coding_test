def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    correct = 0
    zero_cnt = 0
    for lotto in lottos:
        if lotto in set(win_nums):
            correct += 1
        elif lotto == 0:
            zero_cnt += 1
    
    max_rank = rank[correct + zero_cnt]
    min_cnt = rank[correct]
    
    
    
    return [max_rank, min_cnt]