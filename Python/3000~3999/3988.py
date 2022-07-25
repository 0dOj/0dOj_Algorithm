import heapq

n, k = map(int, input().split())
l = n-k
arr = sorted(map(int, input().split()))

min_arr = []
for i in range(n-1):
    min_arr.append(arr[i+1]-arr[i])

mn = 20000001
heap = []
for i in range(l-2):
    heapq.heappush(heap, (min_arr[i], i))
for i in range(l-1, n):
    heapq.heappush(heap, (min_arr[i-1], i-1))
    while heap[0][1] <= i-l:
        heapq.heappop(heap)
    m = arr[i]-arr[i-l+1]
    mn = min(mn, m+heap[0][0])

print(mn)