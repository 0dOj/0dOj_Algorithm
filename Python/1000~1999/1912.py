n = int(input())
arr = tuple(map(int, input().split()))

dp = [arr[0]]
for i in range(1, n):
    dp.append(max(0, dp[i-1])+arr[i])
print(max(dp))