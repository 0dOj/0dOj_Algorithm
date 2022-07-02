import heapq
from sys import stdin
input = stdin.readline

n = int(input())

lowheap = []
highheap = []
mid = int(input())
print(mid)
for i in range(1, n):
    x = int(input())

    if mid < x:
        heapq.heappush(highheap, x)
        heapq.heappush(lowheap, -mid)
    else:
        heapq.heappush(highheap, mid)
        heapq.heappush(lowheap, -x)
    
    if i % 2 == 1:
        mid = -heapq.heappop(lowheap)
    else:
        mid = heapq.heappop(highheap)

    print(mid)