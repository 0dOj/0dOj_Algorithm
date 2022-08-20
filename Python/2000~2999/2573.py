from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

year = 0

while True:
    sub_arr = [[0] * m for _ in range(n)]
    visit = [[False] * m for _ in range(n)]
    checked = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visit[i][j]:
                checked += 1
                if checked == 2:
                    break
                
                queue = deque([(i, j)])
                visit[i][j] = True
                while queue:
                    x, y = queue.popleft()

                    for d in range(4):
                        nx = x+dx[d]; ny = y+dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if arr[nx][ny] and not visit[nx][ny]:
                                visit[nx][ny] = True
                                queue.append((nx, ny))
                            elif not arr[nx][ny]:
                                sub_arr[x][y] += 1

        if checked == 2:
            break
    if checked == 2:
        print(year)
        break
    elif not checked:
        print(0)
        break
        
    for i in range(n):
        for j in range(m):
            if arr[i][j]: arr[i][j] = max(arr[i][j]-sub_arr[i][j], 0)

    year += 1