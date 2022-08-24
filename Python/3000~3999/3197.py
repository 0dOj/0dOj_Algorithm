from sys import stdin
from collections import deque

input = stdin.readline

r, c = map(int, input().split())
map_arr = tuple(tuple(input().rstrip()) for _ in range(r))
meltTime_arr = [[None] * c for _ in range(r)]

queue = deque([])
ax, ay = None, None; bx, by = None, None
for i in range(r):
    for j in range(c):
        if map_arr[i][j] != 'X':
            meltTime_arr[i][j] = 0
            queue.append((0, i, j))

            if map_arr[i][j] == 'L':
                if ax == None: ax, ay = i, j
                else: bx, by = i, j

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

while queue:
    t, x, y = queue.popleft()

    for d in range(4):
        nx = x+dx[d]; ny = y+dy[d]
        if 0 <= nx < r and 0 <= ny < c and meltTime_arr[nx][ny] == None:
            meltTime_arr[nx][ny] = t+1
            queue.append((t+1, nx, ny))

for i in meltTime_arr:
    print(''.join(map(str, i)))

'''
queue = deque([(0, ax, ay)])
visit = [[False] * c for _ in range(r)]

while queue:
    t, x, y = queue.popleft()
    if x == bx and y == by:
        print(t)
        break

    for d in range(4):
        nx = x+dx[d]; ny = y+dy[d]
        if 0 <= nx < r and 0 <= ny < c and not visit[nx][ny]:
            visit[nx][ny] = True
            if meltTime_arr[nx][ny] > t:
                queue.append((t+1, nx, ny))
            else:
                queue.appendleft((t, nx, ny))
'''