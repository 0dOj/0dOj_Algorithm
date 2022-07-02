import sys
from collections import deque
sys.setrecursionlimit(100001)
input = sys.stdin.readline

def dfs(x):
    for i in l[x]:
        if visited[x] < visited[i]:
            visited[i] = visited[x]
            dfs(i)

for i in range(int(input())):
    n = int(input()); k = int(input())
    l = [[] for _ in range(n)]; visited = [_ for _ in range(n)]

    for j in range(k):
        a, b = map(int, input().split())
        l[a].append(b); l[b].append(a)

    for j in range(n):
        if visited[j] == j:
            dfs(j)

    print(f"Scenario {i+1}:")
    for i in range(int(input())):
        a, b = map(int, input().split())
        if visited[a] == visited[b]: print(1)
        else: print(0)
    print()