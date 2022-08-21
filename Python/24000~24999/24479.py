import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m, r = map(int, input().split())

edge = {i:set() for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    edge[a].add(b)
    edge[b].add(a)

visit = [0] * (n+1)
visit[r] = 1
visit_cnt = 1

def dfs(x):
    global visit_cnt
    for nx in sorted(edge[x]):
        if not visit[nx]:
            visit_cnt += 1
            visit[nx] = visit_cnt
            dfs(nx)

dfs(r)

for i in visit[1:]:
    print(i)