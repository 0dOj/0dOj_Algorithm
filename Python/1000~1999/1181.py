lst = []
for i in range(int(input())):
    lst.append(input())

lst = list(set(lst))

def compare(a, b):
    if len(a) < len(b):
        return a
    elif len(b) < len(a):
        return b
    else:
        if a < b:
            return a
        else:
            return b

sc = 2; lft = []; rgt = []

while sc // 2<= len(lst):
    lst.extend([False] * ((sc - (len(lst) % sc)) % sc))
    for i in range(0, len(lst), sc):
        lft = lst[i:i+(sc//2)]; rgt = lst[i+(sc//2):i+sc]; data = []
        while False == rgt[-1]:
            rgt.pop()
            if rgt == []:
               break
        while False == lft[-1]:
            lft.pop()
            if lft == []:
               break
        while len(lft) != 0 or len(rgt) != 0:
            if len(lft) == 0:
                data.extend(rgt)
                rgt = []
                break  
            if len(rgt) == 0:
                data.extend(lft)
                lft = []
                break
            if compare(lft[0], rgt[0]) == lft[0]: # 비교
                data.append(lft.pop(0))
            else:
                data.append(rgt.pop(0))
        lst[i:i+sc] = data
    sc *= 2

for i in range(len(lst)):
    print(lst[i])