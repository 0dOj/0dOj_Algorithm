import sys

chessboard = []
N, M = map(int, sys.stdin.readline().split())

for i in range(N):
    line = sys.stdin.readline()
    chessboard.append(line)

def coloring(c): # c는 왼쪽 위가 W인지 B인지를 입력
    coloredCB = ["0" * M] * N
    for i in range(N):
        if i % 2 == 0:
            color = c
        else:
            if c == "W":
                color = "B"
            elif c == "B":
                color = "W"
        for j in range(M):
            if chessboard[i][j] != color:
                coloredCB[i] = coloredCB[i][:j] + "1" + coloredCB[i][j+1:]
            if color == "W":
                color = "B"
            elif color == "B":
                color = "W"

    data = 64
    for i in range(N - 7): # 칸마다 일일히 8*8로 대조하는 방법. 어떻게 해야 더 효율적인 알고리즘을 '구현'할 수 있을까?
        for j in range(M - 7):
            cnt = 0
            for k in range(8):
                cnt += coloredCB[i+k][j:j+8].count('1')
            if cnt < data:
                data = cnt
    
    return data

w = coloring("W")
b = coloring("B")
print(min(w, b))