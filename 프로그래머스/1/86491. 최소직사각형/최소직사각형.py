def solution(sizes):
    answer = 0
    
    for i, card in enumerate(sizes):
        max_len = max(card[0], card[1])
        min_len = min(card[0], card[1])
        sizes[i] = [max_len, min_len]
        
    max_w = 0
    max_h = 0
    
    for card in sizes:
        if max_w < card[0]:
            max_w = card[0]
        if max_h < card[1]:
            max_h = card[1]
    
    return max_h * max_w