from collections import deque
from sys import stdin
input = stdin.readline

M, N = map(int, input().split())
s = []; d = []; queue = deque([1]); visited = [100] * 101; visited[1] = 0

def onls(x, k): # k = 1~6
    if x+k < 101:
        if visited[x]+1 < visited[x+k]:
            if x+k in s:
                ind = s.index(x+k)
                if visited[x]+1 < visited[d[ind]]:
                    queue.append(d[ind])
                    visited[d[ind]] = visited[x]+1
            else:
                queue.append(x+k)
            visited[x+k] = visited[x]+1
    
for i in range(M+N):
    a, b = map(int, input().split())
    s.append(a); d.append(b)

while visited[100] == 100:
    x = queue.popleft()
    for k in range(1, 7):
        onls(x, k)

print(visited[100])