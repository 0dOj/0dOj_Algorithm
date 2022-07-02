from sys import stdin
input = stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

cntm1 = 0; cnt0 = 0; cntp1 = 0 

def DFS(n, x1, x2, y1, y2):
    t = arr[x1][y1]
    for i in range(x1, x2):
        for j in range(y1, y2):
            if arr[i][j] != t:
                xslice = (x1, (x1*2+x2)//3, (x1+x2*2)//3, x2)
                yslice = (y1, (y1*2+y2)//3, (y1+y2*2)//3, y2)
                for i in range(3):
                    for j in range(3):
                        DFS(n//3, xslice[i], xslice[i+1], yslice[j], yslice[j+1])
                return
    if t == -1: global cntm1; cntm1 += 1
    if t == 0: global cnt0; cnt0 += 1
    if t == 1: global cntp1; cntp1 += 1
    
DFS(n, 0, n, 0, n)
print(cntm1)
print(cnt0)
print(cntp1)