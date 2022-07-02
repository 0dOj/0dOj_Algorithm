from collections import deque

startPos, targetPos = map(int, input().split())
queue = deque([startPos]); visited = [100000] * 100001; visited[startPos] = 0

if startPos >= targetPos:
    print(startPos - targetPos)
else:
    while visited[targetPos] == 100000:
        pos = queue.popleft()
        if pos < 100000 and visited[pos] + 1 < visited[pos + 1]:
            visited[pos + 1] = visited[pos] + 1
            queue.append(pos + 1)
        if pos > 0 and visited[pos] + 1 < visited[pos - 1]:
            visited[pos - 1] = visited[pos] + 1
            queue.append(pos - 1)
        if pos < 50001 and visited[pos] + 1 < visited[pos * 2]:
            visited[pos * 2] = visited[pos] + 1
            queue.append(pos * 2)

    print(visited[targetPos])