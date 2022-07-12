from sys import stdin

input = stdin.readline

r, c, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

purifyer_up = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == -1:
            if not purifyer_up:
                purifyer_up = (i, j, 1)
            else:
                purifyer_down = (i, j, -1)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def diffuse():
    global arr
    next_arr = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if arr[x][y]:
                if arr[x][y] == -1:
                    next_arr[x][y] = -1
                else:
                    cnt = 0
                    for i in range(4):
                        nx = x+dx[i]; ny = y+dy[i]
                        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                            next_arr[nx][ny] += arr[x][y] // 5
                            cnt += 1
                    next_arr[x][y] += arr[x][y] - arr[x][y] // 5 * cnt

    arr = next_arr

def purify():
    global purifyer_up
    global purifyer_down

    for px, y, m in (purifyer_up, purifyer_down):
        x = px - 1 * m
        while x != 0 and x != r-1:
            nx = x - 1 * m
            arr[x][y] = arr[nx][y]
            x = nx
        while y != c-1:
            ny = y + 1
            arr[x][y] = arr[x][ny]
            y = ny
        while x != px:
            nx = x + 1 * m
            arr[x][y] = arr[nx][y]
            x = nx
        while y != 1:
            ny = y - 1
            arr[x][y] = arr[x][ny]
            y = ny
        arr[px][y] = 0

for _ in range(t):
    diffuse()
    purify()

sm = 0
for i in range(r):
    sm += sum(arr[i])
print(sm + 2)