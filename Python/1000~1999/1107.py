targetCH = input()
m = int(input())
brokenButton = []
if m != 0: brokenButton = list(input().split())

if targetCH == '100': print(0); exit(0)

lst = []
for i in range(1000000):
    lst.append(i)
    for j in brokenButton:
        if j in str(i):
            lst.pop()
            break
if not 100 in lst: lst.append(100)

mn = 500000
targetCH = int(targetCH)
for i in lst:
    t = min(abs(targetCH-100), abs(targetCH-i)+len(str(i)))
    if t < mn:
        mn = t

print(mn)