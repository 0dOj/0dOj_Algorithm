p, n = map(int, input().split())
arr = sorted(map(int, input().split()))

cnt = 0
for i in arr:
    if p >= 200:
        break
    p += i
    cnt += 1

print(cnt)