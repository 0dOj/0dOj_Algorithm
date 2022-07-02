n = int(input())
y = [True] * n; a = [True] * (n * 2 - 1); b = [True] * (n * 2 - 1)
cnt = 0
# y:(↓), a:↘ b:↗. 각각 x = 0에서 0번째 줄임.
# r과 c가 주어질 때, a = x-y+(n-1), b = x+y

def DFS(n, x):
    if x == n:
        global cnt
        cnt += 1
        return
    
    for i in range(n):
        if y[i] == True and a[x-i+n-1] == True and b[x+i] == True:
            y[i] = False; a[x-i+n-1] = False; b[x+i] = False
            DFS(n, x+1)
            y[i] = True; a[x-i+n-1] = True; b[x+i] = True

DFS(n, 0)
print(cnt)