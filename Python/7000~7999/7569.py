from sys import stdin
from collections import deque
input = stdin.readline

M, N, H = map(int, input().split())

dx = (-1,1,0,0,0,0); dy = (0,0,-1,1,0,0); dz = (0,0,0,0,-1,1)
lst = []
queue = deque([])

for i in range(H):
    lst.append([])
    for j in range(N):
        line = list(map(int, input().split()))
        for k in range(M):
            if line[k] == 1:
                queue.append([k, j, i])
        lst[i].append(line)

def BFS():
    while queue:
        x,y,z = queue.popleft()

        for i in range(6):
            nx = x+dx[i]; ny = y+dy[i]; nz = z+dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and lst[nz][ny][nx] == 0:
                lst[nz][ny][nx] = lst[z][y][x]+1
                queue.append([nx, ny, nz])

    mx = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                d = lst[i][j][k]
                if d == 0:
                    print(-1)
                    exit(0)
                elif d > mx:
                    mx = d

    return mx

print(BFS() - 1)