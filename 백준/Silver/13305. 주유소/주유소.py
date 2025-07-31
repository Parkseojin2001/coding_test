import sys         

input = sys.stdin.readline

city = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))



total = 0

for i in range(city - 1):
    min_oil_price = min(oil[:i + 1])
    total += min_oil_price * road[i]

print(total)  