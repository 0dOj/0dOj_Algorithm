n, s = map(int, input().split())
arr = tuple(map(int, input().split()))

i = -1
j = -1
sm = 0
mn = 100001

while True:
    if sm < s:
        j += 1
        if j == n:
            break
        sm += arr[j]
    if sm >= s:
        mn = min(mn, j-i)
        i += 1
        sm -= arr[i]

print(0 if mn == 100001 else mn)