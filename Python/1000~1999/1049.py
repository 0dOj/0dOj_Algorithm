n, m = map(int, input().split())

pac = one = 1000
for _ in range(m):
    a, b = map(int, input().split())
    pac = min(a, pac); one = min(b, one)

cost = 0
while n:
    buy = min(n, 6)
    cost += min(pac, one*buy)
    n -= buy

print(cost)