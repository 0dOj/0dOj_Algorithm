from collections import deque

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

lst = [board]

x = (1,-1,0,0)
y = (0,0,1,-1)

def move(dx, dy):
    board_next = [[] for _ in range(n)]

    for i in range(n):
        line = deque([])
        if dx:
            for j in range(n-1, -1, -1) if dx == -1 else range(n):
                if board[i][j]: line.append(board[i][j])
        if dy:
            for j in range(n-1, -1, -1) if dy == -1 else range(n):
                if board[j][i]: line.append(board[j][i])

        line_next = []
        while len(line) > 1:
            if line[0] == line[1]:
                line_next.append(line.popleft()*2)
                line.popleft()
            else:
                line_next.append(line.popleft())
        line_next += list(line)
        while len(line_next) != n: line_next.append(0)
        if dx == -1 or dy == -1: line_next.reverse()

        if dx:
            board_next[i] = line_next
        if dy:
            for j in range(n):
                board_next[j].append(line_next[j])
    
    return board_next

for _ in range(5):
    q = deque(lst)
    lst = []
    while q:
        board = q.popleft()
        for k in range(4):
            lst.append(move(x[k], y[k]))

mx = 0
for board in lst:
    for i in range(n):
        for j in range(n):
            mx = max(mx, board[i][j])
print(mx)