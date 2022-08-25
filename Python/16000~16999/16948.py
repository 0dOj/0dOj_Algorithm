from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dx = (-2, -2, 0, 0, 2, 2)
dy = (-1, 1, -2, 2, -1, 1)

visit = [[None] * n for _ in range(n)]
visit[r1][c1] = 0
queue = deque([(r1, c1)])

while queue:
    x, y = queue.popleft()
    if x == r2 and y == c2:
        print(visit[r2][c2])
        exit(0)

    for d in range(6):
        nx = x+dx[d]; ny = y+dy[d]
        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == None:
            visit[nx][ny] = visit[x][y] + 1
            queue.append((nx, ny))
print(-1)