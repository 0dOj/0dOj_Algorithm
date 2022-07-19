p = {0:2, 1:3, 2:5, 3:7, 4:11}

arr = tuple(map(int, input().split()))
dp = {4:0}

t = (2, 3, 5, 7, 11)

for i in arr:
    if i == 0:
        break

    dp_next = {}

    for k in dp:
        for d in range(5):
            if k%t[d] == 0 and k//t[d]*p[i] != p[i]**2:
                if k//t[d]*p[i] in dp_next:
                    dp_next[k//t[d]*p[i]] = min(dp_next[k//t[d]*p[i]], dp[k]+(2 if d == 0 else 1 if i == d else 4 if i == d-2 or i == d+2 else 3))
                else:
                    dp_next[k//t[d]*p[i]] = dp[k]+(2 if d == 0 else 1 if i == d else 4 if i == d-2 or i == d+2 else 3)
    
    dp = dp_next

print(min(dp.values()))