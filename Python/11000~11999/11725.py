from sys import stdin

input = stdin.readline

n = int(input())

edge = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

parent = [0] * (n+1)
stack = [1]

while stack:
    x = stack.pop()
    
    for i in edge[x]:
        parent[i] = x
        stack.append(i)
        edge[i].remove(x)

for i in range(2, n+1):
    print(parent[i])