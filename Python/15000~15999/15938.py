from collections import defaultdict
input = iter(open(0).read().split("\n")).__next__

xs, ys = map(int, input().split())
t = int(input())
xh, yh = map(int, input().split())
n = int(input())
wall = set()
for _ in range(n):
    wall.add(tuple(map(int, input().split())))

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
dp = [defaultdict(int, {(xs, ys): 1})]
for nt in range(t):
    dp.append(defaultdict(int))

    for x, y in dp[-2]:
        if x == xh and y == yh:
            dp[-1][(x, y)] += dp[-2][(x, y)] % 1000000007
        else:
            for i in range(4):
                nx = x+dx[i]; ny = y+dy[i]
                if not (nx, ny) in wall and (xh-nx if xh-nx > 0 else -xh+nx) + (yh-ny if yh-ny > 0 else -yh+ny) < t-nt:
                    dp[-1][(nx, ny)] += dp[-2][(x, y)] % 1000000007

print(dp[-1][(xh, yh)]%1000000007)