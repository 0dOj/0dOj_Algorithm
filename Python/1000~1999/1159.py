from collections import defaultdict

dic = defaultdict(int)
for _ in range(int(input())):
    dic[input()[0]] += 1

s = ''
for i in sorted(dic):
    if dic[i] >= 5:
        s += i
if s:
    print(s)
else:
    print('PREDAJA')