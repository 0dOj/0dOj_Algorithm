n = int(input())
arr = list(map(int, input().split()))

dp = []
for i in range(n):
    mx = arr[i]
    for j in range(i):
        if arr[i] > arr[j]:
            mx = max(mx, dp[j]+arr[i])
    dp.append(mx)

print(max(dp))