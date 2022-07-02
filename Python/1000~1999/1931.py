from sys import stdin
input = stdin.readline

lst = []
for i in range(int(input())):
    lst.append(tuple(map(int, input().split())))

lst.sort(key = lambda x: (x[1], x[0]))

cnt = 0; t = -1

for i in lst:
    if i[0] >= t:
        cnt += 1
        t = i[1]

print(cnt)