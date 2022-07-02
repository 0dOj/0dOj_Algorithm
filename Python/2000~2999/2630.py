import sys
input = sys.stdin.readline

n = int(input())
arr = []
cnt0 = 0; cnt1 = 0

for i in range(n):
    arr.append(list(map(int, input().split())))

def DFS(x1, x2, y1, y2):
    t = arr[y1][x1]
    for i in range(y1, y2):
        for j in range(x1, x2):
            if arr[i][j] != t:
                DFS(x1, (x1+x2)//2, y1, (y1+y2)//2)
                DFS((x1+x2)//2, x2, y1, (y1+y2)//2)
                DFS(x1, (x1+x2)//2, (y1+y2)//2, y2)
                DFS((x1+x2)//2, x2, (y1+y2)//2, y2)
                return
    if t == 0: global cnt0; cnt0 += 1
    elif t == 1: global cnt1; cnt1 += 1

DFS(0, n, 0, n)
print(cnt0)
print(cnt1)