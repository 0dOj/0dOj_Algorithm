from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
lst = []

for _ in range(n):
    p, l = map(int, input().split())
    mil = sorted(list(map(int, input().split())), reverse=True)
    if p >= l:
        lst.append(mil[l-1])
    else:
        lst.append(1)

lst.sort()

ans = 0
for i in lst:
    if i <= m:
        m -= i
        ans += 1
    else:
        break
    
print(ans)