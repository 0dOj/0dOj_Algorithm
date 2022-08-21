from collections import deque

n, m = map(int, input().split())
map_arr = tuple(tuple(map(int, tuple(input()))) for _ in range(n))

water_arr = [[0] * m for _ in range(n)]
water_fixed = [[False] * m for _ in range(n)]

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

for i in range(n):
    for j in range(m):
        if not water_fixed[i][j]:
            hei = map_arr[i][j]
            fail = True
            for now_hei in range(9, hei, -1):
                visit = [[False] * m for _ in range(n)]
                visit[i][j] = True
                queue = deque([(i, j)])
                fail = False

                while queue:
                    x, y = queue.popleft()

                    for d in range(4):
                        nx = x+dx[d]; ny = y+dy[d]
                        if 0 <= nx < n and 0 <= ny < m and map_arr[nx][ny]:
                            if not visit[nx][ny]:
                                visit[nx][ny] = True
                                if now_hei > map_arr[nx][ny]:
                                    queue.append((nx, ny))
                        else:
                            fail = True
                            break
                    if fail:
                        break
                if not fail:
                    hei = now_hei
                    break

            if not fail:
                for vi in range(n):
                    for vj in range(m):
                        if visit[vi][vj]:
                            water_arr[vi][vj] = hei
                            water_fixed[vi][vj] = True

result = 0
for i in range(n):
    for j in range(m):
        result += max(water_arr[i][j]-map_arr[i][j], 0)
print(result)