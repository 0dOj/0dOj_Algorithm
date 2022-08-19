from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

aset = set()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            sx, sy = i, j
        if arr[i][j] > 2:
            aset.add((i, j))
            arr[i][j] = 0

visit = [[False] * m for _ in range(n)]
visit[sx][sy] = True
queue = deque([(sx, sy, 0)])

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

while queue:
    x, y, t = queue.popleft()
    if (x, y) in aset:
        print('TAK')
        print(t)
        exit(0)

    for i in range(4):
        nx = x+dx[i]; ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and not arr[nx][ny]:
            visit[nx][ny] = True
            queue.append((nx, ny, t+1))

print('NIE')