from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

result = 0
cmx = 0
for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        cmx = max(cmx, c)
        result += c
print(result-cmx)