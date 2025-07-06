import sys

def delete_line(n):
    if n == 1:
        return "-"
    
    line_unit = delete_line(n // 3)
    line_res = line_unit + " " * (n // 3) + line_unit
    
    return line_res

input = sys.stdin.readline

while True:
    try:
        N = int(input())
        print(delete_line(3 ** N))
    except:
        break