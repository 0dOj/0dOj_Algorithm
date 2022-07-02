from sys import stdin
input = stdin.readline

n, m, r = map(int, input().split())
item_list = list(map(int, input().split()))

arr = [[m+1] * n for _ in range(n)]
for i in range(n): arr[i][i] = 0
for _ in range(r):
    a, b, l = map(int, input().split())
    arr[a-1][b-1] = arr[b-1][a-1] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = arr[j][i] = min(arr[i][j], arr[i][k] + arr[k][j])

max_item = 0
for i in range(n):
    item = 0
    for j in range(n):
        if arr[i][j] <= m:
            item += item_list[j]
    max_item = max(max_item, item)
        
print(max_item)