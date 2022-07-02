import heapq
from sys import stdin
input = stdin.readline

n = int(input())
arr = tuple(map(int, input().split()))

arrdict = {}
heap = []
for i in range(n):
    arrdict[i+1] = arr[i]
    heapq.heappush(heap, [arr[i], i+1])

m = int(input())
for i in range(m):
    query = tuple(map(int, input().split()))

    if query[0] == 1:
        arrdict[query[1]] = query[2]
        heapq.heappush(heap, [query[2], query[1]])

    elif query[0] == 2:
        while heap[0][0] != arrdict[heap[0][1]]:
            heapq.heappop(heap)
        print(heap[0][1])