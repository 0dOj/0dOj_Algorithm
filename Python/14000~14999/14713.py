n = int(input())
s = [input().split() for _ in range(n)]
l = input().split()

for _ in range(len(l)):
    imp = True
    for i in range(n):
        if l and s[i] and l[-1] == s[i][-1]:
            imp = False
            l.pop()
            s[i].pop()
            break
    if imp:
        print('Impossible')
        exit(0)
if l:
    print('Impossible')
else:
    print('Possible')