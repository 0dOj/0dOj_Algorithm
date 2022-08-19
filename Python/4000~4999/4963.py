from collections import deque
from sys import stdin

input = stdin.readline

dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, 1, 1, 1, 0, -1, -1, -1)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(bool, map(int, input().split()))) for _ in range(h)]


    land_cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j]:
                land_cnt += 1
                arr[i][j] = False
                queue = deque([(i, j)])
                
                while queue:
                    x, y = queue.popleft()

                    for k in range(8):
                        nx = x+dx[k]; ny = y+dy[k]
                        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny]:
                            arr[nx][ny] = False
                            queue.append((nx, ny))
    
    print(land_cnt)