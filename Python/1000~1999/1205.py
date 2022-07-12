n, s, p = map(int, input().split())
if n == 0:
    print(1)
    exit(0)
lst = list(map(int, input().split()))[:p]

if n+1 > p and s <= lst[-1]:
    print(-1)
    exit(0)

for i in range(min(n, p)):
    if s >= lst[i]:
        print(i+1)
        exit(0)
print(n+1)