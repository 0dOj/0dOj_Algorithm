n, m = map(int, input().split())
aarr = tuple(map(int, input().split()))
carr = tuple(map(int, input().split()))

dp = [0] * 10001

for i in range(n):
   a = aarr[i]
   c = carr[i]
   for j in range(10000, c-1, -1):
      dp[j] = max(dp[j], dp[j-c] + a)

for i in range(10001):
   if dp[i] >= m:
      print(i)
      break