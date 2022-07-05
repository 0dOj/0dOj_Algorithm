n = int(input())

h = 10000
w = 10000
o = 1001
e = 1000
l = 120
r = 100
d = 1
lst = [h, w, o, e, l, r, d]

t = []
def DFS(m): # m = 7
    if m == 0:
        sm = 0
        for i in range(7):
            sm += t[i] * lst[i]
        if sm == n:
            print(f'  {t[0]}{t[3]}{t[4]}{t[4]}{t[2]}')
            print(f'+ {t[1]}{t[2]}{t[5]}{t[4]}{t[6]}')
            print('-------')
            print(f'{n:>7}')
            exit(0)
        else:
            return
    for i in range(10):
        if i == 0 and m >= 6:
            continue
        if not i in t:
            t.append(i)
            DFS(m-1)
            t.pop()

DFS(7)
print('No Answer')