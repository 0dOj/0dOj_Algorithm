from sys import stdin
import heapq

input = stdin.readline

n = int(input())

heap = []
for _ in range(n):
    order = tuple(map(int, input().split()))

    if order[0] == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(-1)
    
    else:
        for x in order[1:]:
            heapq.heappush(heap, -x)