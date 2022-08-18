from sys import stdin

input = stdin.readline

n = int(input())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []

for i in range(n):
    c = int(input())
    edges.append((c, 0, i+1))

for i in range(n):
    line = tuple(map(int, input().split()))
    for j in range(n):
        if line[j] != 0:
            edges.append((line[j], i+1, j+1))

edges.sort()

result = 0
for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += c
print(result)