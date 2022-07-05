from collections import deque

n, m = map(int, input().split())

known = set(list(map(int, input().split()))[1:])
queue = deque(known)

lst = []
for i in range(m):
    lst.append(list(map(int, input().split()))[1:])

while queue:
    x = queue.popleft()

    for i in range(m):
        if x in lst[i]:
            for j in lst[i]:
                if not j in known:
                    known.add(j)
                    queue.append(j)
            lst[i] = []

cnt = 0
for i in range(m):
    if lst[i]:
        cnt += 1
print(cnt)