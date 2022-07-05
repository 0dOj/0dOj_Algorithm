import heapq
import math
from sys import stdin
input = stdin.readline

n, m, o = map(int, input().split())

vec = [[] for _ in range(n+1)]
rvec = [[] for _ in range(n+1)]

for i in range(m):
    a, b, t = map(int, input().split())
    vec[a].append((b, t))
    rvec[b].append((a, t))


def dijk(o):
    arr = [math.inf] * (n+1); arr[o] = 0
    heap = [[arr[o], o]]

    while heap:
        x = heapq.heappop(heap)[1]

        for i in vec[x]:
            if arr[x]+i[1] < arr[i[0]]:
                arr[i[0]] = arr[x]+i[1]
                heapq.heappush(heap, [arr[i[0]], i[0]])

    return arr

lst1 = dijk(o)
vec = rvec
lst2 = dijk(o)

mx = 0
for i in range(1, n+1):
    mx = max(mx, lst1[i]+lst2[i])
print(mx)