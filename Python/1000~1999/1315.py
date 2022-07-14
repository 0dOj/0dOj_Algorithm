from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())

arr = [[[0, 0] for _ in range(1001)] for _ in range(1001)]
for _ in range(n):
    s, i, p = map(int, input().split())

    for ax in range(1001):
        for ay in range(1001):
            if s <= ax or i <= ay:
                arr[ax][ay][0] += p
                arr[ax][ay][1] += 1

queue = deque([(1, 1, 0, 0)])
max_quest = 0

visit = [[False] * 1001 for _ in range(1001)]; visit[1][1] = True
while queue:
    x, y, got_point, cur_point = queue.popleft()

    cur_point += arr[x][y][0] - got_point
    got_point = arr[x][y][0]
    max_quest = max(max_quest, arr[x][y][1])

    if cur_point:
        if 0 < x+1 < 1001 and not visit[x+1][y]:
            visit[x+1][y] = True
            queue.append((x+1, y, got_point, cur_point-1))
        if 0 < y+1 < 1001 and not visit[x][y+1]:
            visit[x][y+1] = True
            queue.append((x, y+1, got_point, cur_point-1))

print(max_quest)