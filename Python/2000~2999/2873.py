def move_left(cnt):
    pos[1] -= cnt
    print('L' * (cnt), end = '')

def move_right(cnt):
    pos[1] += cnt
    print('R' * (cnt), end = '')

def move_up(cnt):
    pos[0] -= cnt
    print('U' * (cnt), end = '')

def move_down(cnt):
    pos[0] += cnt
    print('D' * (cnt), end = '')
    
r, c = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

pos = [0, 0]

if r%2 == 0 and c%2 == 0:
    min_sq = [1000, (0, 0)]
    for i in range(r):
        for j in range(c):
            if (i+j)%2 == 1 and arr[i][j] < min_sq[0]:
                min_sq = [arr[i][j], (i, j)]
    i = min_sq[1][0]
    j = min_sq[1][1]

    right = True
    while True:
        if pos[0] == i-i%2:
            down = True
            while True:
                if down and pos[1] != j:
                    move_down(1)
                    down = False
                elif pos[1] != j:
                    move_up(1)
                    down = True

                if pos[0] == i+1-(i%2) and pos[1] == c-1:
                    break
                else:
                    move_right(1)
            right = False

        elif right == True:
            move_right(c-1)
            right = False
        else:
            move_left(c-1)
            right = True

        if pos[0] == r-1:
            break
        else:
            move_down(1)
            

elif r%2 == 1:
    while True:
        if pos[0]%2 == 0:
            move_right(c-1)
        else:
            move_left(c-1)

        if pos[0] == r-1:
            break
        else:
            move_down(1)

else:
    while True:
        if pos[1]%2 == 0:
            move_down(r-1)
        else:
            move_up(r-1)

        if pos[1] == c-1:
            break
        else:
            move_right(1)