n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

mx = 0

for i in range(n-3):
    for j in range(m):
        mx = max(mx, arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+3][j])

for i in range(n):
    for j in range(m-3):
        mx = max(mx, arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i][j+3])

for i in range(n-1):
    for j in range(m-1):
        mx = max(mx, arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1])

for i in range(n-1):
    for j in range(m-2):
        a = arr[i][j]; b = arr[i][j+1]; c = arr[i][j+2]
        d = arr[i+1][j]; e = arr[i+1][j+1]; f = arr[i+1][j+2]
        mx = max(mx, max(a+d+b+c, a+d+e+f, a+b+e+c, a+b+e+f, d+b+e+c, d+b+e+f, a+b+c+f, d+e+c+f))

for i in range(n-2):
    for j in range(m-1):
        a = arr[i][j]; b = arr[i][j+1]
        c = arr[i+1][j]; d = arr[i+1][j+1]
        e = arr[i+2][j]; f = arr[i+2][j+1]
        mx = max(mx, max(a+b+c+e, a+b+d+f, a+c+d+e, a+c+d+f, b+c+d+e, b+c+d+f, a+c+e+f, b+d+e+f))

print(mx)