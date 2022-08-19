n, k = map(int, input().split())

dic = {}
for i in range(n):
    dic[i] = int(input())

st = {0}
i = 1
next = dic[0]
while len(st) == i:
    if next == k:
        print(i)
        exit(0)
    st.add(next)
    i += 1
    next = dic[next]
print(-1)