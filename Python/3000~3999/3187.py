from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

dx = (-1, 1, 0, 0); dy = (0, 0, -1, 1)

vcnt = 0; kcnt = 0
for i in range(n):
    for j in range(m):
        if not visit[i][j] and arr[i][j] != '#':

            visit[i][j] = True
            queue = deque([[i, j]])
            v = 1 if arr[i][j] == 'v' else 0; k = 1 if arr[i][j] == 'k' else 0

            while queue:
                x, y = queue.popleft()

                for a in range(4):
                    nx = x+dx[a]; ny = y+dy[a]
                    if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and arr[nx][ny] != '#':
                        visit[nx][ny] = True
                        queue.append([nx, ny])
                        if arr[nx][ny] == 'v':
                            v += 1
                        elif arr[nx][ny] == 'k':
                            k += 1
            
            if v >= k:
                vcnt += v
            else:
                kcnt += k
                        
print(kcnt, vcnt)