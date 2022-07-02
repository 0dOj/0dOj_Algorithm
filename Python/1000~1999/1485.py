for _ in range(int(input())):
    arr = []
    sqaure = True
    for i in range(4):
        arr.append(tuple(map(int, input().split())))
    arr.sort()

    # 1. 4개의 점이 있는가?
    for i in range(3):
        if arr[i] == arr[i+1]:
            sqaure = False

    # 2. 4변의 길이가 같은가?
    arr[2], arr[3] = arr[3], arr[2]
    l = (arr[0][0] - arr[1][0]) ** 2 + (arr[0][1] - arr[1][1]) ** 2
    for i in range(1, 4):
        if l != (arr[i%4][0] - arr[(i+1)%4][0]) ** 2 + (arr[i%4][1] - arr[(i+1)%4][1]) ** 2:
            sqaure = False

    # 3. 대각선의 길이가 같은가?
    if (arr[0][0] - arr[2][0]) ** 2 + (arr[0][1] - arr[2][1]) ** 2 != (arr[1][0] - arr[3][0]) ** 2 + (arr[1][1] - arr[3][1]) ** 2 :
        sqaure = False
    if sqaure: print(1)
    else: print(0)