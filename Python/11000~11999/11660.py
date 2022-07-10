from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

arr_sum = [[0]*(n+1)] + [[0] for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr_sum[i+1].append(arr_sum[i+1][j] + arr[i][j])
    for j in range(n):
        arr_sum[i+1][j+1] += arr_sum[i][j+1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr_sum[x2][y2] - arr_sum[x2][y1-1] - arr_sum[x1-1][y2] + arr_sum[x1-1][y1-1])