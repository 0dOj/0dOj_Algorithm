mod = 1000000007
n, k = map(int, input().split())

cnt = 1
for i in range(1, k+1):
  cnt *= (n-i+1)
  cnt //= i

for i in range(k-1):
  cnt *= 2

print(cnt%mod)