import sys

input = sys.stdin.readline
cnt = 0
end_time = 0

N = int(input())
meetings = []
for i in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

for new_start, new_end in meetings:
    if end_time <= new_start:
        cnt += 1
        end_time = new_end
        
print(cnt)