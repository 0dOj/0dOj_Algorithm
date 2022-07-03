import heapq
import math
from sys import stdin
input = stdin.readline

n = int(input())
m = int(input())

vec = [[] for _ in range(n)]

for i in range(m):
    a, b, l = map(int, input().split())
    vec[a-1].append((b-1, l))

s, d = map(int, input().split())
s -= 1; d -= 1

heap = [[0, s]]
arr = [math.inf for _ in range(n)]; arr[s] = 0

while True:
    x = heapq.heappop(heap)[1]

    if x == d:
        print(arr[d])
        exit(0)
    
    for i in vec[x]:
        if arr[i[0]] > arr[x]+i[1]:
            arr[i[0]] = arr[x]+i[1]
            heapq.heappush(heap, [arr[i[0]], i[0]])