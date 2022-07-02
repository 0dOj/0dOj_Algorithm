from sys import stdin
input = stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] |= arr[i][k] & arr[k][j]

for i in range(n):
    print(*arr[i])