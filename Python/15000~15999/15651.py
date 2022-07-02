n, m = map(int, input().split())
table = []

def DFS(m):
    if m == 0:
        print(*table)
        return
    for i in range(1, n+1):
        table.append(i)
        DFS(m-1)
        table.pop()

DFS(m)