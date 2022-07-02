from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(list(input()))
queue = deque([])
cntR = 0; cntG = 0; cntB = 0; cntRG = 0
dirx = (-1,1,0,0); diry = (0,0,-1,1)

def BFS(i, j, c, m):
    queue.append([i, j])
    arr[i][j] = m
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dirx[i]; ny = y+diry[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == c:
                arr[nx][ny] = m
                queue.append([nx, ny])

    

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            BFS(i,j,'R', 'RG')
            cntR += 1
        if arr[i][j] == 'G':
            BFS(i,j,'G', 'RG')
            cntG += 1
            
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'RG':
            BFS(i,j,'RG', False)
            cntRG += 1
        if arr[i][j] == 'B':
            BFS(i,j,'B', False)
            cntB += 1

print(cntR+cntG+cntB, cntRG+cntB)