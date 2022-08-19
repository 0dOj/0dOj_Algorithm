from collections import deque
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
table = [arr[i][:] for i in range(n)]

visit = [[False] * m for _ in range(n)]

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visit[i][j]:
            queue = deque([(i, j)])
            visit[i][j] = True
            cnt = 1
            wall_arr = set()

            while queue:
                x, y = queue.popleft()
                
                for k in range(4):
                    nx = x+dx[k]; ny = y+dy[k]
                    if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                        if arr[nx][ny] == 0:
                            visit[nx][ny] = True
                            cnt += 1
                            queue.append((nx, ny))
                        else:
                            wall_arr.add((nx, ny))

            for x, y in wall_arr:
                table[x][y] += cnt
                table[x][y] %= 10

for line in table:
    print(''.join(map(str, line)))