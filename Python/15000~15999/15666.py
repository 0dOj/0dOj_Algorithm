n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
table = []; ans = []

def DFS(n, m, k):
    if m == 0:
        ans.append([lst[table[i]] for i in range(len(table))])
        return

    for i in range(n):
        if i >= k:
            k = i
            table.append(i)
            DFS(n, m-1, k)
            del table[-1]

DFS(n, m, 0)
ans.sort(); init = []
for i in ans:
    if init != i:
        print(*i)
        init = i