from collections import deque
from sys import stdin

input = stdin.readline

n, m, k = map(int, input().split())
arr = tuple(tuple(map(int, tuple(input().rstrip()))) for _ in range(n))

visit = [[[-1] * m for _ in range(n)] for _ in range(2)]
visit[1][0][0] = k

queue = deque([(0, 0, 1)])

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

while queue:
    x, y, t = queue.popleft()
    if x == n-1 and y == m-1:
        print(t)
        exit(0)

    for i in range(4):
        nx = x+dx[i]; ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and (t%2 or not arr[nx][ny]):
            if visit[t%2][x][y] - arr[nx][ny] > visit[(t+1)%2][nx][ny]:
                visit[(t+1)%2][nx][ny] = visit[t%2][x][y] - arr[nx][ny]
                queue.append((nx, ny, t+1))
    if visit[t%2][x][y] > visit[(t+1)%2][x][y]:
        visit[(t+1)%2][x][y] = visit[t%2][x][y]
        queue.append((x, y, t+1))

print(-1)