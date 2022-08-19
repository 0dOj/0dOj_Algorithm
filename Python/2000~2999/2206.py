from collections import deque

n, m = map(int, input().split())

arr = [input() for _ in range(n)]
visit = tuple(tuple((False) * m for _ in range(n)) for _ in range(2))
visit[1][0][0] = True

queue = deque([(0, 0, 1, 1)])

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

while queue:
    x, y, a, t = queue.popleft()
    if x == n-1 and y == m-1:
        print(t)
        exit(0)

    for i in range(4):
        nx = x+dx[i]; ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == '0' and not visit[a][nx][ny]:
                visit[a][nx][ny] = True
                queue.append((nx, ny, a, t+1))
            if a and not visit[0][nx][ny]:
                visit[0][nx][ny] = True
                queue.append((nx, ny, 0, t+1))

print(-1)