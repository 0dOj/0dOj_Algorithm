from sys import stdin
from collections import deque
input = stdin.readline

com = int(input()); rel = int(input())
rels = [[] for _ in range(com+1)]; queue = deque([1])
visited = [False] * (com + 1); visited[1] = True

for i in range(rel):
    a, b = map(int, input().split())
    rels[a].append(b); rels[b].append(a) # 그래프 입력

ans = 0

while queue:
    x = queue.popleft()

    for i in rels[x]:
        if visited[i] == False:
            queue.append(i)
            visited[i] = True
            ans += 1

print(ans)