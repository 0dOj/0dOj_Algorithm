from sys import stdin

input = stdin.readline

n = int(input())
w = int(input())

dp = {((1, 1), (n, n)): (0, [])}
for _ in range(w):
    dp_next = {}
    nx, ny = map(int, input().split())

    for i1 in dp:
        x1, y1 = i1[0]
        if not ((nx, ny), i1[1]) in dp_next or dp[i1][0] + abs(nx-x1) + abs(ny-y1) < dp_next[((nx, ny), i1[1])][0]:
            dp_next[((nx, ny), i1[1])] = (dp[i1][0] + abs(nx-x1) + abs(ny-y1), dp[i1][1] + [1])
    for i2 in dp:
        x2, y2 = i2[1]
        if not (i2[0], (nx, ny)) in dp_next or dp[i2][0] + abs(nx-x2) + abs(ny-y2) < dp_next[(i2[0], (nx, ny))][0]:
            dp_next[(i2[0], (nx, ny))] = (dp[i2][0] + abs(nx-x2) + abs(ny-y2), dp[i2][1] + [2])

    dp = dp_next

dp_val = list(dp.values())
m = [dp_val[0][0], dp_val[0][1]]
for i in range(1, len(dp_val)):
    if dp_val[i][0] < m[0]:
        m = [dp_val[i][0], dp_val[i][1]]

print(m[0])
for i in range(len(m[1])):
    print(m[1][i])