from collections import deque

n = int(input())

visit = [0] * 1000001

q = deque([n])

while q:
    x = q.popleft()
    
    if x == 1:
        break

    if x % 3 == 0 and not visit[x//3]:
        visit[x//3] = x
        q.append(x//3)

    if x % 2 == 0 and not visit[x//2]:
        visit[x//2] = x
        q.append(x//2)

    if not visit[x-1]:
        visit[x-1] = x
        q.append(x-1)

ans = deque([1])
while x != n:
    x = visit[ans[0]]
    ans.appendleft(x)

print(len(ans)-1)
print(*ans)