from collections import deque

f, s, g, u, d = map(int, input().split())

visit = [-1] * (f+1); visit[s] = 0
queue = deque([s])

while queue:
    x = queue.popleft()
    if x == g:
        print(visit[x])
        exit(0)
    
    if x+u <= f and visit[x+u] == -1:
        visit[x+u] = visit[x]+1
        queue.append(x+u)
    if x-d > 0 and visit[x-d] == -1:
        visit[x-d] = visit[x]+1
        queue.append(x-d)
print("use the stairs")