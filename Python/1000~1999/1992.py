from sys import stdin
input = stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]

s = ""

def DFS(x1, x2, y1, y2):
    global s

    t = arr[x1][y1]

    for i in range(x1, x2):
        for j in range(y1, y2):
            if t != arr[i][j]:
                s += '('
                DFS(x1, (x1+x2)//2, y1, (y1+y2)//2)
                DFS(x1, (x1+x2)//2, (y1+y2)//2, y2) 
                DFS((x1+x2)//2, x2, y1, (y1+y2)//2)
                DFS((x1+x2)//2, x2, (y1+y2)//2, y2)
                s += ')'
                return

    s += t

DFS(0, n, 0, n)
print(s)