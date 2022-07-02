n, m = map(int, input().split())
if n == 0:
    print(0)
    exit(0)
lst = list(map(int, input().split()))
wei = 0
box = 1
for i in range(n):
    if wei + lst[i] <= m:
        wei += lst[i]
    else:
        wei = lst[i]
        box += 1
print(box)