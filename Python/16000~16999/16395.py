n, k = map(int, input().split()); n -= 1; k -= 1

dp = [[1]]

for i in range(1, n+1):
    dp.append([1])
    for j in range(i-1):
        dp[i].append(dp[i-1][j]+dp[i-1][j+1])
    dp[i].append(1)

print(dp[n][k])