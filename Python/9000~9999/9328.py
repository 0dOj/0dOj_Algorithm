from sys import stdin
from collections import defaultdict
from collections import deque

input = stdin.readline

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

for T in range(int(input())):
    h, w = map(int, input().split())
    h += 2; w += 2

    arr = [list('.' * w)] + [list('.'+input().rstrip()+'.') for _ in range(h-2)] + [list('.' * w)]

    keys = set(input().rstrip())
    doors = defaultdict(list)
    paper = 0

    visit = [[False] * w for _ in range(h)]
    visit[0][0] = True

    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x+dx[d]; ny = y+dy[d]
            if 0 <= nx < h and 0 <= ny < w and not visit[nx][ny]:
                visit[nx][ny] = True
                if arr[nx][ny] == '.':
                    queue.append((nx, ny))
                elif arr[nx][ny] == '$':
                    queue.append((nx, ny))
                    paper += 1
                elif 97 <= ord(arr[nx][ny]) <= 122:
                    if arr[nx][ny].upper() in doors:
                        for doorX, doorY in doors[arr[nx][ny].upper()]:
                            queue.append((doorX, doorY))
                    keys.add(arr[nx][ny])
                    queue.append((nx, ny))
                elif 65 <= ord(arr[nx][ny]) <= 90:
                    if arr[nx][ny].lower() in keys:
                        queue.append((nx, ny))
                    else:
                        doors[arr[nx][ny]].append((nx, ny))

    print(paper)