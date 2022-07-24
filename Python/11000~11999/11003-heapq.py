import heapq
from sys import stdout

print = stdout.write

n, l = map(int, input().split())
arr = tuple(map(int, input().split()))

heap = []
for i in range(n):
    heapq.heappush(heap, (arr[i], i))
    while heap[0][1] <= i-l:
        heapq.heappop(heap)
    print(str(heap[0][0])+' ')