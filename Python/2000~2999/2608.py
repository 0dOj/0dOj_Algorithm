roma = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90,
        'L':50, 'XL':40, 'X':10, 'IX': 9, 'V':5, 'IV': 4, 'I':1}

a = list(input()); b = list(input())
a.reverse(); b.reverse();

asum = 0
bsum = 0
data = 0

for i in a:
    if roma[i] >= data:
        asum += roma[i]
        data = roma[i]
    else:
        asum -= roma[i]
data = 0
for i in b:
    if roma[i] >= data:
        bsum += roma[i]
        data = roma[i]
    else:
        bsum -= roma[i]
    
anum = asum + bsum
rnum = ''

print(anum)

j = 0
while anum != 0:
    while anum >= list(roma.values())[j]:
        rnum += list(roma.keys())[j]
        anum -= list(roma.values())[j]
    j += 1
    
print(rnum)