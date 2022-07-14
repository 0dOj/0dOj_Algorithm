from sys import stdin
import heapq

n, m = map(int, input().split())

arr = tuple(tuple(map(int, input().split())) for _ in range(n))
dp = [[0] * m for _ in range(n)]; dp[0][0] = 1

maxheap = []
for i in range(n):
    for j in range(m):
        heapq.heappush(maxheap, (-arr[i][j], i, j))

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

while maxheap:
    x, y = heapq.heappop(maxheap)[1:]

    for i in range(4):
        nx = x+dx[i]; ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] < arr[x][y]:
            dp[nx][ny] += dp[x][y]

print(dp[-1][-1])