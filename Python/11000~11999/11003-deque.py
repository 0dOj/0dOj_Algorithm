from collections import deque
from sys import stdout

print = stdout.write

n, l = map(int, input().split())
arr = tuple(map(int, input().split()))

queue = deque()
for i in range(n):
    while queue and queue[-1][0] > arr[i]:
        queue.pop()
    queue.append((arr[i], i))

    while queue[0][1] <= i-l:
        queue.popleft()

    print(str(queue[0][0])+' ')