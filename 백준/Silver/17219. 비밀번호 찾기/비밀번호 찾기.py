import sys

N, M = map(int, sys.stdin.readline().split())
dic = {}

for _ in range(N):
    key, value = map(str, sys.stdin.readline().strip().split(' '))
    dic[key] = value

password = []

for _ in range(M):
    site = sys.stdin.readline().strip()
    password.append(dic[site])

for p in password:
    print(p)