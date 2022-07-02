import heapq
from sys import stdin
input = stdin.readline

heap = []

for i in range(int(input())):
    x = int(input())
    if x == 0:
        if heap == []:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)  