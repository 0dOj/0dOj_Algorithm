from sys import stdin
from collections import deque
input = stdin.readline

N = int(input()); lst = []; apt = []

for i in range(N):
    lst.append([int(i) for i in list(input().rstrip())])

dirx = (-1, 1, 0, 0); diry = (0, 0, -1, 1)

def BFS(a, b):
    queue = deque([[a, b]])
    lst[a][b] = 0
    result = 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dirx[i]; ny = y+diry[i]
            if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == 1:
                lst[nx][ny] = 0
                queue.append([nx, ny])
                result += 1

    return result

for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            apt.append(BFS(i, j))

apt.sort()
print(len(apt))
for i in apt: print(i)