from collections import deque
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

time = 0
visit = [[False] * m for _ in range(n)]
while True:
    cheese_cnt = 0
    flag = False
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                if not visit[i][j]:
                    flag = True
                else:
                    cheese_cnt += 1
                    arr[i][j] = 0
    if not flag:
        print(time)
        print(cheese_cnt)
        break

    time += 1

    queue = deque([(0, 0)])
    visit = [[False] * m for _ in range(n)]; visit[0][0] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]; ny = y+ dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                visit[nx][ny] = True
                if not arr[nx][ny]:
                    queue.append((nx, ny))