import heapq

a, b = map(int, input().split())
heap = [a]
dic = {a:1}
x = a

while x < b:
    x = heapq.heappop(heap)
    x1 = int(str(x)+"1")
    if not x*2 in dic or dic[x*2] > dic[x]+1:
        heapq.heappush(heap, x*2)
        dic[x*2] = dic[x]+1
    if not x1 in dic or dic[x1] > dic[x]+1:
        heapq.heappush(heap, x1)
        dic[x1] = dic[x]+1

try:
    print(dic[b])
except:
    print(-1)