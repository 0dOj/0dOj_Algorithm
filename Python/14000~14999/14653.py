from sys import stdin

input = stdin.readline

n, k, q = map(int, input().split())

lst = [input().split() for _ in range(k)]

st = {chr(66+i) for i in range(n-1)}
for i in range(k-1, q-2, -1):
    if lst[i][1] in st:
        st.remove(lst[i][1])
i = q-2
while i >= 0 and lst[q-1][0] == lst[i][0]:
    if lst[i][1] in st:
        st.remove(lst[i][1])
    i -= 1

if st and int(lst[q-1][0]) != 0:
    print(*sorted(st))
else:
    print(-1)