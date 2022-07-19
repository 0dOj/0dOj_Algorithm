n = int(input())

arr = sorted(list(map(int, input().split())))

m = 3e9+1
for k in range(n):
    i = 0
    j = n-1
    while True:
        if i == k:
            i += 1
        elif j == k:
            j -= 1
        if i == j:
            break
        s = arr[i]+arr[j]+arr[k]
        if abs(s) < m:
            m = abs(s)
            ans = [arr[i], arr[j], arr[k]]
        if s > 0:
            j -= 1
        elif s < 0:
            i += 1
        else:
            print(*sorted(ans))
            exit(0)

print(*sorted(ans))