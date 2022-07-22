from sys import stdin

input = stdin.readline

n = int(input())
arr = tuple(tuple(map(int, input().split())) for _ in range(n))
if n == 2:
    print(min(arr[0][0]+min(arr[1][1], arr[1][2]), arr[0][1]+min(arr[1][0], arr[1][2]), arr[0][2]+min(arr[1][0], arr[1][1])))
    exit(0)

mn = 1000000
dpr, dpg, dpb = [0]*n, [0]*n, [0]*n

def dp():
    for i in range(2, n):
        dpr[i] = min(dpg[i-1], dpb[i-1]) + arr[i][0]
        dpg[i] = min(dpr[i-1], dpb[i-1]) + arr[i][1]
        dpb[i] = min(dpr[i-1], dpg[i-1]) + arr[i][2]

dpr[1], dpg[1], dpb[1] = 1000000, arr[0][0]+arr[1][1], arr[0][0]+arr[1][2]
dp()
mn = min(mn, dpg[-1], dpb[-1])

dpr[1], dpg[1], dpb[1] = arr[0][1]+arr[1][0], 1000000, arr[0][1]+arr[1][2]
dp()
mn = min(mn, dpr[-1], dpb[-1])

dpr[1], dpg[1], dpb[1] = arr[0][2]+arr[1][0], arr[0][2]+arr[1][1], 1000000
dp()
mn = min(mn, dpr[-1], dpg[-1])

print(mn)