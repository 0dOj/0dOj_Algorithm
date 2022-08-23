import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
ver = tuple([0]) + tuple(input().rstrip())
if n == 1:
    print(ver[1])
    exit(0)

edges = {i:set() for i in range(1, n+1)}
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a].add(b)
    edges[b].add(a)

lst = [1]
queue = deque(lst)
edges_reverse = [0] * (n+1)

while lst:
    lst = []
    max_str = ''
    while queue:
        x = queue.popleft()

        for nx in edges[x]:
            edges[nx].remove(x)
            edges_reverse[nx] = x
            if ver[nx] > max_str:
                max_str = ver[nx]
                lst = [nx]
            elif ver[nx] == max_str:
                lst.append(nx)
    if lst: temp = lst[0]
    queue = deque(lst)

lst = []
while True:
    lst.append(temp)
    if edges_reverse[temp]:
        temp = edges_reverse[temp]
    else:
        break

lst.reverse()
for i in lst:
    print(ver[i], end = '')