from collections import deque

startPos, targetPos = map(int, input().split())
lim = 100001; queue = deque([startPos]); visit = [lim] * lim; visit[startPos] = 0

while queue:
   x = queue.popleft()
   if 0 <= x*2 < lim and visit[x] < visit[x*2]:
      queue.append(x*2)
      visit[x*2] = visit[x]
   for i in (x-1, x+1):
      if 0 <= i < lim and visit[x]+1 < visit[i]:
         queue.append(i)
         visit[i] = visit[x]+1

print(visit[targetPos])