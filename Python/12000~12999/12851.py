from collections import deque

startPos, targetPos = map(int, input().split())
visited = [100002] * 100001; visited[startPos] = 0; queue = deque([startPos]); cnt = 1

while visited[targetPos] == 100002:
    x = queue.popleft()
    for i in (x-1, x+1, x*2):
        if 0 <= i <= 100000 and visited[x]+1 <= visited[i]:
            visited[i] = visited[x]+1
            if visited[targetPos] != 100002:
                break
            queue.append(i)
while queue:
    x = queue.popleft()
    for i in (x-1, x+1, x*2):
        if 0 <= i <= 100000 and visited[x]+1 <= visited[i] and i == targetPos:
            cnt += 1

print(visited[targetPos])
print(cnt)