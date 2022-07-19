from collections import deque

n = int(input())
q = deque(map(int, input().split()))
index = deque(i for i in range(1, n+1))

ans = []
p = 0
for i in range(n):
    if p > 0:
        p -= 1
        while p != 0:
            q.append(q.popleft())
            index.append(index.popleft())
            p -= 1

    elif p < 0:
        while p != 0:
            q.appendleft(q.pop())
            index.appendleft(index.pop())
            p += 1

    ans.append(index.popleft())
    p = q.popleft()

print(*ans)