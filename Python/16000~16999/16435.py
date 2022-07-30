n, l = map(int, input().split())
h = sorted(map(int, input().split()), reverse=True)

while h and l >= h[-1]:
    l += 1
    h.pop()
print(l)