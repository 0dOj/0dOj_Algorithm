import math
import copy
from sys import stdin

inf = math.inf
input = stdin.readline

n, q = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(n)]]
for i in range(n):
    for j in range(n):
        if i != j and arr[0][i][j] == 0:
            arr[0][i][j] = inf

for k in range(n):
    arr.append(copy.deepcopy(arr[-1]))
    for i in range(n):
        for j in range(n):
            arr[-1][i][j] = min(arr[-1][i][j], arr[-1][i][k]+arr[-1][k][j])

for _ in range(q):
    c, s, e = map(int, input().split())
    if arr[c-1][s-1][e-1] == inf:
        print(-1)
    else:
        print(arr[c-1][s-1][e-1])