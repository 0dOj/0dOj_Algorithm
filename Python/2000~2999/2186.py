import copy

n, m, k = map(int, input().split())
arr = tuple(tuple(input()) for _ in range(n))
s = input()

dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if s[0] == arr[i][j]:
            dp[i][j] += 1

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

for c in range(1, len(s)):
    dp_next = [[0] * m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if dp[x][y]:
                for i in range(4):
                    for j in range(1, k+1):
                        nx = x+dx[i]*j; ny = y+dy[i]*j
                        if 0 <= nx < n and 0 <= ny < m and s[c] == arr[nx][ny]:
                            dp_next[nx][ny] += dp[x][y]

    dp = copy.deepcopy(dp_next)

cnt = 0
for i in range(n):
    for j in range(m):
        cnt += dp[i][j]

print(cnt)