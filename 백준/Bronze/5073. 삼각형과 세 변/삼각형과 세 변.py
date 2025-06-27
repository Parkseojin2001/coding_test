while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    max_side = max(a, b, c)
    if a == b == c:
        print("Equilateral")
    elif max_side == a and b + c > a or \
         max_side == b and a + c > b or \
         max_side == c and a + b > c:
        if a != b and b != c and a != c:
            print("Scalene")
        else:
            print("Isosceles")
    else:
        print("Invalid")