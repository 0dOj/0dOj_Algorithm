from collections import deque

n = int(input())
ans = [1]
queue = deque([i for i in range(2, n+1)])
while queue:
    queue.append(queue.popleft())
    ans.append(queue.popleft())
print(*ans)