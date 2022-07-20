from collections import deque

n, m = map(int, input().split())
q = deque([i for i in range(1, n+1)])

arr = list(map(int, input().split()))

cnt = 0
for i in arr:
    x = q.index(i)
    if x <= len(q)-x:
        cnt += x
        for i in range(x):
            q.append(q.popleft())
        q.popleft()
    else:
        cnt += len(q)-x
        for i in range(len(q)-x):
            q.appendleft(q.pop())
        q.popleft()
print(cnt)