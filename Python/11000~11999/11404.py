import math
from sys import stdin
input = stdin.readline

n = int(input())
m = int(input())

arr = [[math.inf] * n for _ in range(n)]
for i in range(n): arr[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a-1][b-1] = min(arr[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

for i in range(n):
    for j in range(n):
        if arr[i][j] == math.inf: arr[i][j] = 0

for i in range(n):
    print(*arr[i])