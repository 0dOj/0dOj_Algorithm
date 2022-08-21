table = []
def dfs(n):
    if len(table) == n:
        print(*table)
    for i in range(1, n+1):
        if not i in table:
            table.append(i)
            dfs(n)
            table.pop()

dfs(int(input()))