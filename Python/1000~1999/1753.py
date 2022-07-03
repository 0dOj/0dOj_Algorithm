import heapq
import math
from sys import stdin
input = stdin.readline

v, e = map(int, input().split())
k = int(input()); k -= 1

vec = [[] for _ in range(v)]

for _ in range(e):
    a, b, w = map(int, input().split()); a -= 1; b -= 1
    vec[a].append((b, w))

arr = [math.inf for _ in range(v)]; arr[k] = 0
heap = [[0, k]]

while heap:
    x = heapq.heappop(heap)[1]

    for i in vec[x]:
        if arr[x] + i[1] < arr[i[0]]:
            arr[i[0]] = arr[x] + i[1]
            heapq.heappush(heap, [arr[i[0]], i[0]])

for i in arr:
    if i == math.inf:
        print('INF')
    else:
        print(i)