def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


N = int(input())

MIN = 1000000000
dis = []
tree_list = []

for _ in range(N):
    tree_list.append(int(input()))

for i in range(len(tree_list) - 1):
    dis.append(tree_list[i+1] - tree_list[i])
    
GCD = dis[0]

for i in range(1, len(dis)):
    GCD = gcd(GCD, dis[i]) 

count = 0

for i in range(len(dis)):
    s = dis[i] // GCD - 1
    count += s
    
print(count)