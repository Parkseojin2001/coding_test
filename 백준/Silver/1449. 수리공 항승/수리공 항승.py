import sys

input = sys.stdin.readline

N, L = map(int, input().split())
leak_points = list(map(int, input().split()))

leak_points.sort()

start = 0
end = 0
cnt = 0

for leak_point in leak_points:
    if end == 0:
        start = leak_point - 0.5
        end = start + L
        cnt += 1
    elif leak_point >= end:
        start = leak_point - 0.5
        end = start + L
        cnt += 1
        

print(cnt)