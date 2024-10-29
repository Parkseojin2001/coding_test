
N, B = map(int, input().split())

num = []
while N > 0:
    rest = N % B
    N = N // B
    if rest >= 10:
        rest = chr(rest - 10 + ord('A'))
    num.append(str(rest))

result = ''.join(num)
print(result[::-1])