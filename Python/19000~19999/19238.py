from sys import stdin
from collections import deque

input = stdin.readline

n, m, f = map(int, input().split())
arr = tuple(tuple(map(int, input().split())) for _ in range(n))
x, y = map(int, input().split()); x -= 1; y -= 1; taxi_pos = (x, y)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

dic = {}
for k in range(m):
    sx, sy, tx, ty = map(int, input().split())
    sx -= 1; sy -= 1; tx -= 1; ty -= 1

    lst = [(sx, sy)]
    visit = [[False] * n for _ in range(n)]; visit[sx][sy] = True
    fuel = 0
    while lst:
        fuel += 1
        queue = deque(lst)
        lst = []

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x+dx[i]; ny = y+dy[i]
                if (nx, ny) == (tx, ty):
                    dic[(sx, sy)] = (tx, ty, fuel)
                    break
                elif 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and arr[nx][ny] != 1:
                    visit[nx][ny] = True
                    lst.append((nx, ny))
        if (sx, sy) in dic:
            break
    if not (sx, sy) in dic:
        print(-1)
        for i in range(m-k-1): input()
        exit(0)

while dic:
    if taxi_pos in dic:
        lst = []
        pas_lst = [taxi_pos]
    else:
        lst = [taxi_pos]
        visit = [[False] * n for _ in range(n)]; visit[taxi_pos[0]][taxi_pos[1]] = True
    while lst:
        f -= 1
        if f < 0:
            print(-1)
            exit(0)
        queue = deque(lst)
        lst = []
        pas_lst = []

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x+dx[i]; ny = y+dy[i]
                if (nx, ny) in dic and not visit[nx][ny]:
                    visit[nx][ny] = True
                    pas_lst.append((nx, ny))
                elif 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and arr[nx][ny] != 1:
                    visit[nx][ny] = True
                    lst.append((nx, ny))
        if pas_lst:
            break
    if pas_lst:
        taxi_pos = min(pas_lst)
        if f >= dic[taxi_pos][2]:
            f += dic[taxi_pos][2]
        else:
            print(-1)
            exit(0)
        next_pos = dic[taxi_pos][:2]
        del dic[taxi_pos]
        taxi_pos = next_pos
    else:
        print(-1)
        exit(0)

print(f)