from collections import deque

n = int(input())
a, b = map(int, input().split())

edge = {i:set() for i in range(n+1)}

for _ in range(int(input())):
    x, y = map(int, input().split())
    edge[x].add(y)
    edge[y].add(x)

visit = [False] * (n+1)
visit[a] = True
queue = deque([(a, 0)])

while queue:
    x, t = queue.popleft()
    if x == b:
        print(t)
        exit(0)

    for next in edge[x]:
        if not visit[next]:
            visit[next] = True
            queue.append((next, t+1))

print(-1)