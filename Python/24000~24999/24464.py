dp = [1,1,1,1,1]

for i in range(int(input())-1):
    dp = [sum(dp[1:]),dp[0]+dp[3]+dp[4],dp[0]+dp[4],dp[0]+dp[1],dp[0]+dp[1]+dp[2]]
    for i in range(5):
        dp[i] %= 1000000007

print(sum(dp)%1000000007)