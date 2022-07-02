e = input()

s = 0
l = 0
c = 0
m = 1
for i in range(len(e)):
    if e[i] == '+':
        c += m*int(e[s:l])
        s = l+1
    elif e[i] == '-':
        c += m*int(e[s:l])
        s = l+1
        m = -1
    l += 1
print(c+m*int(e[s:l]))