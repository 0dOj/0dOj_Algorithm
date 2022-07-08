import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

sight = {(arr[i], i) for i in range(2*m-1)}
heap = list(map(lambda x: (-x[0], x[1]), list(sight)))
heapq.heapify(heap)

ans = [-heap[0][0]]
for i in range(n-2*m+1):
    sight.remove((arr[i], i))
    sight.add((arr[i+2*m-1], i+2*m-1))
    heapq.heappush(heap, (-arr[i+2*m-1], i+2*m-1))
    while not (-heap[0][0], heap[0][1]) in sight:
        heapq.heappop(heap)
    ans.append(-heap[0][0])

print(*ans)