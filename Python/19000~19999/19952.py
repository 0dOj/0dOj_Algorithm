from collections import deque
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    h, w, o, f, xs, ys, xe, ye = map(int, input().split())
    
    arr = []
    for _ in range(h):
        arr.append([0] * w)

    for _ in range(o):
        x, y, l = map(int, input().split())
        arr[x-1][y-1] = l
    
    fArr = []
    for _ in range(h):
        fArr.append([0] * w)
    fArr[xs-1][ys-1] = f
    fArr[xe-1][ye-1] = -1

    queue = deque([[xs-1, ys-1, 0, f]])
    xd = (-1, 1, 0, 0); yd = (0, 0, -1, 1)

    while queue:
        x, y, z, of = queue.popleft()

        for i in range(4):
            nx = x+xd[i]; ny = y+yd[i]
            if 0 <= nx < h and 0 <= ny < w and of-1 > fArr[nx][ny]:
                if z >= arr[nx][ny] or arr[nx][ny] - z <= of:
                    fArr[nx][ny] = of-1
                    queue.append([nx, ny, arr[nx][ny], of-1])

    if fArr[xe-1][ye-1] == -1:
        print("인성 문제있어??")
    else:
        print("잘했어!!")