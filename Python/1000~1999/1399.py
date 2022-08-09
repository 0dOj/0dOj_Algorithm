from collections import deque

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

def dig(n):
    if n >= 10:
        return dig(sum(map(int, list(str(n)))))
    else:
        return n

for _ in range(int(input())):
    k, m = map(int, input().split())
    f = dig(m)
    lst = []
    n = 1
    while True:
        if dig(n) in lst:
            lst.append(dig(n))
            break
        else:
            lst.append(dig(n))
            n *= f
    non_cycle = deque(lst[:lst.index(lst[-1])])
    cycle = deque(lst[lst.index(lst[-1]):-1])
    
    x, y = 0, 0
    dir = 0
    while k and non_cycle:
        x += dx[dir] * non_cycle[0]
        y += dy[dir] * non_cycle[0]
        dir = (dir+1)%4
        non_cycle.popleft()
        k -= 1
    if not k:
        print(x, y)
        continue

    k %= len(cycle)*4
    while k:
        x += dx[dir] * cycle[0]
        y += dy[dir] * cycle[0]
        dir = (dir+1)%4
        cycle.append(cycle.popleft())
        k -= 1

    print(x, y)