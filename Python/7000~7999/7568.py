import sys
input = sys.stdin.readline

N = int(input())
lst = []
ans = []

for i in range(N):
    x, y = map(int, input().split())
    lst.append([x, y])

for i in range(N):
    cnt = 1
    for j in range(N):
        if lst[j][0] > lst[i][0] and lst[j][1] > lst[i][1]:
            cnt += 1
    ans.append(cnt)

print(*ans)