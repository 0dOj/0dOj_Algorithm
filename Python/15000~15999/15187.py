from sys import stdin
from collections import defaultdict

input = stdin.readline

n, x = map(int, input().split())

dp = defaultdict(int, {0:1})

for _ in range(n):
    l, c = map(int, input().split())
    lst = sorted(dp.keys(), reverse=True)
    for i in lst:
        for j in range(l*c, 0, -l):
            if i+j <= x:
                dp[i+j] += dp[i]

print(dp[x])