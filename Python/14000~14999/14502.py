from collections import deque

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.extend(list(map(int, input().split())))

virus = []
for i in range(n*m):
    if arr[i] == 2:
        virus.append(i)

mx = 0
for a in range(n*m-2):
    if arr[a] == 0:
        arr[a] = 1
        for b in range(a+1, n*m-1):
            if arr[b] == 0:
                arr[b] = 1
                for c in range(b+1, n*m):
                    if arr[c] == 0:
                        arr[c] = 1

                        arr2 = arr[:]
                        for v in virus:
                            queue = deque([v])

                            while queue:
                                x = queue.popleft()

                                for i in (x-m, x+m, x-1 if (x-1)%m != (m-1) else -1, x+1 if (x+1)%m != 0 else -1):
                                    if 0 <= i < n*m and arr2[i] == 0:
                                        arr2[i] = 2
                                        queue.append(i)

                        mx = max(mx, arr2.count(0))
                        
                        arr[c] = 0
                arr[b] = 0
        arr[a] = 0

print(mx)