import sys
input = sys.stdin.readline

cnt = {}
lst = []
mx = 0; mx_lst = []
sm = 0

for i in range(-4000, 4001):
    cnt[i] = 0

N = int(input())
for i in range(N):
    cnt[int(input())] += 1

for i in range(-4000, 4001):
    for j in range(cnt[i]):
        lst.append(i)
        sm += i
    if cnt[i] > mx:
        mx = cnt[i]
        mx_lst = []
        mx_lst.append(i)
    elif cnt[i] == mx:
        mx_lst.append(i)

print(round(sm/len(lst)))
print(lst[len(lst)//2])
if len(mx_lst) == 1:
    print(mx_lst[0])
else:
    print(mx_lst[1])
print(lst[-1] - lst[0])