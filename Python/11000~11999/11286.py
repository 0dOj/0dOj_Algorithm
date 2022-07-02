import heapq
from sys import stdin
input = stdin.readline

heap = []

for i in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)