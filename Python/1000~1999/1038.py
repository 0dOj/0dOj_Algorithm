n = int(input())
cnt = 0
table = []

def DFS(m, k):
    if m == 0:
        global cnt
        global n
        if n == cnt:
            print(''.join(map(str, table)))
            exit(0)
        cnt += 1
        return
    for i in range(0, 10):
        if i < k:
            table.append(i)
            DFS(m-1, i)
            table.pop()

for m in range(1, 11):
    DFS(m, 10)

print(-1)