from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10001)

n, m, v = map(int, input().split())
lines = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    lines[a].append(b); lines[b].append(a)

# DFS
visited = [False] * (n+1); visited[v] = True; lst = [v]

def dfs(x):
    for i in sorted(lines[x]):
        if not visited[i]:
            visited[i] = True
            lst.append(i)
            dfs(i)

dfs(v)
print(*lst)

#BFS
visited = [False] * (n+1); visited[v] = True; lst = [v]; queue = deque([v])

while queue:
    x = queue.popleft()
    for i in sorted(lines[x]):
        if not visited[i]:
            visited[i] = True
            lst.append(i)
            queue.append(i)

print(*lst)