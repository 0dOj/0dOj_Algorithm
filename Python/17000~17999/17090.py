n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(input()))

visit = [[0] * m for _ in range(n)]
cnt = 0
loopSet = set([])
breakSet = set([])
t = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            t += 1
            x, y = i, j
            while True:
                visit[x][y] = t

                if arr[x][y] == 'U':
                    x -= 1
                elif arr[x][y] == 'R':
                    y += 1
                elif arr[x][y] == 'D':
                    x += 1
                elif arr[x][y] == 'L':
                    y -= 1

                if x < 0 or x >= n or y < 0 or y >= m or visit[x][y] in breakSet:
                    breakSet.add(t)
                    break
                elif visit[x][y] == t or visit[x][y] in loopSet:
                    loopSet.add(t)
                    break

for i in range(n):
    for j in range(m):
        if visit[i][j] in breakSet:
            cnt += 1
print(cnt)