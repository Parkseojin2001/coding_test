import sys

def recursion(s, left, right):
    global count
    count += 1
    if (left >= right):
        return 1
    elif s[left] != s[right]:
        return 0
    else:
        return recursion(s, left + 1, right - 1)
    


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    S = input().strip()
    count = 0
    is_palindrome = recursion(S, 0, len(S) - 1)
    print(is_palindrome, count)