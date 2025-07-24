def solution(s, n):
    password = list(s)
    for i, s in enumerate(password):
        if s == ' ':
            continue
            
        num = (ord(s) + n)
        
        if s >= 'a' and s <= 'z' and num > ord('z'):
            num -= ord('z')
            password[i] = chr(ord('a') + num - 1)
    
        elif s >= 'A' and s <= 'Z' and num > ord('Z'):
            num -= ord('Z')
            password[i] = chr(ord('A') + num - 1)
        else:
            password[i] = chr(num)
        
    return ''.join(password)
        