dp = [[0] * 1001 for _ in range(1001)]
dp[0][0] = 1; dp[1][1] = 1; dp[2][1] = 1; dp[2][2] = 1

for num in range(3, 1001):
    for num_used in range(1, 1001):
        for i in range(1, 4):
            dp[num][num_used] += dp[num-i][num_used-1]

for T in range(int(input())):
    n, m = map(int, input().split())
    print(dp[n][m]%1000000009)