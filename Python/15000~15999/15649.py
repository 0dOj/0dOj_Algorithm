n, m = map(int, input().split())

lst = [i for i in range(1, n+1)]
table = []

def DFS(n, m):
    if m == 0:
        print(*table)
        return
    for i in lst:
        if not i in table:
            table.append(i)
            DFS(n, m-1)
            table.pop()

DFS(n, m)