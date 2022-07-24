from collections import deque

n, k = input().split()

m = len(n)
if m < 2:
    print(-1)
    exit(0)

st = set([n])
for t in range(int(k)):
    queue = deque(st)
    st = set()
    while queue:
        x = queue.popleft()

        for i in range(m-1):
            for j in range(i+1, m):
                nx = list(x)
                nx[i], nx[j] = nx[j], nx[i]
                nx = ('').join(nx)
                if nx[0] != '0':
                    st.add(nx)
    if not st:
        print(-1)
        exit(0)

print(max(map(int, st)))