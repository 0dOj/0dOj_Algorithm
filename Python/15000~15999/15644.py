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

def roll(d, redPos, bluePos, string):
    if d == 'L':
        x = 0; y = -1
    elif d == 'R':
        x = 0; y = 1
    elif d == 'U':
        x = -1; y = 0
    elif d == 'D':
        x = 1; y = 0

    rnx, rny = list(redPos)
    bnx, bny = list(bluePos)

    while arr[bnx+x][bny] != '#' and arr[bnx][bny+y] != '#':
        bnx += x
        bny += y
        if arr[bnx][bny] == 'O':
            return redPos, bluePos, string
    while arr[rnx+x][rny] != '#' and arr[rnx][rny+y] != '#':
        rnx += x
        rny += y
        if arr[rnx][rny] == 'O':
            global cnt
            print(cnt)
            print(string+d)
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

    return (rnx, rny), (bnx, bny), string+d

d = ('L', 'R', 'U', 'D')

cnt = 0
visit = set()
lst = [(redPos, bluePos, '')]
for i in range(10):
    cnt += 1
    queue = deque(lst)
    lst = []

    while queue:
        redPos, bluePos, string = queue.popleft()
        if (redPos, bluePos) in visit:
            continue
        visit.add((redPos, bluePos))

        for i in range(4):
            lst.append(roll(d[i], redPos, bluePos, string))

print(-1)