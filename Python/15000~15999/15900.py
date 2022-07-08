from sys import stdin

input = stdin.readline

n = int(input())
edge = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

dcnt = 0
stack = [(1, 0)]
while stack:
    s, d = stack.pop()

    if edge[s]:
        for c in edge[s]:
            edge[c].remove(s)
            stack.append((c, d+1))

    else:
        dcnt += d

if dcnt % 2 == 1:
    print('Yes')
else:
    print('No')