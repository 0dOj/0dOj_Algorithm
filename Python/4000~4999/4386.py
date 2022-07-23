n = int(input())

parent = [i for i in range(n)]

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

vertex = []
for _ in range(n):
    a, b = map(float, input().split())
    vertex.append((a, b))

edges = []
for i in range(n):
    x1, y1 = vertex[i]
    for j in range(i+1, n):
        x2, y2 = vertex[j]
        cost = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        edges.append((cost, i, j))
edges.sort()

result = 0
for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += c
print(result)