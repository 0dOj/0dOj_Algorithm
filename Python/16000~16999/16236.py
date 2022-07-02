from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0
            xs = i; ys = j

size = 2; exp = 0


queue = deque([[xs, ys]])
queue2 = []
visit = [[False] * n for _ in range(n)]; visit[xs][ys] = True
    
xdir = (-1, 0, 0, 1)
ydir = (0, -1, 1, 0)

time = 0
ansTime = 0

while queue:
    time += 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+xdir[i]; ny = y+ydir[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] <= size and not visit[nx][ny]:
                visit[nx][ny] = True
                queue2.append([nx, ny])

        queue2.sort(reverse=True)

    while queue2:
        x, y = queue2.pop()

        if 1 <= arr[x][y] < size:
            arr[x][y] = 0
            queue = deque([[x, y]])
            queue2 = []
            visit = [[False] * n for _ in range(n)]; visit[x][y] = True
            exp += 1
            if size == exp:
                size += 1
                exp = 0
            ansTime += time
            time = 0
            break
        else:
            queue.append([x, y])

print(ansTime)