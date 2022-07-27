from collections import deque

n, s, d, f, b, k = map(int, input().split())
if k: police = set(map(int, input().split()))
else: police = set()

queue = deque([s])
visit = [-1] * (n+1); visit[s] = 0

while queue:
    x = queue.popleft()

    if x+f <= n and visit[x+f] == -1 and not x+f in police:
        visit[x+f] = visit[x]+1
        queue.append(x+f)
    if 0 < x-b and visit[x-b] == -1 and not x-b in police:
        visit[x-b] = visit[x]+1
        queue.append(x-b)

    if visit[d] != -1:
        print(visit[d])
        exit(0)

print('BUG FOUND')