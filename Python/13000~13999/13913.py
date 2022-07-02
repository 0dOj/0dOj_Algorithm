from collections import deque

s, t = map(int, input().split())
if s == t:
    print(0)
    print(s)
    exit(0)
queue = deque([s])
visit = [-1] * 100001
cnt = 0

while visit[t] == -1:
    x = queue.popleft()

    for i in (x-1, x+1, x*2):
        if 0 <= i < 100001 and visit[i] == -1 and i != s:
            visit[i] = x
            queue.append(i)

k = t
ans = []
while k != s:
    ans.append(k)
    k = visit[k]

print(len(ans))
print(s, *reversed(ans)) 