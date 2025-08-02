import sys
from collections import defaultdict
import heapq


input = sys.stdin.readline


N = int(input())

num_plus = []
num_minus = []
num_zero = []

for i in range(N):
    n = int(input())
    if n > 0:
        heapq.heappush(num_plus, (-n, n))
    elif n == 0:
        num_zero.append(n)
    else:
        heapq.heappush(num_minus, n)

total = 0

for i in range(len(num_plus) // 2):
    num1 = heapq.heappop(num_plus)
    num2 = heapq.heappop(num_plus)
    
    if num1[1] == 1 or num2[1] == 1:
        total += num1[1] + num2[1]
    else:
        total += num1[1] * num2[1]
    
for i in range(len(num_minus) // 2):
    num1 = heapq.heappop(num_minus)
    num2 = heapq.heappop(num_minus)
    
    total += num1 * num2

if num_minus and num_zero:
    num_minus[0] = 0
if num_plus:
    num_plus[0] = num_plus[0][1]
    
total += sum(num_minus) + sum(num_plus)

print(total)