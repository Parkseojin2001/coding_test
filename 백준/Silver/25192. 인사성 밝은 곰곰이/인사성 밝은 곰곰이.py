import sys

input = sys.stdin.readline

N = int(input())
member = set()

cnt = 0

for _ in range(N):
    message = input().strip()
    if message != "ENTER":
        member.add(message)
    else:
        cnt += len(member)
        member.clear()

cnt += len(member)
print(cnt)