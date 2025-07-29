def solution(babbling):
    can_baby = set(["aya", "ye", "woo", "ma"])
    answer = 0
    
    for word in babbling:
        l_word = []
        flag = 0
        while len(word) > 0:
            if word[:3] in can_baby:
                if l_word and l_word[-1] == word[:3]:
                    flag = 1
                l_word.append(word[:3])
                word = word[3:]
            elif word[:2] in can_baby:
                if l_word and l_word[-1] == word[:2]:
                    flag = 1
                l_word.append(word[:2])
                word = word[2:]
            else:
                l_word.append(word)
                break
        if len(set(l_word) - can_baby) == 0 and flag == 0:
                answer += 1
            
            
    return answer