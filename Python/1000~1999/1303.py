from collections import deque

m, n = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

w = 0
b = 0

for i in range(n):
    for j in range(m):
        if not visit[i][j]:

            queue = deque([[i, j]])
            visit[i][j] = True
            c = arr[i][j]
            cnt = 1

            while queue:
                x, y = queue.popleft()

                for k in range(4):
                    nx = x+dx[k]; ny = y+dy[k]
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == c and not visit[nx][ny]:
                        visit[nx][ny] = True
                        queue.append([nx, ny])
                        cnt += 1

            if c == 'W':
                w += cnt ** 2
            else:
                b += cnt ** 2

print(w, b)