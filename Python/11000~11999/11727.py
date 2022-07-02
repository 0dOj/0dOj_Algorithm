from collections import deque
n = int(input())
q = deque([1, 3])
for i in range(n-1):
    q.append((q[0]*2+q[1])%10007)
    q.popleft()
print(q[0])