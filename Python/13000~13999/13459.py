from collections import deque

n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            redPos = (i, j)
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            bluePos = (i, j)
            arr[i][j] == '.'

def roll(x, y, redPos, bluePos):
    rnx, rny = list(redPos)
    bnx, bny = list(bluePos)

    while arr[bnx+x][bny] != '#' and arr[bnx][bny+y] != '#':
        bnx += x
        bny += y
        if arr[bnx][bny] == 'O':
            return redPos, bluePos
    while arr[rnx+x][rny] != '#' and arr[rnx][rny+y] != '#':
        rnx += x
        rny += y
        if arr[rnx][rny] == 'O':
            print(1)
            exit(0)

    if rnx == bnx and rny == bny:
        if x:
            if redPos[0]*x > bluePos[0]*x:
                bnx -= x
            else:
                rnx -= x
        elif y:
            if redPos[1]*y > bluePos[1]*y:
                bny -= y
            else:
                rny -= y

    return (rnx, rny), (bnx, bny)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

visit = set()
lst = [(redPos, bluePos)]
for i in range(10):
    queue = deque(lst)
    lst = []

    while queue:
        redPos, bluePos = queue.popleft()
        if (redPos, bluePos) in visit:
            continue
        visit.add((redPos, bluePos))

        for i in range(4):
            lst.append(roll(dx[i], dy[i], redPos, bluePos))

print(0)