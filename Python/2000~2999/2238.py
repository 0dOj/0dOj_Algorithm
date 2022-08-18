from sys import stdin

input = stdin.readline

u, n = map(int, input().split())
arr = [[0, ''] for _ in range(10001)]

for i in range(n):
    s, p = input().split(); p = int(p)
    arr[p][0] += 1
    if not arr[p][1]: arr[p][1] = s

mn = 100001
cost = 0
for i in range(10001):
    if 0 < arr[i][0] < mn:
        mn = arr[i][0]
        cost = i

print(arr[cost][1], cost)