from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
cols = []
for _ in range(n):
    cols.append(tuple(map(int, input().split())))
cols.sort()

mx = (0, 0)
for col in cols:
    if col[1] > mx[1]:
        mx = col

cols = deque(cols)
height = [0] * 1001; height[mx[0]] = mx[1]
top = 0
for i in range(1, mx[0]):
    if i == cols[0][0]:
        top = max(top, cols.popleft()[1])
    height[i] = top

top = 0
for i in range(1000, mx[0], -1):
    if i == cols[-1][0]:
        top = max(top, cols.pop()[1])
    height[i] = top

result = 0
for i in height:
    result += i
print(result)