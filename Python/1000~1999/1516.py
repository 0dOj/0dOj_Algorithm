from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())

indegree = [0]
edge = [[] for _ in range(n+1)]
dist = [0] * (n+1)
time = [0]

for b in range(1, n+1):
    line = deque(map(int, input().split()))

    time.append(line.popleft())

    indegree.append(len(line)-1)
    while line[0] != -1:
        a = line.popleft()
        edge[a].append(b)

queue = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    dist[x] += time[x]

    for next in edge[x]:
        indegree[next] -= 1
        dist[next] = max(dist[next], dist[x])
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, n+1):
    print(dist[i])