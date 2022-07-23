from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
arr = tuple(tuple(input().rstrip()) for _ in range(n))

parent = [i*m+j for i in range(n) for j in range(m)]

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

for i in range(n):
    for j in range(m):
        if   arr[i][j] == 'L':
            union(i*m+j, i*m+j-1)
        elif arr[i][j] == 'R':
            union(i*m+j, i*m+j+1)
        elif arr[i][j] == 'U':
            union(i*m+j, i*m+j-m)
        elif arr[i][j] == 'D':
            union(i*m+j, i*m+j+m)

for i in range(n):
    for j in range(m):
        parent[i*m+j] = find(i*m+j)

print(len(set(parent)))