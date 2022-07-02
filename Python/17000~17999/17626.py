n = int(input())
dp = [0]
sq = []

for i in range(1, n+1):
    if i ** 0.5 == i // (i ** 0.5):
        sq.append(i)
        dp.append(1)
    else:
        m = 5
        for k in sq:
            if dp[i-k] < m:
                m = dp[i-k]
        dp.append(m+1)

print(dp[n])