from collections import deque

M, N = map(int, input().split()) # M : 가로줄 개수, N : 세로줄 개수
storage = []
day = 0

for y in range(N): # 가로줄 개수 번 만큼 반복
    line = list(map(int, input().split()))
    storage.append(line)
    
queue = deque([])

for y in range(N): # y = 세로줄 개수 = y 좌표, x = 가로줄 개수 = x 좌표
    for x in range(M):
        if storage[y][x] == 1:
            queue.append([y, x])
    
    
while queue:
    
    y,x = queue[0][0], queue[0][1]
    del queue[0]
    
    if y+1 < N:
        if storage[y+1][x] == 0:
            storage[y+1][x] = storage[y][x] + 1
            queue.append([y+1, x])
    if y-1 >= 0:
        if storage[y-1][x] == 0:
            storage[y-1][x] = storage[y][x] + 1
            queue.append([y-1, x])
    if x+1 < M:
        if storage[y][x+1] == 0:
            storage[y][x+1] = storage[y][x] + 1
            queue.append([y, x+1])
    if x-1 >= 0:
        if storage[y][x-1] == 0:
            storage[y][x-1] = storage[y][x] + 1
            queue.append([y, x-1])
            
day = 0
    
for y in range(N):
    for x in range(M):
        if storage[y][x] == 0:
            print(-1)
            exit(0)
        day = max(day, storage[y][x])
    
print(day-1)