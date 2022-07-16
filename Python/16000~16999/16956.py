from sys import stdin

input = stdin.readline

r, c = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(r)]

def no():
    print('0')
    exit(0)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'W':
            for k in range(4):
                nx = i+dx[k]; ny = j+dy[k]
                if 0 <= nx < r and 0 <= ny < c:
                    if arr[nx][ny] == '.':
                        arr[nx][ny] = 'D'
                    elif arr[nx][ny] == 'S':
                        no()

print(1)
for i in range(r):
    print(''.join(arr[i]))