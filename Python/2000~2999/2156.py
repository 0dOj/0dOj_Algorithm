from sys import stdin
input = stdin.readline

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

if n < 2:
    print(sum(arr))
    exit(0)

dp = [0, arr[1], arr[1]+arr[2]]

for i in range(3, n+1):
    dp.append(max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i], dp[i-1]-arr[i-2]+arr[i]))

print(max(dp[n-1], dp[n]))