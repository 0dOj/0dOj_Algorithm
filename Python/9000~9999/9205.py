from collections import deque
from sys import stdin

input = stdin.readline

for T in range(int(input())):
    n = int(input())

    sx, sy = map(int, input().split())
    store_arr = [tuple(map(int, input().split())) for _ in range(n)]
    tx, ty = map(int, input().split()); store_arr.append((tx, ty))

    queue = deque([(sx, sy)])
    visit = set()
    happy = False

    while queue:
        x, y = queue.popleft()
        if (x, y) == (tx, ty):
            happy = True
            break
        
        for nx, ny in store_arr:
            if not (nx, ny) in visit and abs(x-nx)+abs(y-ny) <= 1000:
                visit.add((nx, ny))
                queue.append((nx, ny))
        
    if happy:
        print('happy')
    else:
        print('sad')