from collections import deque

a, b, d, n = map(int, input().split())
q = deque([1] + [0] * (d-1))
copyable = 0

for day in range(n):
    q.pop()
    q.appendleft(0)

    copyable += q[a]
    copyable -= q[b]

    q[0] = copyable % 1000

print(sum(q)%1000)