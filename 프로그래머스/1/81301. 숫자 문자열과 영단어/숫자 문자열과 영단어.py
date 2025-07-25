def solution(s):
    number = {'zero': '0',
              'one': '1',
              'two': '2',
              'three': '3',
              'four': '4',
              'five': '5',
              'six': '6',
              'seven': '7',
              'eight': '8',
              'nine': '9'}
    
    nums = []
    
    temp = []
    
    for c in s:
        if c >= '0' and c <= '9':
            nums.append(c)
        else:
            temp.append(c)
        if ''.join(temp) in number.keys():
            nums.append(number[''.join(temp)])
            temp = []
            
    answer = int(''.join(nums))
    
    return answer