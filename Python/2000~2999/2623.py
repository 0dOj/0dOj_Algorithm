from collections import deque

n, m = map(int, input().split())

indegree = [0] * (n+1)
edge = [[] for _ in range(n+1)]
for _ in range(m):
    line = tuple(map(int, input().split()[1:]))
    for i in range(len(line)-1):
        a, b = line[i], line[i+1]
        edge[a].append(b)
        indegree[b] += 1

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

result = []
while queue:
    x = queue.popleft()
    result.append(x)

    for next in edge[x]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

if len(result) == n:
    print(*result)
else:
    print(0)