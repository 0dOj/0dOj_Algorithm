from sys import stdin
import heapq

input = stdin.readline

n, m = map(int, input().split())

indegree = [0] * (n+1)
edge = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    indegree[b] += 1

heap = []

for i in range(1, n+1):
    if indegree[i] == 0:
        heap.append(i)

ans = []
while heap:
    x = heapq.heappop(heap)
    ans.append(x)

    for next in edge[x]:
        indegree[next] -= 1
        if indegree[next] == 0:
            heapq.heappush(heap, next)

print(*ans)