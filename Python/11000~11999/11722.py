n = int(input())

arr = tuple(map(int, input().split()))
dp = []

for i in range(n):
    mx = 1
    for j in range(i):
        if arr[i] < arr[j]:
            mx = max(mx, dp[j]+1)
    dp.append(mx)

print(max(dp))