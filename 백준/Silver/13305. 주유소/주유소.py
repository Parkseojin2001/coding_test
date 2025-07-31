import sys      

input = sys.stdin.readline

city = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))



total = 0
min_oil = oil[0]

for i in range(city - 1):
    if oil[i] < min_oil:
        min_oil = oil[i]
    total += min_oil * road[i]

print(total)  