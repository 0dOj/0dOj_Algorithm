from sys import stdin
input = stdin.readline

N = int(input())
lst = list(map(int, (input().split())))

for i in range(N):
    lst[i] = [lst[i], i]

lst.sort(key=lambda x:(x[0]))

cnt = 0; lst[0].append(0)
for i in range(1, N):
    if lst[i][0] == lst[i-1][0]:
        lst[i].append(lst[i-1][2])
    else:
        lst[i].append(lst[i-1][2] + 1)

lst.sort(key=lambda x:(x[1]))
ans = []

for i in range(N):
    ans.append(lst[i][2])

print(*ans)