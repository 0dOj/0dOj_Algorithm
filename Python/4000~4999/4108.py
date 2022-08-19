dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, 1, 1, 1, 0, -1, -1, -1)

while True:
    r, c = map(int, input().split())
    if r == 0:
        break
    
    arr = [input() for _ in range(r)]

    table = []
    for x in range(r):
        table.append('')
        for y in range(c):
            if arr[x][y] == '*':
                table[-1] += '*'
            else:
                cnt = 0
                for i in range(8):
                    nx = x+dx[i]; ny = y+dy[i]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '*':
                        cnt += 1
                table[-1] += str(cnt)
    
    for l in table:
        print(l)