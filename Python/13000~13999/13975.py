from sys import stdin
import heapq

input = stdin.readline

for _ in range(int(input())):
    n = int(input())

    heap = list(map(int, input().split()))
    heapq.heapify(heap)

    cost = 0
    while len(heap) != 1:
        c1 = heapq.heappop(heap)
        c2 = heapq.heappop(heap)

        x1 = c1+c2
        cost += x1
        heapq.heappush(heap, x1)

    print(cost)