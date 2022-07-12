n = int(input())

arr = [list(map(int, input().split())) + [1] for _ in range(n)] + [[1] * (n+2)]

dp_0 = [[0] * n for _ in range(n)]; dp_0[0][1] = 1
dp_45 = [[0] * n for _ in range(n)]
dp_90 = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(1, n):
        if not arr[i][j+1]:
            dp_0[i][j+1] += dp_0[i][j] + dp_45[i][j]
            if not arr[i+1][j] and not arr[i+1][j+1]:
                dp_45[i+1][j+1] += dp_0[i][j] + dp_45[i][j] + dp_90[i][j]
        if not arr[i+1][j]:
            dp_90[i+1][j] += dp_45[i][j] + dp_90[i][j]

print(dp_0[-1][-1]+dp_45[-1][-1]+dp_90[-1][-1])