from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

n, m = map(int, input().split())
pic = tuple(tuple(map(int, input().split())) for _ in range(n))

v = [[False] * m for _ in range(n)]

pic_cnt = 0
pic_max = 0

for i in range(n):
    for j in range(m):
        if pic[i][j] and not v[i][j]:
            pic_cnt += 1
            v[i][j] = True
            q = deque([(i, j)])
            cnt = 0

            while q:
                cnt += 1
                x, y = q.popleft()

                for d in range(4):
                    nx = x+dx[d]; ny = y+dy[d]
                    if 0 <= nx < n and 0 <= ny < m and pic[nx][ny] and not v[nx][ny]:
                        v[nx][ny] = True
                        q.append((nx, ny))

            pic_max = max(pic_max, cnt)

print(pic_cnt)
print(pic_max)