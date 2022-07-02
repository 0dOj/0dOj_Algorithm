import sys
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
l = [[] for i in range(n+1)]; visited = [i for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    l[a].append(b); l[b].append(a)

def dfs(x):
    for i in l[x]:
        if visited[x] < visited[i]:
            visited[i] = visited[x]
            dfs(i)

cnt = 0
for i in range(1, n+1):
    if visited[i] == i:
        dfs(i)
        cnt += 1

print(cnt)