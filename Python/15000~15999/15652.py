n, m = map(int, input().split())
lst = [_ for _ in range(1, n+1)]; table = []

def DFS(n, m, k):
    if m == 0:
        print(*table)
        return
    for i in lst:
        if i >= k:
            k = i
            table.append(i)
            DFS(n, m-1, k)
            table.pop()

DFS(n, m, 0)