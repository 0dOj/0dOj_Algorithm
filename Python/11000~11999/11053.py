n = int(input())
arr = list(map(int, input().split()))

dp = []
for i in range(n):
    mx = 1
    for j in range(i):
        if arr[j] < arr[i]:
            mx = max(mx, dp[j]+1)
    dp.append(mx)

print(max(dp))