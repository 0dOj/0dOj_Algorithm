from sys import stdin 
import math
import heapq

input = stdin.readline
inf = math.inf

n = int(input())
m = int(input())

edge = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edge[a].append((b, c))

s, d = map(int, input().split())

dist = [inf] * (n+1); dist[s] = 0
heap = [(0, s)]
track = [0] * (n+1)

while heap:
    cost, node = heapq.heappop(heap)

    if cost > dist[d]:
        break

    if cost > dist[node]:
        continue

    for i in edge[node]:
        if cost+i[1] < dist[i[0]]:
            dist[i[0]] = cost+i[1]
            heapq.heappush(heap, (dist[i[0]], i[0]))
            track[i[0]] = node

ans = [d]
while ans[-1] != s:
    ans.append(track[ans[-1]])

print(dist[d])
print(len(ans))
print(*reversed(ans))