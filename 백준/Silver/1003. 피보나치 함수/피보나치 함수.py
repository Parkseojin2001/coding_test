import sys         


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0] * (N + 1)
    
    for i in range(N + 1):
        if i == 0:
            dp[i] = (1, 0)
        elif i == 1:
            dp[i] = (0, 1)
        elif i == 2:
            dp[i] = (1, 1)
        else:
            n_0 = 2 * dp[i - 2][0] + dp[i - 3][0]
            n_1 = 2 * dp[i - 2][1] + dp[i - 3][1]
            dp[i] = (n_0, n_1)
    
    print(dp[N][0], dp[N][1])