from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for _ in range(n):
    w = input()[::-1]
    for i in range(len(w)):
        dic[w[i]] += 36 ** i

zval = []
val = 0

for i in dic:
    if i.isdigit():
        zval.append((35-int(i)) * dic[i])
        val += int(i) * dic[i]
    else:
        zval.append((90-ord(i)) * dic[i])
        val += (ord(i)-55) * dic[i]

zval.sort(reverse=True)

k = int(input())
ans10 = sum(zval[0:k])+val

def convert(n):
    s, r = divmod(n, 36)
    if s == 0:
        if r >= 10:
            return chr(r+55)
        else:
            return str(r)
    else:
        if r >= 10:
            return convert(s) + chr(r+55)
        else:
            return convert(s) + str(r)
print(convert(ans10))