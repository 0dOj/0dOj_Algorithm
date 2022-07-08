for _ in range(int(input())):
    n = int(input())
    stack = list(map(int, input().split()))

    mx = 0
    prof = 0
    for i in range(n):
        x = stack.pop()
        if x > mx:
            mx = x
        else:
            prof += mx-x
    print(prof)