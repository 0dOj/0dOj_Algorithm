from collections import deque

k = int(input())
w, h = map(int, input().split())

arr = tuple(tuple(map(int, input().split())) for _ in range(h))
visit = [[[False] * w for _ in range(h)] for _ in range(k+1)]
visit[k][0][0] = True

dx = (-1, 0, 1, 0, -2, -2, -1, 1, 2, 2, -1, 1)
dy = (0, -1, 0, 1, -1, 1, -2, -2, -1, 1, 2, 2)

queue = deque([(0, 0, k, 0)])
while queue:
    x, y, ck, t = queue.popleft()
    if x == h-1 and y == w-1:
        print(t)
        exit(0)

    for i in range(4):
        nx = x+dx[i]; ny = y+dy[i]
        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 0 and not visit[ck][nx][ny]:
            visit[ck][nx][ny] = True
            queue.append((nx, ny, ck, t+1))
    if ck:
        for i in range(4, 12):
            nx = x+dx[i]; ny = y+dy[i]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 0 and not visit[ck-1][nx][ny]:
                visit[ck-1][nx][ny] = True
                queue.append((nx, ny, ck-1, t+1))
    
print(-1)