dx = (1, -1, -1, 0, 1, 0, 1, -1)
dy = (-1, -1, 0, -1, 0, 1, 1, 1)

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

cnt = 0

for x in range(n):
    for y in range(m):
        if arr[x][y] == '#':
            for i in range(6) if x%2 == 0 else range(2, 8):
                nx = x+dx[i]; ny = y+dy[i]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '.':
                    cnt += 1
print(cnt)