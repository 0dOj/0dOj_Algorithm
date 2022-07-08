from sys import stdin

input = stdin.readline

for _ in range(int(input())):

    n, m, w = map(int, input().split())

    edge = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edge.append((s, e, t))
        edge.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edge.append((s, e, -t))

    dist = [0] * (n+1)
    loop = False
    
    for i in range(n):
        for j in range(m+m+w):
            cur = edge[j][0]
            next = edge[j][1]
            cost = edge[j][2]

            if dist[cur]+cost < dist[next]:
                dist[next] = dist[cur]+cost
                if i == n-1:
                    loop = True
                    break
        if loop:
            break
        
    if loop:
        print('YES')
    else:
        print('NO')