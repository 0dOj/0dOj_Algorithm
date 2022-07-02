from sys import stdin
input = stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]; dp[0][0] = 1

for i in range(n):
    for j in range(n):
        d = arr[i][j]
        if i+d < n :
            dp[i+d][j] += dp[i][j]
        if j+d < n :
            dp[i][j+d] += dp[i][j]

print(dp[-1][-1]//4)