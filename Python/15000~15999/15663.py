n, m = map(int, input().split())
lst = list(map(int, input().split()))
table = []; ans = []

def DFS(n, m):
    if m == 0:
        ans.append([lst[table[i]] for i in range(len(table))])
        return

    for i in range(n):
        if not i in table:
            table.append(i)
            DFS(n, m-1)
            table.pop()

DFS(n, m)
ans.sort(); init = []
for i in ans:
    if init != i:
        print(*i)
        init = i