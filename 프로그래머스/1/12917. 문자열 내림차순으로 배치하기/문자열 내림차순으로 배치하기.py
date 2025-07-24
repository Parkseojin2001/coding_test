def solution(s):
    small = []
    big = []
    for c in s:
        if c >= 'A' and c <= 'Z':
            big.append(c)
        else:
            small.append(c)
    big.sort(reverse=True)
    small.sort(reverse=True)
    return ''.join(small) + ''.join(big)