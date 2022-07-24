import heapq

n, d = map(int, input().split())
arr = tuple(map(int, input().split()))

dp = [arr[0]]
st = {(-dp[0], 0)}
heap = [(-dp[0], 0)]

for i in range(1, n):
    dp.append(max(arr[i], arr[i]-heap[0][0]))

    st.add((-dp[i], i))
    if len(st) > d:
        st.remove((-dp[i-d], i-d))
    
    while heap and not heap[0] in st:
        heapq.heappop(heap)
    heapq.heappush(heap, (-dp[i], i))

print(max(dp))