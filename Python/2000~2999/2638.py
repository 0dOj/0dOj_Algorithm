from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

flag = True
cnt = 0

while flag:
    queue = deque([[0, 0]])
    visit = [[0]*m for _ in range(n)]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]; ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] != 2:
                if arr[nx][ny] == 1:
                    visit[nx][ny] += 1
                else:
                    visit[nx][ny] += 2
                    queue.append([nx, ny])

    flag = False
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 2:
                arr[i][j] = 0
            else:
                flag = True

    cnt += 1

print(cnt)