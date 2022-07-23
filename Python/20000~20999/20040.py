from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b, i):
    global cycle
    a = find(a)
    b = find(b)
    if not cycle and a == b:
        cycle = i
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b

cycle = 0
for i in range(1, m+1):
    a, b = map(int, input().split())
    union(a, b, i)

print(cycle)