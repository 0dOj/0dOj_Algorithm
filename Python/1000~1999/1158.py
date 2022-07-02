from collections import deque

n, k = map(int, input().split())
queue = deque([_ for _ in range(1, n+1)])
cnt = 0
ans = []

while queue:
    x = queue.popleft()
    cnt += 1
    if cnt == k:
        cnt = 0
        ans.append(x)
    else:
        queue.append(x)

print('<'+str(ans)[1:-1]+'>')