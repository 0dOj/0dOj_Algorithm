from sys import stdin
import heapq

for _ in range(int(input())):
    m = int(input())
    arr = []
    for _ in range(m//10+1):
        arr.extend(list(map(int, input().split())))
    mid_list = [arr[0]]
    mid = arr[0]

    lowheap = []
    highheap = []

    for i in range(1, m, 2):
        l = sorted([mid, arr[i], arr[i+1]])

        heapq.heappush(highheap, l.pop())
        heapq.heappush(lowheap, -l.pop(0))

        l.append(heapq.heappop(highheap))
        l.append(-heapq.heappop(lowheap))

        l.sort()
        mid = l[1]
        mid_list.append(l[1])

        heapq.heappush(highheap, l.pop())
        heapq.heappush(lowheap, -l.pop(0))

    print(len(mid_list))
    for i in range(len(mid_list)//10+1):
        print(*mid_list[i*10:(i+1)*10])