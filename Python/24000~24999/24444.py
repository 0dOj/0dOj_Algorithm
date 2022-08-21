from sys import stdin
from collections import deque

input = stdin.readline

n, m, r = map(int, input().split())

edge = {i:set() for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    edge[a].add(b)
    edge[b].add(a)

visit = [0] * (n+1)
visit[r] = 1
visit_cnt = 1

queue = deque([r])

while queue:
    x = queue.popleft()

    for nx in sorted(edge[x]):
        if not visit[nx]:
            visit_cnt += 1
            visit[nx] = visit_cnt
            queue.append(nx)

for i in visit[1:]:
    print(i)