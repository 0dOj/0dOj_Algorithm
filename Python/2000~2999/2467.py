n = int(input())

arr = sorted(list(map(int, input().split())))

i = 0
j = n-1

m = 2e9+1
ans = [0, 0]
while i != j:
    s = arr[i]+arr[j]
    if abs(s) < m:
        m = abs(s)
        ans = [arr[i], arr[j]]
    if s > 0:
        j -= 1
    elif s < 0:
        i += 1
    else:
        break

print(*sorted(ans))