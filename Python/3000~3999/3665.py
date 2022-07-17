from sys import stdin
from collections import deque

input = stdin.readline

for _ in range(int(input())):
    n = int(input())

    arr = list(map(int, input().split()))

    indegree = [0] * (n+1)
    edge = [set() for _ in range(n+1)]

    for a in range(n):
        for b in range(a+1, n):
            indegree[arr[b]] += 1
            edge[arr[a]].add(arr[b])

    m = int(input())

    imp = False
    for _ in range(m):
        if not imp:
            a, b = map(int, input().split())
            if a in edge[b]:
                edge[b].remove(a)
                indegree[a] -= 1
                edge[a].add(b)
                indegree[b] += 1
            elif b in edge[a]:
                edge[a].remove(b)
                indegree[b] -= 1
                edge[b].add(a)
                indegree[a] += 1
            else:
                imp = True
        else:
            input()
    if imp:
        print('IMPOSSIBLE')

    queue = deque()
    for i in range(n):
        if indegree[arr[i]] == 0:
            queue.append(arr[i])

    ans = []
    while queue:
        x = queue.popleft()
        ans.append(x)

        for next in edge[x]:
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)

    if len(ans) != n:
        print('IMPOSSIBLE')
    else:
        print(*ans)