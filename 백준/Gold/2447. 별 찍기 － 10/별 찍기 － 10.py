import sys

def draw_stars(N):
    if N == 1:
        return ["*"]
    stars = draw_stars(N // 3)
    
    L = []
    
    for star in stars:
        L.append(star * 3)
    for star in stars:
        L.append(star + " " * (N//3) + star)
    for star in stars:
        L.append(star * 3)

    return L


input = sys.stdin.readline

N = int(input())

star_list = draw_stars(N)
print("\n".join(star_list))