n = int(input())
arr = tuple(map(int, input().split()))

ans = [0] * n
for i in range(n):
    cnt = arr[i]
    for j in range(n):
        if not ans[j]:
            if cnt:
                cnt -= 1
            else:
                ans[j] = i+1
                break

print(*ans)