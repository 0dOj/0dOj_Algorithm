import heapq
import math
from sys import stdin
input = stdin.readline

n, e = map(int, input().split())

vec = [[] for _ in range(n)]
for _ in range(e):
    a, b, c = map(int, input().split()); a -= 1; b -= 1
    vec[a].append((b, c))
    vec[b].append((a, c))

v1, v2 = map(int, input().split()); v1 -= 1; v2 -= 1

def Dijk(s, t):
    arr = [math.inf] * n; arr[s] = 0
    heap = [[arr[s], s]]

    while heap:
        x = heapq.heappop(heap)[1]

        if x == t:
            return arr[t]

        for i in vec[x]:
            if arr[x] + i[1] < arr[i[0]]:
                arr[i[0]] = arr[x] + i[1]
                heapq.heappush(heap, [arr[i[0]], i[0]])

    return math.inf

ans = min(Dijk(0, v1)+Dijk(v2, n-1), Dijk(0, v2)+Dijk(v1, n-1)) + Dijk(v1, v2)
if ans == math.inf:
    print(-1)
else:
    print(ans)