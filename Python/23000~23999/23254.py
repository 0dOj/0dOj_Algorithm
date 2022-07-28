import heapq

n, m = map(int, input().split()); n *= 24
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
heap = []
for i in range(m):
    heapq.heappush(heap, [-b[i], a[i]])

while n:
    n -= 1
    while -heap[0][0]+heap[0][1] > 100:
        heapq.heappush(heap, [-100+heap[0][1], heap[0][1]])
        heapq.heappop(heap)
    heap[0][1] += -heap[0][0]

score = 0
for i in heap:
    score += i[1]
print(score)