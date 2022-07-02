from collections import deque

n = int(input())

lst = deque([])
for i in range(6):
    lst.append(tuple(map(int, input().split())))
 
while lst[0][0] != lst[2][0] or lst[1][0] != lst[3][0]:
    lst.append(lst.popleft())

print(n * (lst[4][1] * lst[5][1] - lst[1][1] * lst[2][1]))