from sys import stdin
from collections import deque
import math
import heapq

input = stdin.readline
inf = math.inf

def dijk(d):
    while heap:
        cost, node = heapq.heappop(heap)

        if cost > dist[d]:
            break

        if cost > dist[node]:
            continue

        for next in edges[node]:
            c = edges[node][next]+cost
            if c < dist[next]:
                track[next] = {node}
                dist[next] = c
                heapq.heappush(heap, (dist[next], next))
            elif c == dist[next]:
                track[next].add(node)

while True:
    n, m = map(int, input().split())
    if n == 0:
        break

    s, d = map(int, input().split())

    edges = [{} for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        edges[u][v] = p

    track = {s:set([])}

    heap = [(0, s)]
    dist = [inf] * n; dist[s] = 0
    dijk(d)

    if dist[d] == inf:
        print(-1)
        continue

    queue = deque([d])
    visit = [False] * n
    while queue:
        x = queue.popleft()
        if not visit[x]:
            visit[x] = True
            for i in track[x]:
                del edges[i][x]
                queue.append(i)

    heap = [(0, s)]
    dist = [inf] * n; dist[s] = 0
    dijk(d)

    if dist[d] == inf:
        print(-1)
    else:
        print(dist[d])