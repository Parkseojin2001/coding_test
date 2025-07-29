def solution(wallet, bill):
    answer = 0
    
    min_w, max_w = min(wallet), max(wallet)
    min_b, max_b = min(bill), max(bill)
    
    while min_w < min_b or max_w < max_b:
        max_b_idx = bill.index(max_b)
        bill[max_b_idx] = max_b // 2
        answer += 1
        min_b, max_b = min(bill), max(bill)
        
    return answer