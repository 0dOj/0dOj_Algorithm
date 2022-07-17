from sys import stdin
from collections import deque

input = stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    time = [0] + list(map(int, input().split()))

    indegree = [0] * (n+1)
    edge = [[] for _ in range(n+1)]
    for _ in range(k):
        a, b = map(int, input().split())
        edge[a].append(b)
        indegree[b] += 1

    queue = deque()
    for i in range(1, n+1):
        if not indegree[i]:
            queue.append(i)

    dist = [0] * (n+1)
    target = int(input())
    while queue:
        x = queue.popleft()
        dist[x] += time[x]
        if x == target:
            print(dist[x])
            break

        for next in edge[x]:
            indegree[next] -= 1
            dist[next] = max(dist[next], dist[x])
            if not indegree[next]:
                queue.append(next)