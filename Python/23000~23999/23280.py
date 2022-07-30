import math

inf = math.inf

n, a, b = map(int, input().split())
order = tuple(map(lambda x: x-1, map(int, input().split())))

dp = [[[inf] * 12 for _ in range(12)] for _ in range(n+1)]
dp[0][0][2] = 0

for k in range(n):
    o = order[k]
    ox = o // 3; oy = o % 3
    for i in range(12):
        ix = i // 3; iy = i % 3
        for j in range(12):
            jx = j // 3; jy = j % 3
            dp[k+1][o][j] = min(dp[k+1][o][j], dp[k][i][j]+a+abs(ox-ix)+abs(oy-iy))
            dp[k+1][i][o] = min(dp[k+1][i][o], dp[k][i][j]+b+abs(ox-jx)+abs(oy-jy))

mn = inf
for i in range(12):
    for j in range(12):
        mn = min(mn, dp[-1][i][j])
print(mn)