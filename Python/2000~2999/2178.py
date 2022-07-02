from sys import stdin
from collections import deque
input = stdin.readline

N, M = map(int, input().split()); lst = []; apt = []

for i in range(N):
    lst.append([int(i) for i in list(input().rstrip())])

dirx = (-1, 1, 0, 0); diry = (0, 0, -1, 1)

def BFS(a, b):
    queue = deque([[a, b]])
    lst[a][b] = 2

    while queue:
        x, y = queue.popleft()

        if x == N-1 and y == M-1:
            return
        
        for i in range(4):
            nx = x+dirx[i]; ny = y+diry[i]
            if 0 <= nx < N and 0 <= ny < M and lst[nx][ny] == 1:
                lst[nx][ny] = lst[x][y] + 1
                queue.append([nx, ny])

BFS(0, 0)
print(lst[-1][-1] - 1)