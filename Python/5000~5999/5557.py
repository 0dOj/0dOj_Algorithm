n = int(input())
arr = tuple(map(int, input().split()))

dp = [[0] * 21 for _ in range(n-1)]; dp[0][arr[0]] = 1

for k in range(n-2):
    for i in range(21):
        for j in (i+arr[k+1], i-arr[k+1]):
            if 0 <= j <= 20:
                dp[k+1][j] += dp[k][i]

print(dp[-1][arr[-1]])