k, n = map(int, input().split())

lst = []
mx = 0
for _ in range(k):
    x = input()
    lst.append(x)
    if int(x) > mx:
        mx = int(x)

for i in range(k):
    if lst[i] == str(mx):
        lst[i] += lst[i] * (n-k)
        break

if len(lst) == 1:
    print(lst[0])
    exit(0)

for i in range(k):
    for j in range(1, k):
        c1 = lst[j-1]+lst[j]
        c2 = lst[j]+lst[j-1]

        if c1 < c2:
            lst[j], lst[j-1] = lst[j-1], lst[j]

s = ''
for i in lst:
    s += i
print(s)